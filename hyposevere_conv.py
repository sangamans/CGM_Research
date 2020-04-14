# script for processing HypoSevere_Type1_200subjects
# Author: Sangaman Senthil
# Date: February 5th, 2020

import pandas as pd

# reading csv from raw data location
df = pd.read_csv("Google Drive/CGMprojectSpring2020/Datasets/HypoSevere_Type1_200subjects/RawData/RawData.txt", sep="|", low_memory=False)
# drop unwanted columns
df = df.drop(columns=['RecID', 'BCGMDeviceType', 'BFileType', 'CalBG'])
# rename columns
df = df.rename(columns={'PtID': 'id', 'DeviceDaysFromEnroll': 'time', 'DeviceTm': 'tm', 'Glucose': 'gl'})

# meeting format standards
function = lambda x: "1990-01-" + str(x+1)
# applying function to each element in Days Been column
df['time'] = df['time'].apply(function)

# combining the time and date column into one
df['time'] = df['time'] + " " + df['tm']
# dropping unwanted time column since date and time have been combine
df = df.drop(columns=['tm'])


# export final data set as csv (index = False drops the index column when exporting to csv)
df.to_csv(r"Google Drive/CGMprojectSpring2020/Datasets/HypoSevere_Type1_200subjects/CleanData/HypoSevere_Type1_200subjects.csv", index=False)

