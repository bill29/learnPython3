"""
Week 3 practice project template for Python Data Analysis
Reading and writing CSV files using lists
"""


import csv


#########################################################
# Part 1 - Week 3

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      A list of strings corresponding to the field names in 
      the given CSV file.
    """
    table = []
    with open(filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table.append(row)
    return table[0]



def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, 'rt') as csvfile:
        csvfile = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for line in csvfile:
            table.append(line)
    return table

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the 
      field values for that row.
    """
    table = {}
    with open(filename, "rt", newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table[row[keyfield]] = row
    return table
def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    table1 = []
    for line in table:
        table2 = []
        for field_name in fieldnames:
            table2.append(line[field_name])
        table1.append(table2)
    with open(filename, 'w', newline='') as csv_file:
        csv_write = csv.writer(csv_file, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
        print(fieldnames)
        csv_write.writerow(fieldnames)
        for line in table1:
            csv_write.writerow(line)
            print(line)


# def print_table(table):
#     """
#     Echo a nested listto the console
#     """
#     print(table)
#     for row in table:
#         print(row)

  
# def test_part1_code():
#     """
#     Run examples that test the functions for part 1
#     """
#     field_names = read_csv_fieldnames('test.csv',',',"'")
#     table = read_csv_as_list_dict('test.csv',',',"'")
#     table2 = read_csv_as_nested_dict('test.csv','ten',',',"'")

#     write_csv_from_list_dict('test3.txt',table,field_names,',',"'")

    
#     # Test whether two tables are the samevanprint_table(table)
#     print('====')
#     #print_table(table2)

# test_part1_code()

