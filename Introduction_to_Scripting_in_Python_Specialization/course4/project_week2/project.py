"""
Project for Week 2 of "Python Data Visualization".
Read World Bank GDP data and create some basic XY plots.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import pygal
import nhap

import matplotlib.pyplot as plt
Billion = 10**9
def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename,'rt',newline='') as csvfile:
      csv_reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
      for row in csv_reader:
        rowid = row[keyfield]
        table[rowid]=row
    return table

def build_plot_values(gdpinfo,gdpdata):
    """
    Inputs:
      gdpinfo - GDP data information dictionary
      gdpdata - A single country's GDP stored in a dictionary whose
                keys are strings indicating a year and whose values
                are strings indicating the country's corresponding GDP
                for that year.
    
    Output: 
      Returns a list of tuples of the form (year, GDP) for the years
      between "min_year" and "max_year", inclusive, from gdpinfo that
      exist in gdpdata.  The year will be an integer and the GDP will
      be a float.
    """
    table = []
    gdpdata_clear = {} # a list for coppy dict gdp data and convert foat gdp data
    for k,v in gdpdata.items():
      try:
        gdpdata_clear[int(k)] = float(v)
      except:
        pass
    #print('PRINT DATA AFTER CLEAR DATA ')
    #print(gdpdata_clear)
    min_max_year = range(int(gdpinfo['min_year'])-1, int(gdpinfo['max_year'])+1)
    for year in min_max_year:
      if year in gdpdata_clear: # check year in list
        table.append((year,gdpdata_clear[year]))
    return table

def build_plot_dict(gdpinfo, country_list):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names

    Output:
      Returns a dictionary whose keys are the country names in
      country_list and whose values are lists of XY plot values 
      computed from the CSV file described by gdpinfo.

      Countries from country_list that do not appear in the
      CSV file should still be in the output dictionary, but
      with an empty XY plot value list.
    """
    dict_of_gdp_by_country = {} # a list return
    nested_dict = read_csv_as_nested_dict(gdpinfo['gdpfile'],gdpinfo['country_name'],gdpinfo['separator'],gdpinfo['quote'])
    #dict read by csv file
    for country in country_list:
      gdpdata = nested_dict[country] # data of single country gdp
      dict_of_gdp_by_country[country]=build_plot_values(gdpinfo,gdpdata)
    return dict_of_gdp_by_country

def render_xy_plot(gdpinfo, country_list, plot_file):
    """
    Inputs:
      gdpinfo      - GDP data information dictionary
      country_list - List of strings that are country names
      plot_file    - String that is the output plot file name

    Output:
      Returns None.

    Action:
      Creates an SVG image of an XY plot for the GDP data
      specified by gdpinfo for the countries in country_list.
      The image will be stored in a file named by plot_file.
    """
    list_country_gdp = build_plot_dict(gdpinfo, country_list)
    print(list_country_gdp)
    XYplot = pygal.XY(height = 400)
    XYplot.title = 'Plot of GDP for select country spanning 1960 -2015'
    for country in list_country_gdp:
      XYplot.add(country, list_country_gdp[country])
    XYplot.render_to_file(plot_file)
    return

def render_by_plot(gdpinfo,country_list):
  dict_country_gdp = build_plot_dict(gdpinfo,country_list)
  plot_name = 'GDP OF '
  for country_name in country_list:
    plot_name +=country_name + ' ' # create a name of plot for many country
    country_gdp_update = nhap.suitable_data(dict_country_gdp[country_name]) # suitable dgp by billion
    x_label = []
    y_label = []
    for year_gdp in country_gdp_update:
      if year_gdp[0]%10 == 0:
        x_label.append(year_gdp[0])
        y_label.append(int(year_gdp[1]))
    print(country_name)
    print(x_label)
    print(y_label)
    plt.plot(x_label,y_label,label = country_name)
  plot_name += ' From {} to {}'.format(gdpinfo['min_year'], gdpinfo['max_year'])
  plt.title(plot_name)
  plt.xlabel('Year')
  plt.ylabel('GDP from GDP (Billion Dolar)')
  plt.legend(loc='best')
  plt.show()

def test_render_xy_plot():
    """
    Code to exercise render_xy_plot and generate plots from
    actual GDP data.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }
    # print('Dau tien la khong in cua quoc gia nao')
    # render_xy_plot(gdpinfo, [], "isp_gdp_xy_none.svg")
    # print('trung quoc')
    # render_xy_plot(gdpinfo, ["China"], "isp_gdp_xy_china.svg")
    # print(' United KIngdom')
    # render_xy_plot(gdpinfo, ["United Kingdom", "United States"],
    #                "isp_gdp_xy_uk+usa.svg")
    render_by_plot(gdpinfo, ['China','United Kingdom','United States', 'Japan', 'Vietnam'])
    render_by_plot(gdpinfo, ['Vietnam', 'Thailand', 'Malaysia', 'Philippines', 'Singapore', 'Lao PDR'])

test_render_xy_plot()