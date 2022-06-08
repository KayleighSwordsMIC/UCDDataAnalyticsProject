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

"""

import the data, replace missing values and then replace the Code column with 
unique code values
    
"""

#import data from github csv to dataframe

gitdata = pd.read_csv(r"https://raw.githubusercontent.com/KayleighSwordsMIC/"\
                      r"UCDDataAnalyticsProject/main/Data/World-Deaths.csv")

#read from local csv 
#downloaded_data = pd.read_csv(r"C:\Users\kayleigh.swords\OneDrive - "\
    #r"Mary Immaculate College\1 Personal\Cert in Introductory data Analytics "\
        #"(with Python)\Project Folder\GitHub Upload\Data\World-Deaths.csv")    
    
    
#check for missing values
#print(data.isna().any())  

#replace missing values with n/a
gitdata.fillna("N/A", inplace=True)

#check again to make sure all missing values are gone
#print(data.isna().any())


#drop duplicates for country and year matches
unique_data = gitdata.drop_duplicates(subset=["Entity", "Year"])

#list of columns
list(unique_data)

#rename columns to make things simpler
unique_data.columns = ["Entity", "Code", "Year", "Executions", \
                       "Meningitis", "Neoplasms", "Fire", \
              "Malaria", "Drowning", "Interpersonal violence", "HIV/AIDS", "Drugs", \
                "Tuberculosis", "Road injuries", "Maternal disorders", \
                "Lower respiratory infections", "Neonatal Disorders", \
                "Alcohol", "Exposure To Forces of nature", \
                "Diarrheal diseases", "Environmental heat and cold exposure", \
                "Nutritional deficiencies", "Self harm", \
                "Conflict & terrorist attacks", "Diabetes mellitus", \
                "Poisonings", "Protein-energy malnutrition", "Terrorism", \
                "Cardiovascular diseases", "Chronic kidney disease", \
                "Chronic respiratory diseases", "Cirrhosis & other liver disease", \
                "Digestive diseases", "Acute hepatitis", "Alzheimers & dementia",\
                "Parkinsons"]
    
#create list of countries as "keys"
list_of_keys = unique_data["Entity"].to_list()
    
#characters to be removed
extra_chars = "()"
    
#use join() to remove the extra characters
new_list_of_keys = [''.join(x for x in string if not x in extra_chars) \
                        for string in list_of_keys]

#create sublist to hold each key
indiv_list_of_keys = []
    
#create holding variable for values
temp_value = ""
    
#create list of values
list_of_values = []


#make new list of codes
for key in new_list_of_keys:
    temp_value = key.upper()
    if ("-" in temp_value) and (" " not in temp_value):
        list_of_values.append(temp_value[:10])
    
    elif (" " not in temp_value) and (len(temp_value) > 7):
        list_of_values.append(temp_value[:])
    
    
    elif " " not in temp_value:
        list_of_values.append(temp_value[:6])
        
            
    elif " " in temp_value:
        temp_value = temp_value.split(" ")
        if len(temp_value) < 3:
            list_of_values.append(temp_value[0][:5] + " " + temp_value[1][:6] \
                                  +  " ")
        elif len(temp_value) == 3:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:5] \
                                  + " " + temp_value[2][:4])
        
        elif len(temp_value) == 4:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                  + " " + temp_value[2][:4] + " " + temp_value[3][:4])
                
        elif len(temp_value) == 5:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                  + " " + temp_value[2][:4] + " " + \
                                      temp_value[3][:4] + " " + temp_value[4][:4])
        elif len(temp_value) == 6:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                  + " " + temp_value[2][:4] + " " + \
                                      temp_value[3][:4] + " " + temp_value[4][:4]\
                                          + " " + temp_value[5][:4])
        
        elif len(temp_value) == 7:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                  + " " + temp_value[2][:4] + " " + \
                                      temp_value[3][:4] + " " + temp_value[4][:4]\
                                          + " " + temp_value[5][:4] + " " + \
                                              temp_value[6][:4])
        
        elif len(temp_value) == 8:
            list_of_values.append(temp_value[0][:4] + " " + temp_value[1][:4] \
                                  + " " + temp_value[2][:4] + " " + \
                                      temp_value[3][:4] + " " + temp_value[4][:4]\
                                         + " " + temp_value[5][:4] + " " + \
                                             temp_value[6][:4] +  " " + \
                                                 temp_value[7][:4])
        else:
            print("can't add value")
  
        
    

    
#convert entity column to a list
entity_column = unique_data["Entity"].to_list()

