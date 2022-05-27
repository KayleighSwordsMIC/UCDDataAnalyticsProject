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


#import data from github csv to dataframe

gitdata = pd.read_csv(r"https://raw.githubusercontent.com/KayleighSwordsMIC/"\
                      r"UCDDataAnalyticsProject/main/Data/World-Deaths.csv")

#check for missing values
#print(data.isna().any())  

#replace missing values with n/a
gitdata.fillna("N/A", inplace=True)

#check again to make sure all missing values are gone
#print(data.isna().any())

#drop duplicates for country and year matches
unique_data = gitdata.drop_duplicates(subset=["Entity", "Year"])





#set index
data_index = unique_data.set_index(["Entity", "Year"])

#sort values by index
data_srt = data_index.sort_index()


#slice data for Ireland
ireland = data_srt.loc["IRL":"IRL"]

