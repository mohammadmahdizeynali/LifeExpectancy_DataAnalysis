# in the name of ALLAH

# import library 

import pandas as pd
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2

# we need 2 function for this task

def get_continent_name(continent_code: str) -> str:
    continent_dict = {
        "NA": "North America",
        "SA": "South America",
        "AS": "Asia",
        "AF": "Africa",
        "OC": "Oceania",
        "EU": "Europe",
        "AQ" : "Antarctica"
    }
    return continent_dict[continent_code]



def get_continent(country_name):
    try:
        country_alpha2 = country_name_to_country_alpha2(country_name)
        continent_code = country_alpha2_to_continent_code(country_alpha2)
        return get_continent_name(continent_code)
    except KeyError:
        return "Not found"

# import df

df = pd.read_csv("life_expectancy_primary_data.csv")

# insert new feature as continent

df.insert(1, "Continent", "")
df["Continent"] = df["Country"].apply(get_continent)

# save df as csv
df.to_csv("life_expectancy_data.csv", index = False)

print("job is finished!")

