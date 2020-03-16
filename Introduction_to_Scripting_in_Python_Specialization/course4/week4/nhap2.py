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
    # co o trong plot nhung ko co o trong convert, co nghia la convert file loi

    list_map = dict()
    set_2 = set()
    map_code = build_country_code_converter(codeinfo)
    print(map_code)
    upper_map_code = {}
    for k,v in map_code.items():
        upper_map_code[k.upper()] = v
    # print(upper_map_code)

    for country_code in plot_countries.keys():
        for data_code in gdp_countries.keys():
          if country_code in upper_map_code:
            if upper_map_code[country_code].upper() == data_code.upper():
                list_map[country_code] = data_code
          elif country_code.upper() in upper_map_code:
                if upper_map_code[country_code.upper()] == data_code.upper():
                    list_map[country_code] = data_code
        if country_code not in list_map:
            set_2.add(country_code)
    # print(list_map, set_2)
    return list_map,set_2


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
        csv_test = csv.DictReader(csv_test, delimiter=gdpinfo['separator'], quotechar=gdpinfo['quote'])
        for row in csv_test:
            rowid = row[gdpinfo['country_code']]
            gdp_countries[rowid] = row
    # print(gdp_countries)
    list_map_plot_to_gdp = reconcile_countries_by_code(codeinfo, plot_countries, gdp_countries)
    print(list_map_plot_to_gdp)
    list_country_data = list_map_plot_to_gdp[0]
    set_country_not_data = list_map_plot_to_gdp[1]
    list_plot_code_gdp_by_year = dict()
    set_contry_code2= set()
    for country_code, data_code in list_country_data.items():
        try:
          list_plot_code_gdp_by_year[country_code] = math.log10(float(gdp_countries[data_code][year]))
        except:
          set_contry_code2.add(country_code)
    return list_plot_code_gdp_by_year, set_country_not_data, set_contry_code2
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
        "data_codes": "ISO3166-1-Alpha-3"}



    pygal_countries = pygal.maps.world.COUNTRIES
    print(reconcile_countries_by_code(codeinfo, pygal_countries, gdpinfo))
    final_tuple = build_map_dict_by_code(gdpinfo, codeinfo, pygal_countries, '2012')
    print(final_tuple[1])
    print(final_tuple[2])

    print(pygal_countries)

    print(len(final_tuple[0])+ len(final_tuple[1])+ len(final_tuple[2]))





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




# test_render_world_map()




# print(build_map_dict_by_code({'gdpfile': 'gdptable3.csv', 'separator': ';', 'quote': "'", 'min_year': 20010, 'max_year': 20017, 'country_name': 'ID', 'country_code': 'CC'},
#  {'codefile': 'code1.csv', 'separator': ',', 'quote': "'", 'plot_codes': 'Code4', 'data_codes': 'Code3'}, {'C1': 'c1', 'C2': 'c2', 'C3': 'c3', 'C4': 'c4', 'C5': 'c5'}, '20012'))
# #   expected ({'C1': 9.778151250383642, 'C2': 9.778151250383642, 'C3': 9.99999999995657, 'C4': 9.99999999995657}, {'C5'}, set()) 
# # but received (Exception: KeyError) "'CC'" at line 98, in build_map_dict_by_code



# print(reconcile_countries_by_code({'codefile': 'code4.csv', 'separator': ',', 'quote': '"', 'plot_codes': 'ISO3166-1-Alpha-2', 'data_codes': 'ISO3166-1-Alpha-3'}, {'pr': 'Puerto Rico', 'no': 'Norway', 'us': 'United States'}, {'USA': {'Country Name': 'United States', 'Country Code': 'USA'}, 'NOR': {'Country Name': 'Norway', 'Country Code': 'NOR'}, 'PRI': {'Country Name': 'Puerto Rico', 'Country Code': 'PRI'}}))
 # expected ({'pr': 'PRI', 'no': 'NOR', 'us': 'USA'}
#   , set()) but received ({}, {'us', 'no', 'pr'}) (Exception: Invalid Keys) Expected dictionary {'pr': 'PRI', 'no': 'NOR', 'us': 'USA'} 
# has a different number of keys than received dictionary {}