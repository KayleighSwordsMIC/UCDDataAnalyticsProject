# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:52:20 2022

@author: Kayleigh.Swords
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May 12 19:46:26 2022

@author: Kayleigh.Swords
"""

# import required packages, pandas, matplotlib, seaborn, numpy and requests
import pandas as pd


"""

import the data, replace missing values and then replace the Code column with 
unique code values
    
"""

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
    
def max_deaths():
        
   #specify the dataframe this is working on 
    df = ireland
    
    #replace missing N/A values with 0
    df = df.replace("N/A", 0)
    
    #thank you statement
    thank_you = "Okay, thanks have a nice day!"
    
    #opening statement    
    statement = "Hello! I hear you are interested in data on the causes of "\
        "deaths in Ireland. \n"
    
    #selection statement
    selection = "Please select the category of death you are interested in from "\
        "the following list: \n"
        
    #list of options
    list_to_print = (", \n".join([str(death) for death in df.columns[1:]]))
        
    #check if death is in columns
    entry = "Please type in the death you are interested in data on. \n"\
                  "Please make sure it matches the list above exactly: \n "
    
    #change columns to all lower case for comparison
    df.columns = df.columns.str.lower()
    
    #list of possible yes answers
    yes = ["yes", "y", "ya", "yeah", "okay", "ok"]
    
    #list of possible no answers
    no = ["no", "n", "no thanks", "no thank you", "no way", "quit"]
    
    #question for user to respond to
    try_again_q = "Would you like to try that again? "
    
    
    
    #function to try again
    def try_again():
        try_again_a = input(try_again_q).lower()
        if try_again_a in yes:
            call_deaths()            
        elif try_again_a in no:
            print(thank_you)
        else:
            print("Please type in 'Yes' or 'No'. ")
            try_again()
   
   #function to play again
    def play_again():
        q = input("Would you like to try another category? ").lower()
        if q in yes:
            call_deaths()
        elif q in no:
            print(thank_you)
        else:
            print("Please type in 'Yes' or 'No'. ")
            try_again()
   
       
    print(statement)
    
    def call_deaths():
    
        while True:
            print(selection)
            print(list_to_print)
            death = input(entry).lower()
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
                play_again()
                break
                
            elif death not in df.columns:
                print("I don't think you typed that in correctly. \n")
                try_again()
                break
            
            else:
                print(thank_you)
                break
        
    call_deaths()
    
    
max_deaths()
    