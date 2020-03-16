"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal
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
def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    set_countries = set()
    list_map_countries_by_name = dict()
    for country_code,country_name in plot_countries.items():
        if country_name in gdp_countries:
            list_map_countries_by_name[country_code]=country_name
        else:
            set_countries.add(country_code)
    return list_map_countries_by_name, set_countries

def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    dict_country_code_by_year = dict()
    countries_code1 = set()
    countries_code2 = set()
    gdp_countries = read_csv_as_nested_dict(gdpinfo['gdpfile'],gdpinfo['country_name'], gdpinfo['separator'], gdpinfo['quote'])

    for country_code, country_name in plot_countries.items():
      if country_name in gdp_countries:
        try:
          dict_country_code_by_year[country_code] = math.log10((float(gdp_countries[country_name][year])))
        except:
          countries_code2.add(country_code)
      else:
        countries_code1.add(country_code)
    return dict_country_code_by_year, countries_code1, countries_code2


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    worldmap_chart = pygal.maps.world.World()
    worldmap_chart.title = 'GDP of the World in ' + str(year)

    gdp_datas = build_map_dict_by_name(gdpinfo, plot_countries, year)
    worldmap_chart.add('GDP For ' + year, gdp_datas[0])
    worldmap_chart.add('Missing Data ', gdp_datas[1])
    worldmap_chart.add('No GDP Data', gdp_datas[2])
    
    help(worldmap_chart)

    # worldmap_chart.render_in_browser()
    # worldmap_chart.render()


def test_render_world_map():
    """
    Test the project code for several years.
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

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES
    # print(pygal_countries)
    # 1960
    # render_world_map(gdpinfo, pygal_countries, "2015", "isp_gdp_world_name_1960.svg")

    # # 1980
    # render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # # 2000
    # render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# # Make sure the following call to test_render_world_map is commented
# # out when submitting to OwlTest/CourseraTest.

# test_render_world_map()