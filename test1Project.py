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

#function to replace N/A country codes with specific code
def country_codes_replace(country, country_code):
    idx = country
    subset_country = data_srt.loc[idx]
    
    if "N/A" in subset_country["Code"].values:
        subset_country["Code"] = subset_country["Code"].replace(["N/A"], country_code)

    
#call function to replace n/a country codes
country_codes_replace("Africa", "AFR")
country_codes_replace("America", "USA")
country_codes_replace("African Region", "AFR REG")
country_codes_replace("African Union", "AFR UNION")
country_codes_replace("Andean Latin America", "AL AMER")
country_codes_replace("Asia", "ASIA")
country_codes_replace("Australasia", "AUS ASIA")
country_codes_replace("Australasia & Oceania", "AUS-ASIA & OCEANIA")
country_codes_replace("Bosnia-Herzegovina", "BOS-HER")
country_codes_replace("Caribbean", "CARIB")
country_codes_replace("Central America & Caribbean", "CENT-AMER & CARIB")
country_codes_replace("Central Asia", "CENT-ASIA")
country_codes_replace("Central Europe", "CENT-EUR")
country_codes_replace("Central Europe, Eastern Europe, and Central Asia", \
                      "CENT-EUR & EAST-EU & CENT-ASIA")
country_codes_replace("Central Latin America", "CENT-LAT AMER")
country_codes_replace("Central sub-Saharan Africa", "CENT-SUB SAH-AFR")
country_codes_replace("Commonwealth", "COM-WEAL")
country_codes_replace("Commonwealth High Income", "COM-WEAL-HIGH")
country_codes_replace("Commonwealth Low Income", "COM-WEAL-LOW")
country_codes_replace("Commonwealth Middle Income", "COM-WEAL-MID")
country_codes_replace("East Asia", "EAST-ASIA")
country_codes_replace("East Asia & Pacific - World Bank region", "EAST-ASIA WORL-BANK")
country_codes_replace("East Germany (GDR)", "EAST-GER")
country_codes_replace("East Timor", "EAST-TIMOR")
country_codes_replace("Eastern Europe", "EAST-EUR")
country_codes_replace("Eastern Mediterranean Region", "EAST-MED-REG")
country_codes_replace("Eastern sub-Saharan Africa", "EAST-SUB SAH-AFR")
country_codes_replace("England", "ENGLAND")
country_codes_replace("Europe", "EUR")
country_codes_replace("Europe & Central Asia - World Bank region", "EUR & CENT-ASIA WORL-BANK")
country_codes_replace("European Region", "EUR REG")
country_codes_replace("European Union", "EUR UNION")
country_codes_replace("G20", "G20")
country_codes_replace("High SDI", "HIGH SDI")
country_codes_replace("High-income", "High-income")
country_codes_replace("High-income Asia Pacific", "HIGH ASIA-PAC")
country_codes_replace("High-income North America", "HIGH NOR-AMER")
country_codes_replace("High-middle SDI", "HIGH MID SDI")
country_codes_replace("International", "INTERNAT")
country_codes_replace("Latin America & Caribbean - World Bank region", \
                      "LAT-AMER & CARIB")
country_codes_replace("Low SDI", "LOW SDI")
country_codes_replace("Low-middle SDI", "LOW MID SDI")
country_codes_replace("Macau", "MACAU")
country_codes_replace("Middle East & North Africa", "MID-EAST & NOR AFR")
country_codes_replace("Middle SDI", "MID SDI")
country_codes_replace("Nordic Region", "NORD REG")
country_codes_replace("North Africa and Middle East", "NOR AFR & MID-EAST")
country_codes_replace("North America", "NOR AMER")
country_codes_replace("Northern Ireland", "NOR IREL")
country_codes_replace("OECD Countries", "OECD")
country_codes_replace("Oceania", "OCEANIA")
country_codes_replace("Region of the Americas", "REG OF AMERS")
country_codes_replace("Scotland", "SCOT")
country_codes_replace("Serbia-Montenegro", "SER-MONT")
country_codes_replace("South America", "SOU-AMER")
country_codes_replace("South Asia", "SOU-ASIA")
country_codes_replace("South Asia - World Bank region", "SOU-ASIA WORL-BANK")
country_codes_replace("South-East Asia Region", "SOU-EAST ASIA REG")
country_codes_replace("Southeast Asia", "SOU-EAST ASIA")
country_codes_replace("Southeast Asia, East Asia, and Oceania", "SOU-EAST ASIA & OCEANIA")
country_codes_replace("Southern Latin America", "SOU-LAT AMER")
country_codes_replace("Southern sub-Saharan Africa", "SOU-SAH AFR")
country_codes_replace("Sub-Saharan Africa", "SUB-SAH-AFR")
country_codes_replace("Sub-Saharan Africa - World Bank region", "SUB-SAH-AFR - WORL-BANK")
country_codes_replace("Tropical Latin America", "TROP LAT AMER")
country_codes_replace("Wales", "WALES")
country_codes_replace("West Germany (FRG)", "WEST-GER")
country_codes_replace("Western Europe", "WEST-EUR")
country_codes_replace("Western Pacific Region", "WEST-PAC REG")
country_codes_replace("Western sub-Saharan Africa", "WEST-SAH AFR")
country_codes_replace("World (excluding China)", "WORL-EX CHINA")
country_codes_replace("World Bank High Income", "WORL-BANK HIGH IN")
country_codes_replace("World Bank Low Income", "WORL-BANK LOW IN")
country_codes_replace("World Bank Lower Middle Income", "WORL-BANK LOW MID IN")
country_codes_replace("World Bank Upper Middle Income", "WORL-BANK UPP MID IN")
country_codes_replace("Zaire", "ZAIRE")


#slice data for Ireland
ireland = data_srt.loc["IRL":"IRL"]

