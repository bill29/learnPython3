"""
Project for Week 4 of "Python Data Analysis".
Processing CSV files with baseball stastics.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

##
## Provided code from Week 3 Project
##

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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            table.append(row)
    return table
#stats_list = read_csv_as_list_dict('batting1.csv', ",", '"')
#print(stats_list)

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
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table
#stats_dict = read_csv_as_nested_dict('Batting_2016.csv',  ",", '"')
#print(stats_dict)

##
## Provided formulas for common batting statistics
##

# Typical cutoff used for official statistics
MINIMUM_AB = 500

def batting_average(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the batting average as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return hits / at_bats
    else:
        return 0

def onbase_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the on-base percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    at_bats = float(batting_stats[info["atbats"]])
    walks = float(batting_stats[info["walks"]])
    if at_bats >= MINIMUM_AB:
        return (hits + walks) / (at_bats + walks)
    else:
        return 0

def slugging_percentage(info, batting_stats):
    """
    Inputs:
      batting_stats - dictionary of batting statistics (values are strings)
    Output:
      Returns the slugging percentage as a float
    """
    hits = float(batting_stats[info["hits"]])
    doubles = float(batting_stats[info["doubles"]])
    triples = float(batting_stats[info["triples"]])
    home_runs = float(batting_stats[info["homeruns"]])
    singles = hits - doubles - triples - home_runs
    at_bats = float(batting_stats[info["atbats"]])
    if at_bats >= MINIMUM_AB:
        return (singles + 2 * doubles + 3 * triples + 4 * home_runs) / at_bats
    else:
        return 0


##
## Part 1: Functions to compute top batting statistics by year
##

def filter_by_year(statistics, year, yearid):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      year       - Year to filter by
      yearid     - Year ID field in statistics
    Outputs:
      Returns a list of batting statistics dictionaries that
      are from the input year.
    """
    new_list = []
    
    for row in statistics:
        if int(row[yearid]) == year:
            new_list.append(row)
    return new_list

def top_player_ids(info, statistics, formula, numplayers):
    """
    Inputs:
      info       - Baseball data information dictionary
      statistics - List of batting statistics dictionaries
      formula    - function that takes an info dictionary and a
                   batting statistics dictionary as input and
                   computes a compound statistic
      numplayers - Number of top players to return
    Outputs:
      Returns a list of tuples, player ID and compound statistic
      computed by formula, of the top numplayers players sorted in
      decreasing order of the computed statistic.
    """
    # initiate a new list
    new_list = []
    final_list = []
    for row in statistics:
        # create the parameters for the tuple
        player_id = row[info['playerid']]
        comp_stat = formula(info, row)
        # create the tuple based on the previous variables
        current_tuple = tuple((player_id, comp_stat))
        # add each tuple to the new list
        new_list.append(current_tuple)
    
    # sort the list by the second element in each tuple
    new_list.sort(key = lambda pair: pair[1], reverse=True)
    # limit the amount of items in the list to numplayers #
    for tuple_idx in new_list:
        if numplayers > 0:
            final_list.append(tuple(tuple_idx))
            numplayers -= 1
        else: break
    return final_list
'''

'''

def lookup_player_names(info, top_ids_and_stats):
    """
    Inputs:
      info              - Baseball data information dictionary
      top_ids_and_stats - list of tuples containing player IDs and
                          computed statistics
    Outputs:
      List of strings of the form "x.xxx --- FirstName LastName",
      where "x.xxx" is a string conversion of the float stat in
      the input and "FirstName LastName" is the name of the player
      corresponding to the player ID in the input.
    """
    # initiate a new list
    new_list = []
    # make a reference to the master file as a nested dictionary
    info_dict = read_csv_as_nested_dict(info['masterfile'], info['playerid'], info['separator'], info['quote'])
    # add each string as an item in the new list
    for idx in top_ids_and_stats:
        formatted_string = format(idx[1], '.3f') + " --- {0} {1}".format(info_dict[idx[0]][info['firstname']],
                                                                         info_dict[idx[0]][info['lastname']])
        new_list.append(formatted_string)
    return new_list



