__author__ = 'dkatz'

import ttk
from File_Creator import WriteFile
from Tkinter import *

val_dict = {}

def addition():
    """
    Adds a new value to the val_dict where the catagory is the key and the ctid#'s (along with the other included
    information) is the value.
    :return:
    """
    val_dict[category_var.get()] = value_var.get()
    set_list()

def set_list():
    """
    Defines the listbox that displays the keys & values of the val_dict.
    :return:
    """
    listbox1.delete(0, END)
    listbox2.delete(0, END)
    for key in val_dict.keys():
        listbox1.insert(END, key)
        listbox2.insert(END, val_dict[key])

def process():
    """
    Calls the WriteFile function, which converts the val_dict into an excel file and prints the name the document will
    be given to the terminal.
    :return:
    """
    name = agency_var.get() + " " + grant_var.get() + " " + hp_rrh_var.get() + ".xls"
    print name
    WriteFile(str(name), val_dict)

def clear_all():
    """
    Clears the values from the listboxes and the val_dict allowing a new report to be processed without restarting the
    application.
    :return:
    """
    val_dict.clear()
    listbox1.delete(0, END)
    listbox2.delete(0, END)

root = Tk()
root.title("SSVF Repository DQ Processor")

agency_var = StringVar()
grant_var = StringVar()
hp_rrh_var = StringVar()
category_var = StringVar()
value_var = StringVar()

mainframe = ttk.Frame(root, padding="3 3 3 3")
mainframe.grid(column=1, row=1, sticky=(N, W, S, E))
mainframe.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)

lower_frame = ttk.Frame(root, padding="3 3 3 3")
lower_frame.grid(column=1, row=4, sticky=(N, W, S, E))
lower_frame.rowconfigure(0, weight=1)
lower_frame.columnconfigure(0, weight=1)

reporting_categories = sorted(["Choose a reporting category",
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
                               "Very High Monthly Income (Exit)"])

agency_choices = ["-",
                  "Central City Concern",
                  "Human Solutions",
                  "Impact North West",
                  "NAYA",
                  "North West Pilot Projects",
                  "Transition Projects"]

grant_choices = ["-", "C15", "ZZ-127"]

hp_or_rrh = ["-", "HP", "RRH"]

ttk.Label(mainframe, text="Agency:").grid(column=1, row=1, sticky=N)
ttk.Label(mainframe, text="Grant:").grid(column=2, row=1, sticky=N)
ttk.Label(mainframe, text="HP or RRH:").grid(column=3, row=1, sticky=N)

OptionMenu(mainframe, agency_var, *agency_choices).grid(column=1, row=2, sticky=N)
agency_var.set("-")
OptionMenu(mainframe, grant_var, *grant_choices).grid(column=2, row=2, sticky=N)
grant_var.set("-")
OptionMenu(mainframe, hp_rrh_var, *hp_or_rrh).grid(column=3, row=2, sticky=N)
hp_rrh_var.set("-")

OptionMenu(mainframe, category_var, *reporting_categories).grid(column=1, row=3, sticky=(N, W))
ttk.Entry(mainframe, textvariable=value_var).grid(column=2, row=3, sticky=(N, W, E))
b = ttk.Button(mainframe, command=addition, text="Add")
b.grid(column=3, row=3, sticky=(N, E))

y_scroll = Scrollbar(lower_frame, orient=VERTICAL)
y_scroll.grid(column=3, row=0, sticky=(N, S))
listbox1 = Listbox(lower_frame, width=30, yscrollcommand=y_scroll.set)
listbox1.grid(column=1, row=0, sticky=(N, W, E))
listbox2 = Listbox(lower_frame, width=30, yscrollcommand=y_scroll.set)
listbox2.grid(column=2, row=0, sticky=(N, W, E))
y_scroll["command"] = listbox1.yview
y_scroll["command"] = listbox2.yview

ttk.Button(lower_frame, command=process, text="Process").grid(column=3, row=1, sticky=W)
ttk.Button(lower_frame, command=clear_all, text="Clear Data").grid(column=2, row=1, sticky=W)

root.mainloop()
