

# these should be the options for the dropdownmenu location
boroughs = [
    'The Bronx',
    'Brooklyn',
    'Manhattan',
    'Queens',
    'Staten Island'
]


Interest = [
    'Food',
    'Art & Music'
    'Sightseeing',
    'Shopping',
    'Sports',
    'Nightlife'
]

age_range = {
    'a': '18-30',
    'b': '31-50',
    'c': '51-120'
}

import json
import wget
import os
import pandas as pd


if os.path.exists('newyork_data.json'):
    os.remove('newyork_data.json')
wget.download('https://cocl.us/new_york_dataset/newyork_data.json')

with open('newyork_data.json') as json_data:
    newyork_data = json.load(json_data)

# define the dataframe columns
column_names = ['Borough', 'Neighborhood', 'Latitude', 'Longitude']

# instantiate the dataframe
neighborhoods = pd.DataFrame(columns=column_names)
neighborhoods_data = newyork_data['features']

for data in neighborhoods_data:
    borough = data['properties']['borough']
    neighborhood_name = data['properties']['name']

    #neighborhood_latlon = data['geometry']['coordinates']
    #neighborhood_lat = neighborhood_latlon[1]
    #neighborhood_lon = neighborhood_latlon[0]

    neighborhoods = neighborhoods.append({'Borough': borough,
                                          'Neighborhood': neighborhood_name}, ignore_index=True)
                                          #'Latitude': neighborhood_lat, 'Longitude': neighborhood_lon},



print('The dataframe has {} boroughs and {} neighborhoods.'.format(
        len(neighborhoods['Borough'].unique()),
        neighborhoods.shape[0]
    )
)

a_list = ['Astoria','Williamsburg','East Village','Financial District','Brooklyn Heights','Dumbo','Nolita','Bushwick','Crown Heights','Murray Hill']
b_list = ['Kensington','Sunnyside','Windsor Terrace','Central Harlem','East Harlem','Greenpoint','Prospect Heights', 'Clinton Hill','Long Island City']
c_list = ['Upper East Side',"Hell's kitchen",'Murray Hill','Park Slope','Battery Park City']

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Astoria', 'age_category'] = 'a'

print(neighborhoods['Neighborhood'])

## TOP 20 Neighborhoods Manhattan
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Midtown', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Midtown', 'interests'] = 'Food, Sightseeing, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Soho', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Soho', 'interests'] = 'Art & Music, Shopping, Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Chelsea', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Chelsea', 'interests'] = 'Art & Music, Shopping, Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Upper East Side', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Upper East Side', 'interests'] = 'Shopping, Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'East Village', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'East Village', 'interests'] = 'Art & Music, Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Lower East Side', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Lower East Side', 'interests'] = 'Art & Music, Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tribeca', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tribeca', 'interests'] = 'Food, Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Greenwich Village', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Greenwich Village', 'interests'] = 'Art & Music, Sightseeing, Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Harlem', 'age_category'] = 'b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Harlem', 'interests'] = 'Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Flatiron', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Flatiron', 'interests'] = 'Sightseeing, Food,'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Chinatown', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Chinatown', 'interests'] = 'Food, Nightlife, Sightseeing, Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Upper West Side', 'age_category'] = 'c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Upper West Side', 'interests'] = 'Sightseeing, Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'West Village', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'West Village', 'interests'] = 'Food, Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Gramercy', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Midtown', 'interests'] = 'Sightseeing, Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Nolita', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Nolita', 'interests'] = 'Shopping, Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Battery Park City', 'age_category'] = 'c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Battery Park City', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Noho', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Noho', 'interests'] = 'Food'


# Top 10 Brookyln

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Park Slope', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Park Slope', 'interests'] = 'Food, Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Carroll Gardens', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Carroll Gardens', 'interests'] = 'Food, Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Cobble Hill', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Cobble Hill', 'interests'] = 'Sightseeing, Food, Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Greenpoint', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Greenpoint', 'interests'] = 'Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Fort Greene', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Fort Greene', 'interests'] = 'Art & Music, Food, Shopping, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Brooklyn Heights', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Brookyln Heights', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Dumbo', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Dumbo', 'interests'] = 'Sightseeing, Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Williamsburg', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Williamsburg', 'interests'] = 'Nightlife, Food, Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Bushwick', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Bushwick', 'interests'] = 'Art & Music, Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Red Hook', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Red Hook', 'interests'] = 'Art & Music, Food, Nightlife'


# Top 10 Bronx

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Concourse', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Concourse', 'interests'] = 'Food, Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Fordham', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Fordham', 'interests'] = 'Sightseeing, Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Kingsbridge', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Kingsbridge', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Mott Haven', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Mott Haven', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Riverdale', 'age_category'] = 'c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Riverdale', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Woodlawn', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Woodlawn', 'interests'] = 'Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'South Bronx', 'age_category'] = 'b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'South Bronx', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'City Island', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'City Island', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Belmont', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Belmont', 'interests'] = 'Food'


# Top 8 Staten Island

neighborhoods.loc[neighborhoods['Neighborhood'] == 'West Brighton', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'West Brighton', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'St. George', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'St. George', 'interests'] = 'Food, Sightseeing, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'New Dorp', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'New Dorp', 'interests'] = 'Food, Sightseeing, Nightlife, Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Great Kills', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Great Kills', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Oakwood', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Oakwood', 'interests'] = 'Shopping'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Todt Hill', 'age_category'] = 'c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Todt Hill', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tompkinsville', 'age_category'] = 'b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tompkinsville', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Randall Manor', 'age_category'] = 'c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Randall Manor', 'interests'] = 'Sightseeing'

# Top 9 Queens

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Long Island City', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Long Island City', 'interests'] = 'Sightseeing, Nightlife, Food, Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Astoria', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Astoria', 'interests'] = 'Sightseeing, Art & Music, Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Jackson Heights', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Jackson Heights', 'interests'] = 'Food, Nightlife'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Forest Hills', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Forest Hills', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Corona', 'age_category'] = 'a,b'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Corona', 'interests'] = 'Art & Music'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Rockaway Beach', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Rockaway Beach', 'interests'] = 'Shopping, Art & Music, Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Flushing', 'age_category'] = 'a'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Flushing', 'interests'] = 'Food'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Jamaica Hills', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Jamaica Hills', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tompkinsville', 'age_category'] = 'b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Tompkinsville', 'interests'] = 'Sightseeing'

neighborhoods.loc[neighborhoods['Neighborhood'] == 'Sunnyside', 'age_category'] = 'a,b,c'
neighborhoods.loc[neighborhoods['Neighborhood'] == 'Sunnyside', 'interests'] = 'Sightseeing, Food, Nightlife'



























