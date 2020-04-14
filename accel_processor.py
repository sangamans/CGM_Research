# This is the script for processing the accelerometer data on average for 5 minute intervals
# Author: Sangaman Senthil
# Date: March 4, 2020

# import necessary libraries
import pandas as pd
import numpy as np

# read csv from accelerator data and replace * with file date
df = pd.read_csv('Google Drive/CGMprojectSpring2020/Datasets/D1NAMO_Type1_9subjects/Extra Info/healthy_subset/004/*_Accel.csv')

# change the data types to float anf date time because by default they were int
df = df.astype({'Vertical': 'float64'})
df = df.astype({'Lateral': 'float64'})
df = df.astype({'Sagittal': 'float64'})

# the euclidean norm equation
norm = np.sqrt(np.square(df['Vertical']) + np.square(df['Lateral']) + np.square(df['Sagittal']))

# create a column for the aggregated function
df['Norm'] = norm

# drop the unwanted columns
df = df.drop(columns=['Vertical', 'Lateral', 'Sagittal'])

# finding the average of norm for every 5 minutes
df['Time'] = pd.to_datetime(df['Time'])
df = df.groupby(pd.Grouper(key='Time', freq='5min')).mean()

# export cleaned data file to Clean data and replace * with the same one used to read csv on line 4
df.to_csv(r'Google Drive/CGMprojectSpring2020/Datasets/D1NAMO_Type1_9subjects/CleanData/Accel_Clean/004/*_Accel.csv')
