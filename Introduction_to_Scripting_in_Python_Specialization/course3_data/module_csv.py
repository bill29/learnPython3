"""
Using the csv module.
"""

# csv nay no lam cho het , va no nhan biet duoc dau la row va dau la ko row y ma. cai kia la 
# ko bat khoang cach , ko sao dau

import csv

def parse(csvfilename):
    """
    Reads CSV file named csvfilename, parses
    it's content and returns the data within
    the file as a list of lists.
    """
    table = []
    with open(csvfilename, "r") as csvfile:
        csvreader = csv.reader(csvfile,
                               skipinitialspace=True)
        for row in csvreader:
            table.append(row)
    return table


def print_table(table):
    """
    Print out table, which must be a list
    of lists, in a nicely formatted way.
    """
    for row in table:
        # Header column left justified
        print("{:<19}".format(row[0]), end='')
        # Remaining columns right justified
        for col in row[1:]:
            print("{:>4}".format(col), end=' ')
        print("", end='\n')

table = parse("hightemp.csv")
print_table(table)

print("")
print("")

table2 = parse("hightemp2.csv")
print_table(table2)