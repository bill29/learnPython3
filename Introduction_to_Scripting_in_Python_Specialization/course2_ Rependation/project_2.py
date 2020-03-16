"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)



    if(len1 == 0 or len2 == 0):
      return 0
    elif len1 == len2:
      for i in range(len1):
        if line1[i] != line2[i]:
          return i
      return IDENTICAL
    elif len1 > len2:
      for i in range(len2):
        if line1[i] != line2[i]:
          return i
      return i+1
    else:
      for i in range(len1):
        if line2[i] != line1[i]:
          return i
      return i+1



# line1 ="abcd21321312"
# line2 ="abvfdvfdvdff"
# test=singleline_diff(line1,line2)
# print(test)

def check_contain(line):
  for char_in_line in line:
    if char_in_line == "\n" or char_in_line == "\r":
      return -1
  return 1


# line1 = "nguyen minh dan "

# print(check_contain(line1))


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if idx < 0 or check_contain(line1) == -1 or check_contain(line2) == -1:
      return ""
    else:
      line_between = "="*idx + "^\n"
      return line1 + "\n" + line_between  + line2 + "\n"
# line1 ="abcd21321312\n"
# line2 ="abvfdvfdvdff\n"
# print(singleline_diff_format(line1,line2,singleline_diff(line1,line2)))
print(singleline_diff_format("abc", "abd", 2))
def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    len1 = len(lines1)
    len2 = len(lines2)
    if(len1 == len2):
      for i in range(len1):
        if(singleline_diff(lines2[i], lines1[i]) != IDENTICAL):
          my_tuple = (i, singleline_diff(lines2[i], lines1[i]))
          return my_tuple
      return (IDENTICAL, IDENTICAL)
    elif len1 < len2:
      for i in range(len1):
        if(singleline_diff(lines1[i], lines2[i]) != IDENTICAL):
          my_tuple = (i, singleline_diff(lines2[i], lines1[i]))
          return my_tuple
      return (len1, 0)
    elif len1 > len2:
      for i in range(len2):
        if(singleline_diff(lines1[i], lines2[i]) != IDENTICAL):
          my_tuple = (i, singleline_diff(lines2[i], lines1[i]))
          print(lines1[i],lines2[i])
          return my_tuple
      return (len2, 0)

def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    datafile = open(filename, "rt")
    list_line = []
    for line in datafile.readlines():
      if line[-1] == "\n" or line[-1] == "\r":
        line = line[:-1]
      list_line.append(line)
      datafile.close()
    return list_line

#print(get_file_lines("sai.py"))
def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """

    list1 = get_file_lines(filename1)

    list2 = get_file_lines(filename2)
    final_tuple = multiline_diff(list1, list2)
    if final_tuple == (IDENTICAL, IDENTICAL):
      return "No differences\n"
    else:
      final_string ="Line "
      line_diff = final_tuple[0]
      index_diff = final_tuple[1]
      print(line_diff, index_diff)
      print(singleline_diff_format(list1[line_diff], list2[line_diff], index_diff))

      return 0