def compute_top_stats_year(info, formula, numplayers, year):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
      year        - Year to filter by
    Outputs:
      Returns a list of strings for the top numplayers in the given year
      according to the given formula.
    """
    
    stats_list = read_csv_as_list_dict(info['battingfile'],
                                       info['separator'],
                                       info['quote']
                                       )
    # filter by year using filter_by_year()
    filtered_by_year = filter_by_year(stats_list,
                                   year,
                                   info['yearid'])
    # return list of tuples of top players using top_player_ids()
    top_players = top_player_ids(info, filtered_by_year, formula, numplayers)
    # return list of strings for top numplayers using
    return lookup_player_names(info, top_players)


##
## Part 2: Functions to compute top batting statistics by career
##

def aggregate_by_player_id(statistics, playerid, fields):
    """
    Inputs:
      statistics - List of batting statistics dictionaries
      playerid   - Player ID field name
      fields     - List of fields to aggregate
    Output:
      Returns a nested dictionary whose keys are player IDs and whose values
      are dictionaries of aggregated stats.  Only the fields from the fields
      input will be aggregated in the aggregated stats dictionaries.
    """
    # initialize an empty dict
    final_dict = {}
    stats_dict = {}        
        
    for row in statistics:
        
        #1 the first time you see a player, create a new entry in final_dict
        if row[playerid] not in final_dict:
            # add the playerid to the nested dictionary
            stats_dict[playerid] = row[playerid]
            # for each stat to aggregate in fields, add the stat to the nested dictionary
            for field in fields:
                stats_dict[field] = int(row[field])
            # remember to add the dict in 'dict(stats_dict)' so that
            # the stats_dict fields will not get overwritten
            final_dict[row[playerid]] = dict(stats_dict)
        #2 if the player is already in final_dict
        else:
            # for each stat to aggregate in fields, update the stat
            for field in fields:
                final_dict[row[playerid]][field] += int(row[field])
            
    return final_dict
        
        
    example_output = {'playerid1': {'stat1': 'aggregated_number1', 'stat2': 'aggregated_number2'},
                      'playerid2': {'stat1': 'aggregated_number1', 'stat2': 'aggregated_number2'}}


def compute_top_stats_career(info, formula, numplayers):
    """
    Inputs:
      info        - Baseball data information dictionary
      formula     - function that takes an info dictionary and a
                    batting statistics dictionary as input and
                    computes a compound statistic
      numplayers  - Number of top players to return
    """
    stats = []
    # aggregate the stats for each player so that you are operating on career statistics
    aggregated_stats = aggregate_by_player_id(read_csv_as_list_dict(info['battingfile'], info['separator'], info['quote']),
                                              info['playerid'],
                                              info['battingfields'])
    
    # add each dictionary row in agreggated_stats to the stats list
    # to have an easily usable stats list to pass to other functions
    for value in aggregated_stats.values():
        stats.append(value)
    # use lookup_player_names and top_player_ids to return top players
    return lookup_player_names(info, top_player_ids(info, stats, formula, numplayers))


def test_baseball_statistics():
    """
    Simple testing code.
    """

    #
    # Dictionary containing information needed to access baseball statistics
    # This information is all tied to the format and contents of the CSV files
    #
    baseballdatainfo = {"masterfile": "Master_2016.csv",   # Name of Master CSV file
                        "battingfile": "Batting_2016.csv", # Name of Batting CSV file
                        "separator": ",",                  # Separator character in CSV files
                        "quote": '"',                      # Quote character in CSV files
                        "playerid": "playerID",            # Player ID field name
                        "firstname": "nameFirst",          # First name field name
                        "lastname": "nameLast",            # Last name field name
                        "yearid": "yearID",                # Year field name
                        "atbats": "AB",                    # At bats field name
                        "hits": "H",                       # Hits field name
                        "doubles": "2B",                   # Doubles field name
                        "triples": "3B",                   # Triples field name
                        "homeruns": "HR",                  # Home runs field name
                        "walks": "BB",                     # Walks field name
                        "battingfields": ["AB", "H", "2B", "3B", "HR", "BB"]}

    print("Top 5 batting averages in 1923")
    top_batting_average_1923 = compute_top_stats_year(baseballdatainfo, batting_average, 5, 1923)
    for player in top_batting_average_1923:
        print(player)
    print("")

    print("Top 10 batting averages in 2010")
    top_batting_average_2010 = compute_top_stats_year(baseballdatainfo, batting_average, 10, 2010)
    for player in top_batting_average_2010:
        print(player)
    print("")

    print("Top 10 on-base percentage in 2010")
    top_onbase_2010 = compute_top_stats_year(baseballdatainfo, onbase_percentage, 10, 2010)
    for player in top_onbase_2010:
        print(player)
    print("")

    print("Top 10 slugging percentage in 2010")
    top_slugging_2010 = compute_top_stats_year(baseballdatainfo, slugging_percentage, 10, 2010)
    for player in top_slugging_2010:
        print(player)
    print("")

    # You can also use lambdas for the formula
    #  This one computes onbase plus slugging percentage
    print("Top 10 OPS in 2010")
    top_ops_2010 = compute_top_stats_year(baseballdatainfo,
                                          lambda info, stats: (onbase_percentage(info, stats) +
                                                               slugging_percentage(info, stats)),
                                          10, 2010)
    for player in top_ops_2010:
        print(player)
    print("")

    print("Top 20 career batting averages")
    top_batting_average_career = compute_top_stats_career(baseballdatainfo, batting_average, 20)
    for player in top_batting_average_career:
        print(player)
    print("")


# Make sure the following call to test_baseball_statistics is
# commented out when submitting to OwlTest/CourseraTest.

#test_baseball_statistics()