#make dataframe of entity column and list of values
new_df = pd.DataFrame()

#add the columns
new_df["Entity"] = entity_column
new_df["Code"] = list_of_values

#replace the code column in unique_data
unique_data.loc[:, ["Code"]] = new_df[["Code"]]



"""

continue on with rest of program - this text is added to make the program \
    easier to read by breaking it up.
    
    Next step is to slice the data to look specifically at Ireland

"""



#set index
data_index = unique_data.set_index(["Entity", "Year"])

#sort values by index
data_srt = data_index.sort_index()


#slice data for Ireland
ireland = data_srt.loc["Ireland":"Ireland"]


"""
Create a function - type of death to return the year and its max value

"""
    
def max_deaths():
   #specify the dataframe this is working on 
    df = ireland
    
    #replace missing N/A values with 0
    df = df.replace("N/A", 0)
    
    
    print("Hello! I hear you are interested in data on the causes of deaths in "\
          "Ireland. \n"
        "Please select the category of death you are interested in from the "
            "following list: \n")
    print(", \n".join([str(death) for death in df.columns[1:]]))
        
    #check if death is in columns
    death = input("Please type in the death you are interested in data on. \n"
                  "Please make sure it matches the list above exactly: \n ").lower()
    
    #change columns to all lower case for comparison
    df.columns = df.columns.str.lower()
    
    
    if death in df.columns:
        #get max no of deaths
        max_value = df[death].max()
        
        
        #get year - index returns as tuple, convert to list containing just year
        max_year_tuple = df[death].idxmax()
        max_year_list = list(max_year_tuple)
        max_year = max_year_list.pop(1)
        
        
        print("\n You selected " + str(death).upper() + ". \n The highest number of "\
              "deaths which have been recorded in Ireland for this category is " + \
                  str(int(max_value)) + ".\n This occured in " + str(max_year) + ".")
        
    elif death not in df.columns:
        whoops = input("I don't think you typed that in correctly. \n" \
              "Would you like to try again? \n" \
                  "Please type 'Yes' or 'No' \n").lower()
        if whoops == "yes":
            max_deaths()
        elif whoops == "no":
            print("Okay, thanks, have a nice day!")
        else:
            whoops_2 = input("Please type in 'Yes' or 'No' \n").lower()
            if whoops_2 == "yes":
                max_deaths()
            else:
                print("Okay, thanks, have a nice day!")
    
    else:
        print("Have a nice day!")
             
    
    
max_deaths()

"""

continue on with rest of program - this text is added to make the program \
    easier to read by breaking it up.
    
    Next step is to slice the data to look specifically at Ireland and then \
        do the same with UK data. Then merge the data and look at summary \
            statistics for both

"""


#set index
data_index = unique_data.set_index(["Entity", "Code"])

#sort values by index
data_srt = data_index.sort_index()

#change N/A values to 0
data_srt = data_srt.replace("N/A", 0)

#remove > sign from some values as its causing issues
data_srt = data_srt.replace(">1", 1)
data_srt = data_srt.replace(">1000", 1000)

#change execution column to int
data_srt["Executions"] = pd.to_numeric(data_srt["Executions"])


#slice data for Ireland
ireland = data_srt.loc["Ireland":"Ireland"]


#slice data for UK
uk = data_srt.loc["United Kingdom":"United Kingdom"]

#merge dataframes Ireland and UK
i_uk = ireland.merge(uk, on = "Year", suffixes = ("_I", "_UK"))

#use melt to reorganise data
i_uk_melt = i_uk.melt(id_vars=["Year"], value_vars = i_uk.columns, \
                      var_name = "Type of death", \
                          value_name = "No of deaths").sort_values(by = \
                          ["Year", "Type of death", "No of deaths"])

#use groupby for summary stats
#year where minimum deaths and maximum deaths of each type occured
min_max_year_i_uk = i_uk_melt.groupby("Type of death")["Year"].agg([min, max])
#value for min and max deaths
min_max_val_i_uk = i_uk_melt.groupby("Type of death")["No of deaths"].agg([min, max])

#use pivot table to get mean of each death in each country
pivot_i_uk = i_uk_melt.pivot_table(values = "No of deaths", index = "Year", \
                                   columns = "Type of death").mean()

#get sum of deaths with pivot and swap columns and rows data
pivot_sum = i_uk_melt.pivot_table(values = "No of deaths", index = "Year", \
                                   columns = "Type of death", aggfunc = "sum", \
                                   margins = True, margins_name = "Total").T

