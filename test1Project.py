# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:46:26 2022

@author: Kayleigh.Swords
"""

# import required packages, pandas, matplotlib, seaborn, numpy and requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from urllib.request import urlretrieve , urlopen, Request

#website hosting data
url = "https://www.kaggle.com/datasets/ivanchvez/causes-of-death-our-world-in"\
   "-data?select=20220327+annual-number-of-deaths-by-cause.csv"

#import data from CSV to dataframe - see if can change to webpage later - not 
#working due to errors at moment
data = pd.read_csv(r"C:\Users\kayleigh.swords\OneDrive - Mary Immaculate "\
r"College\1 Personal\Cert in Introductory data Analytics "\
r"(with Python)\Project Folder\World-Deaths.csv")

#check for missing values
#print(data.isna().any())  

#replace missing values with n/a
data.fillna("n/a", inplace=True)

#check again to make sure all missing values are gone
#print(data.isna().any())

#set country code as index
data_index = data.set_index("Entity")

#drop duplicates for country and year matches
unique_data = data.drop_duplicates(subset=["Entity", "Year"])

#sort values by index
data_srt = unique_data.set_index("Code").sort_index()

#slice data for Ireland
ireland = data_srt.loc["IRL":"IRL"]

