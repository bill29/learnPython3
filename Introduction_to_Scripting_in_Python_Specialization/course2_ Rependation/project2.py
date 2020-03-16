"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def min(num1,num2):
  if num1 <= num2 :
    return num1
  else:
    return num2

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
    if line1 == "":
      if len(line2) >= 1:
        return 0
      else:
        return IDENTICAL
    elif line2 == "":
      if len(line1) >= 1:
        return 0
    else:
      if len(line1) == len(line2):
        for i in range(len(line1)):
          if line1[i] != line2[i]:
            return i
        return IDENTICAL
      else:
        num_less = min(len(line1), len(line2))
        for i in range(num_less):
          if line1[i] != line2[i]:
            return i # if diff in range(less len) return i , else return last less than
        return num_less

# line1 = "anhdan"
# line2 = "anhdan"
# print(singleline_diff(line2,line1))


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
    if idx == 0 :
      if line1 == '' and line2 == '':
        return '\n^\n\n'
      elif line1 == '' and line2 != '':
        return '\n^\n' + line2 +'\n'
      else:
        return line1 +'\n^\n' + line2 +'\n'
    elif idx < 0 or idx > min(len(line1), len(line2)):
      return ""
    else:
      return line1 +'\n' + '='*idx +'^' +"\n" + line2 + '\n'


# line1 = "anhdan"
# line2 = "anhdan"
# print(singleline_diff_format(line1,line2,2))

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
    lines_less = min(len(lines1), len(lines2))
    if len(lines1) == 0 and len(lines2) ==0:
      return (IDENTICAL,IDENTICAL)
    elif lines_less == 0:
      return (0,0)
    elif len(lines1) == len(lines2):
      for i in range(len(lines1)):
        if singleline_diff(lines1[i], lines2[i]) != IDENTICAL:
          return (i, singleline_diff(lines1[i], lines2[i]))
      return (IDENTICAL, IDENTICAL)
    else:
      for i in range(lines_less):
        if singleline_diff(lines1[i], lines2[i]) != IDENTICAL:
          return (i, singleline_diff(lines1[i], lines2[i]))
      return (i+1, 0)


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
    list_return = []

    for line in datafile.readlines():
      if line[-1] == "\n":
        line = line[:-1]
      list_return.append(line)
    datafile.close()
    return list_return
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
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)

    tuple_diff = multiline_diff(lines1, lines2)
    line_diff = tuple_diff[0]
    index_diff = tuple_diff[1]

    #print(line_diff)
    #print(index_diff)

    # print(lines1[line_diff])
    #print(lines2[line_diff])
    min_lines = min(len(lines1), len(lines2))
    if tuple_diff == (IDENTICAL, IDENTICAL):
      return "No differences\n"
    elif tuple_diff == (min_lines, 0) and len(lines2) > min_lines:
      return "Line " + str(line_diff) +":\n" + singleline_diff_format("",lines2[min_lines],0)
    elif tuple_diff == (min_lines, 0) and len(lines1) > min_lines:
      return "Line " + str(line_diff) +":\n" + singleline_diff_format(lines1[min_lines],"",0)
    return "Line " + str(line_diff) + ":\n" + singleline_diff_format(lines1[line_diff], lines2[line_diff], index_diff) 




