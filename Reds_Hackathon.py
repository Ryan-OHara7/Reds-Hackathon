# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd


excel_file_path1 = "C:/Users/Ryan/OneDrive/Documents/Reds Hackathon2023 Pitching Dataset.xlsx"
excel_file_path2 = "C:/Users/Ryan/OneDrive/Documents/Reds Hackathon/savant_pitch_level.csv"


pitcher_seasons = pd.read_excel(excel_file_path1)
print(pitcher_seasons)


#drop NA rows
pitcher_seasons = pitcher_seasons.drop([550, 551], axis=0)



print(pitcher_seasons[['Age', 'GS', 'G', 'Stuff+']].dtypes)

#Quality Pitch conditions
QP_Var = ['Stf+ FA', 'Stf+ SI', 'Stf+ FC', 'Stf+ FS', 'Stf+ SL', 'Stf+ CU', 'Stf+ CH', 'Stf+ KC']
QP_three_plus = pitcher_seasons[pitcher_seasons[QP_Var] > 100].sum(axis=1) >= 3
QP_two_plus = pitcher_seasons[pitcher_seasons[QP_Var] > 100].sum(axis=1) >=2

#Elite Pitch conditions
conditions = (
    (pitcher_seasons['Stf+ SI'] >= 123.679403) ,
    (pitcher_seasons['Stf+ FC'] >= 124.0058363) ,
    (pitcher_seasons['Stf+ FS'] >= 150.8215068) ,
    (pitcher_seasons['Stf+ SL'] >= 141.2422957) ,
    (pitcher_seasons['Stf+ CU'] >= 139.537178) ,
    (pitcher_seasons['Stf+ CH'] >= 113.1669972) ,
    (pitcher_seasons['Stf+ KC'] >= 154.0185689)
)



QP_count = (pitcher_seasons[['Stf+ FA', 'Stf+ SI', 'Stf+ FC', 'Stf+ FS', 'Stf+ SL', 'Stf+ CU', 'Stf+ CH', 'Stf+ KC']] > 100).sum(axis=1)
pitcher_seasons4 = pitcher_seasons[(QP_count >= 1) & (QP_count <= 2)]
pitcher_seasons4['Elite_Pitches'] = sum(conditions)


pitcher_seasons2 = pitcher_seasons[QP_three_plus]
pitcher_seasons3 = pitcher_seasons[QP_two_plus]

#Filtering Data Frame for pitchers moving from RP to SP roles based on intuitive metrics
RP_to_SP = pitcher_seasons2[
    (pitcher_seasons2['GS %'] < .50 ) & 
    (pitcher_seasons2['xERA'] < 4.00) 
]    



#Filtering Data Frame for pitchers moving from SP to RP roles based on intuitive metrics
SP_to_RP = pitcher_seasons3[
    (pitcher_seasons3['GS %'] >= .50) &
    (pitcher_seasons3['Role'] != 'RP') &
    (pitcher_seasons3['xERA'] >= 4.2)
]

#Filtering for CP candidates
CP_Candidate = pitcher_seasons4[
    (pitcher_seasons4['Role'] != 'CL') &
    (pitcher_seasons4['SV'] < 5) &
    (pitcher_seasons4['xERA'] > 4.2)
]