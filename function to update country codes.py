# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:46:26 2022

@author: Kayleigh.Swords
"""
# import required packages
import pandas as pd
import numpy as np
import requests
from io import StringIO

#import data from CSV to dataframe

data = pd.read_csv(r"C:\Users\kayleigh.swords\OneDrive - Mary Immaculate College\1 Personal\Cert in Introductory data Analytics (with Python)\Project Folder\GitHub Upload\Data\World-Deaths.csv")

#check for missing values
#print(data.isna().any())  

#replace missing values with n/a
data.fillna("n/a", inplace=True)

#check again to make sure all missing values are gone
#print(data.isna().any())

#set country as index
data_index = data.set_index("Entity")

#drop duplicates for country and year matches
unique_data = data.drop_duplicates(subset=["Entity", "Year"])

#sort values by index
data_srt = unique_data.set_index("Entity").sort_index()

#function to replace n/a country codes
def country_codes_replace(country, country_code):
    #data_srt.loc[(data_srt["Code"] == "n/a") & (data_srt["Entity"] == country), "Code"] = country_code
    
    
    
#call function to replace n/a country codes
country_codes_replace("Africa", "AFR")
country_codes_replace("America", "USA")

print(data_srt[["Entity", "Code"]])

#write to csv to check data
data_srt.to_csv(r"C:\Users\kayleigh.swords\OneDrive - Mary Immaculate College\1 Personal\Cert in Introductory data Analytics (with Python)\Project Folder\function-checker.csv")
