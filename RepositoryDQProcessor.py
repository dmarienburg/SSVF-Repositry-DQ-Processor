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

        self.add_button = ttk.Button(self, command=self.addition, text="Add")

        self.y_scroll = tk.Scrollbar(self, orient="vertical")
        self.list_box1 = tk.Listbox(self, width=30, yscrollcommand=self.y_scroll.set)
        self.list_box2 = tk.Listbox(self, width=30, yscrollcommand=self.y_scroll.set)
        self.y_scroll["command"] = self.list_box1.yview
        self.y_scroll["command"] = self.list_box2.yview

        self.state.set("Select Your State")
        self.provider.set("Select Your Provider")
        self.grant.set("Select Your Grant")
        self.hp_rrh.set("Select HP or RRH")
        self.reporting_category.set("Choose the Reporting Category")

        self.state_menu.pack(side="top")
        self.provider_menu.pack(side="top")
        self.hp_rrh_menu.pack(side="top")
        self.grant_menu.pack(side="top")
        self.add_button.pack()
        self.y_scroll.pack(side="bottom", fill="y")
        self.list_box1.pack(side="bottom")
        self.list_box2.pack(side="bottom")
        self.pack()

    def addition(self):
        """
        Adds a new value to the val_dict where the catagory is the key and the ctid#'s (along with the other included
        information) is the value.
        :return:
        """
        self.values_dict[self.reporting_category.get()] = self.value.get()
        self.set_list()

    def set_list(self):
        """
        defines the listbox that displays the keys & values of the values_dict.
        :return:
        """
        self.list_box1.delete(0, End)
        self.list_box2.delete(0, End)
        for key in self.values_dict.keys():
            self.list_box1.insert(END, key)
            self.list_box2.insert(END, self.values_dict[key])

    def update_options(self, *args):
        """
        This method allows the provider menu to update depending on which state is selected.
        :param args:
        :return:
        """
        countries = self.dict[self.state.get()]
        self.provider.set(countries[0])

        menu = self.provider_menu["menu"]
        menu.delete(0, 'end')

        for country in countries:
            menu.add_command(label=country, command=lambda nation=country: self.provider.set(nation))


if __name__ == "__main__":
    root = tk.Tk()
    make_dict = Get_Providers.MakeDictionary()
    app = App(root, make_dict.read_csv())
    app.mainloop()
