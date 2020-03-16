"""
Project for Week 4 of "Python Data Visualization".
Unify data via common country codes.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    # print(codeinfo['codefile'], codeinfo['separator'], codeinfo['plot_codes'], codeinfo['data_codes'])
    dict_country_code = dict()
    with open(codeinfo['codefile'], "rt", newline ='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter = codeinfo['separator'], quotechar = codeinfo['quote'])
        for row in csvreader:
            row_id = row[codeinfo['plot_codes']]
            row_value = row[codeinfo['data_codes']]
            dict_country_code[row_id] = row_value
    return dict_country_code

# print(build_country_code_converter(codeinfo))

def reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries):
    """
    Inputs:
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country codes used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country codes from
      gdp_countries.  The set contains the country codes from
      plot_countries that did not have a country with a corresponding
      code in gdp_countries.

      Note that all codes should be compared in a case-insensitive
      way.  However, the returned dictionary and set should include
      the codes with the exact same case as they have in
      plot_countries and gdp_countries.
    """
    list_map = dict()
    set_2 = set()
    map_code = build_country_code_converter(codeinfo)
    copy_code_converter = dict()
    #coppy standar converter
    for code1, code2 in map_code.items():
        copy_code_converter[code1.upper()] = code2 
    

    for country_code in plot_countries.keys():
        if country_code.upper() in copy_code_converter.keys():
            if copy_code_converter[country_code.upper()] in gdp_countries.keys():
                list_map[country_code] = copy_code_converter[country_code.upper()]
            else:
                set_2.add(country_code)
    return list_map, set_2


def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    gdp_countries = dict()
    with open(gdpinfo['gdpfile'], 'rt', newline='') as csv_test:
        csv_test = csv.DictReader(csv_test, delimiter=',', quotechar='"')
        for row in csv_test:
            rowid = row[gdpinfo['country_code']]
            gdp_countries[rowid] = row

    list_map_plot_to_gdp = reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries)

    list_country_data = list_map_plot_to_gdp[0]
    set_country_not_data = list_map_plot_to_gdp[1]
    list_plot_code_gdp_by_year = dict()
    set_contry_code2= set()
    for code_plot,code_data in list_country_data.items():
        try:
          list_plot_code_gdp_by_year[code_plot] = math.log10(float(gdp_countries[code_data][year])) 
        except:
          set_contry_code2.add(code_plot)
    return list_plot_code_gdp_by_year, set_country_not_data, set_contry_code2

#test 1
# gdp_countries = dict()
# with open('gdptable1.csv', 'rt', newline='') as csv_test:
#     csv_test = csv.DictReader(csv_test, delimiter=',', quotechar='"')
#     for row in csv_test:
#         rowid = row[gdpinfo['country_code']]
#         gdp_countries[rowid] = row

# print(gdp_countries)
# reconcile_countries_by_code(codeinfo, pygal_countries, gdp_countries)
# tuple_reconcile_countries = reconcile_countries_by_code(codeinfo, pygal_countries, gdp_countries)
# print(tuple_reconcile_countries[0])
# print(tuple_reconcile_countries[1])


pygal_countries = pygal.maps.world.COUNTRIES
build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '2010')

print('List country GDP in ')
print(build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '2010')[0])
print('List country miss data in World Data')
print(build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '2010')[1])
print('List country miss data in ')
print(build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '2010')[2])
















def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    return


def test_render_world_map():
    """
    Test the project code for several years
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

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }


    print(build_country_code_converter(gdpinfo))
    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # # 1980
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # # 2000
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # # 2010
    # render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map

