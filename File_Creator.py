__author__ = 'dkatz'

from re import *
from xlwt import *


class WriteFile(object):
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
        search_pattern = compile(ur"(?:\d{2}\/\d{2}\/\d{4})|(\d{4,})")
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
            self.edit_sheet.write(r, col, key)
            self.data_write(col, r, key)
            col += 1

    def data_write(self, col, row, k):
        """
        Writes CTID #'s to columns beneath the appropriate column heading.
        :param col:
        :param row:
        :param k:
        :return:
        """
        for value in self.d[k]:
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
