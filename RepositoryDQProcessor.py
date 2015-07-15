__author__ = 'dkatz'

import ttk
from File_Creator import WriteFile
import Tkinter as tk

import Get_Providers


class App(tk.Frame):
    def __init__(self, master, dictionary):
        """
        Initializes the main frame which will be known as self
        :param master:
        :param dictionary:
        :return:
        """
        tk.Frame.__init__(self, master)

        self.grid(column=0, row=1, sticky="N,W,S,E")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.dict = dictionary
        self.values_dict = {}

        self.grant_choices = ["C15", "ZZ-127"]
        self.hp_or_rrh = ["HP", "RRH"]
        self.reporting_categories = sorted(["Choose a reporting category",
                                            "Name",
                                            "Social Security Number",
                                            "Date of Birth",
                                            "Race",
                                            "Ethnicity",
                                            "Gender",
                                            "Veteran Status",
                                            "Disabling Condition",
                                            "Homeless Living Situation",
                                            "Project Entry Date",
                                            "Project Exit Date",
                                            "Destination",
                                            "Personal ID",
                                            "Household ID",
                                            "Relationship to Head of Household",
                                            "Client Location",
                                            "Length of Time on Street",
                                            "Income Sources (Entry)",
                                            "Income Sources (Exit)",
                                            "Non-Cash Benefits (Entry)",
                                            "Non-Cash Benefits (Exit)",
                                            "Insurance (Entry)",
                                            "Insurance (Exit)",
                                            "Services Provided",
                                            "Financial Assistance Provided",
                                            "Move-In Date",
                                            "Non-Homeless Living Situation",
                                            "Date of Move-In",
                                            "Year Entered Military Service",
                                            "Year Separated from Military Service",
                                            "Theaters of Operation",
                                            "Military Branch",
                                            "Discharge Status",
                                            "Household Income as a % of AMI",
                                            "Last Permanent Address",
                                            "Total Monthly Income (Entry)",
                                            "Total Monthly Income (Exit)",
                                            "Continuously Homeless One Year",
                                            "Times Homeless Past Three Years",
                                            "No Head of Household",
                                            "Residence Prior to Project Entry",
                                            "Multiple Heads of Household",
                                            "Very High Monthly Income (Entry)",
                                            "Very High Monthly Income (Exit)"
                                            ])

        self.state = tk.StringVar(self)
        self.provider = tk.StringVar(self)
        self.hp_rrh = tk.StringVar(self)
        self.grant = tk.StringVar(self)
        self.reporting_category = tk.StringVar(self)
        self.value = tk.StringVar(self)

        self.state.trace("w", self.update_options)

        self.state_menu = tk.OptionMenu(self, self.state, *self.dict.keys())
        self.provider_menu = tk.OptionMenu(self, self.provider, "")
        self.hp_rrh_menu = tk.OptionMenu(self, self.hp_rrh, *self.hp_or_rrh)
        self.grant_menu = tk.OptionMenu(self, self.grant, *self.grant_choices)
        self.reporting_categories_menu = tk.OptionMenu(self, self.reporting_category, *self.reporting_categories)

        self.values = ttk.Entry(self, width=48, textvariable=self.value)
        self.add_button = ttk.Button(self, command=self.addition, text="Add")

        self.tree = ttk.Treeview(self,
                                 columns=("Reporting Category", "Error Values"),
                                 selectmode="extended",
                                 show="headings"
                                 )
        self.tree.column("#0", width=10)
        self.tree.column("Reporting Category", width=50)
        self.tree.heading(0, text="Reporting Category")
        self.tree.heading(1, text="Error Values")

        self.y_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.y_scroll.set)

        self.clear = ttk.Button(self, command=self.clear_all, text="Clear All")
        self.process_button = ttk.Button(self, command=self.process, text="Process")

        self.state.set("Select Your State")
        self.provider.set("Select Your Provider")
        self.grant.set("Select Your Grant")
        self.hp_rrh.set("Select HP or RRH")
        self.reporting_category.set("Choose the Reporting Category")

        self.state_menu.grid(column=0, row=1, padx=2, sticky="E")
        self.provider_menu.grid(column=1, row=1, padx=2, sticky="E")
        self.grant_menu.grid(column=2, row=1, padx=2, sticky="W")
        self.hp_rrh_menu.grid(column=3, row=1, padx=2, sticky="w")
        self.reporting_categories_menu.grid(column=0, row=2, padx=2, sticky="E")
        self.values.grid(column=1, columnspan=2, row=2, sticky="W, E")
        self.add_button.grid(column=3, row=2, sticky="W")
        self.tree.grid(column=0, columnspan=4, row=3, sticky="E, W")
        self.y_scroll.grid(column=4, row=3, sticky="N, W, S")
        self.clear.grid(column=2, row=4, sticky="E")
        self.process_button.grid(column=3, row=4, sticky="E")

    def addition(self):
        """
        Adds a new value to the val_dict where the category is the key and the ctid#'s (along with the other included
        information) is the value.
        :return:
        """
        self.values_dict[self.reporting_category.get()] = self.value.get()
        self.set_list()

    def clear_all(self):
        """
        Clears all the values from the tree widget and the value_dict allowing a new report to be processed
        without closing and re-opening the program.
        :return:
        """
        self.values_dict.clear()
        for child_id in self.tree.get_children():
            self.tree.delete(child_id)

    def process(self):
        """
        Calls the WriteFile function, which converts the value_dict into an excel file.
        The name of this file will be printed to the terminal window to show that the process
        is complete
        :return:
        """
        name = self.provider.get() + " " + self.grant.get() + " " + self.hp_rrh.get() + ".xls"
        try:
            WriteFile(str(name), self.values_dict)
            print(name)
        except ValueError:
            print("An error occurred and your file was not saved.")

    def set_list(self):
        """
        defines the listbox that displays the keys & values of the values_dict.
        :return:
        """
        for child_id in self.tree.get_children():
            self.tree.delete(child_id)
        for key in self.values_dict.keys():
            self.tree.insert("", index="end", values=(key, self.values_dict[key]))

    def update_options(self, *args):
        """
        This method allows the provider menu to update depending on which state is selected.
        :param args:
        :return:
        """
        providers = self.dict[self.state.get()]

        menu = self.provider_menu["menu"]
        menu.delete(0, 'end')

        for provider in providers:
            menu.add_command(label=provider, command=lambda region=provider: self.provider.set(region))


if __name__ == "__main__":
    root = tk.Tk()
    make_dict = Get_Providers.MakeDictionary()
    app = App(root, make_dict.read_csv())
    app.mainloop()
