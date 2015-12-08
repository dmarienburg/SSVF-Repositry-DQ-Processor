__author__ = 'David Katz-Wigmore'

from re import *
from xlwt import *


class WriteFile(object):
    service_point_equivalent_field_names = {
        "Name": "First/Last Name",
        "Social Security Number": "SSID",
        "Date of Birth": "DoB",
        "Race": "Race 1",
        "Ethnicity": "Ethnicity",
        "Gender": "Gender",
        "Veteran Status": "Veteran Status",
        "Disabling Condition": "Disabling Condition",
        "Homeless Living Situation": "Residence Prior to Project Entry",
        "Project Entry Date": "Entry Date",
        "Project Exit Date": "Exit Date",
        "Destination": "Exit Destination",
        "Personal ID": "CTID",
        "Household ID": "Household ID",
        "Relationship to Head of Household": "Relationship to Head of Household",
        "Client Location": "Client Location",
        "Length of Time on Street": "Total Number of Months Continuously Homeless Immediately Prior to Project Entry",
        "Income Sources (Entry)": "Monthly Income (HUD) <-- in the Entry",
        "Income Sources (Exit)": "Monthly Income (HUD) <-- in the Exit",
        "Non-Cash Benefits (Entry)": "Non-Cash Benefits (HUD) <-- in the Entry",
        "Non-Cash Benefits (Exit)": "Non-Cash Benefits (HUD) <-- in the Exit",
        "Insurance (Entry)": "Health Insurance (HUD) <-- in the Entry",
        "Insurance (Exit)": "Health Insurance (HUD) <-- in the Exit",
        "Services Provided": "Services Provided",
        "Financial Assistance Provided": "Financial Assistance Provided <-- in each service",
        "Move-In Date": "Initial Placement/Eviction Prevention Date",
        "Non-Homeless Living Situation": "Residence Prior to Project Entry Does Not Equal Homeless",
        "Date of Move-In": "Placement Date <-- in Client's Residence / Last Permanent Address",
        "Year Entered Military Service": "Year Entered Military Service",
        "Year Separated from Military Service": "Year Separated from Military Service",
        "Theaters of Operation": "Combat/War Zone",
        "Military Branch": "Military Branch",
        "Discharge Status": "Discharge Type",
        "HP Screening Score": "HP Screening Score",
        "Household Income as a % of AMI": "Percentage of AMI",
        "Last Permanent Address": "Client's Residence / Last Permanent Address",
        "Total Monthly Income (Entry)": "Total Monthly Income (Entry)",
        "Total Monthly Income (Exit)": "Total Monthly Income (Exit)",
        "Continuously Homeless One Year": "Continuously Homeless for at Least One Year",
        "Times Homeless Past Three Years": "Number of Times the Client has been Homeless in the Past Three Years",
        "No Head of Household": "Relationship to Head of Household & Head of Household",
        "Residence Prior to Project Entry": "Residence Prior to Project Entry",
        "Multiple Heads of Household": "Relationship to Head of Household & Head of Household",
        "VAMC Station Number": "VAMC Station Number",
        "Very High Monthly Income (Entry)": "Total Monthly Income/Monthly Income (HUD)/Percentage of AMI/"
                                            "Percent of Median Family Income",
        "Very High Monthly Income (Exit)": "Total Monthly Income/Monthly Income (HUD)/Percentage of AMI/"
                                            "Percent of Median Family Income"
    }

    def __init__(self, title, data_dict):
        self.data_dict = data_dict
        self.title = title
        self.d = {}
        self.wb = Workbook()
        self.edit_sheet = self.wb.add_sheet("DQ")
        self.run()

    def ctid_finder(self, data, d):
        """
        Finds CTID #'s by searching through the data's values using regex.
        :param data:
        :param d:
        :return:
        """
        search_pattern = compile(u"(?:\d{2}\/\d{2}\/\d{4})|(\d{4,})")
        for key in data:
            #  print "Wub!"
            d[key] = findall(search_pattern, self.data_dict[key])

    def title_write(self, data):
        """
        Writes the column heads to the excel sheet.
        :param data:
        :return:
        """
        col = 0
        for key in data.keys():
            r = 0
            #  print "Ping!"
            #  print "Col: %d, Row: %d" % (col, r)
            #  print key
            self.edit_sheet.write(r, col, self.service_point_equivalent_field_names[key])
            self.data_write(col, r, key)
            col += 1

    def data_write(self, col, row, key):
        """
        Writes CTID #'s to columns beneath the appropriate column heading.
        :param col:
        :param row:
        :param key:
        :return:
        """
        for value in self.d[key]:
            try:
                if int(value) > 1:
                    row += 1
                    #  print "Pong!"
                    #  print "Col: %d, Row: %d" % (col, row)
                    #  print value
                    self.edit_sheet.write(row, col, int(value))
                else:
                    pass
            except ValueError:
                pass
            else:
                pass

    def run(self):
        """
        Initializes the class methods in sequence.
        :return:
        """
        self.ctid_finder(self.data_dict, self.d)
        self.title_write(self.d)
        self.wb.save(self.title)
