# script for ChildrenHypo_Type1_50subjects - Extra data processor
# Author: Sangaman Senthil
# Date: February 24th, 2020

# import the pandas library
import pandas as pd

# read all relevent data sets as csv
# enrollment for covariant
cov = pd.read_csv('Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/RawData/tblDEnrollment.csv')
bd = pd.read_csv('Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/RawData/tblDDataBDMeter.csv')
hrt = pd.read_csv('Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/RawData/tblDHeartRateData.csv')
med = pd.read_csv('Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/RawData/tblDMedications.csv')

# drop unwanted columns
cov = cov.drop(columns=['VisitDt', 'RaceDs', 'InsDur1Yr', 'Regular', 'InsOth', 'InsOthDs', 'InsStable', 'EligVer'])
cov = cov.drop(columns=['PEAbn', 'PEAbnDs', 'PubicH', 'BreGen', 'TotLongAct', 'RecID', 'OthCareGvr'])

bd = bd.drop(columns=['RecID'])

hrt = hrt.drop(columns=['RecID'])

med = med.drop(columns=['RecID', 'DCRCAdmType'])

# rename columns
med = med.rename(columns={'GenName': 'MedName', 'Dose': 'MedDose', 'Frequency': 'MedFreq'})

# combine tblDEnrollment.csv with tblDMedications.csv to create covariant data file
cov = cov.merge(med, on='PtID', how='left')

# export as csv
cov.to_csv(r'Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/CleanData/ChildrenHypo_Type1_50subjects_covariant.csv', index=False)
bd.to_csv(r'Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/CleanData/BDMeter.csv', index=False)
hrt.to_csv(r'Google Drive/CGMprojectSpring2020/Datasets/ChildrenHypo_Type1_50subjects/CleanData/HeartRate.csv', index=False)