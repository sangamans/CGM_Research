# CGM_Research

The following codes I have posted is related to my Continous Glucose Monitoring (CGM) Data Research with Dr. Irina Gaynanova at Texas A&M University. 

The purpose of this research is to research gaps and opportunities in data obtained from CGM device that contributes to diabetes and other clinical outcomes, affecting millions of patients across the nation.

Personally, I was able to get hands on experience with applying my web scraping, data analysis, data visualization, statistical methods, and data prediction using machine learning methods with large data sets.

In my GitHub, I have included some of my code that demonstrates my skills mentioned above. However, please do keep in mind that since I have worked with very different and large datasets. As a result, I have only only a few codes from the whole research in order to highlight specific skills.
Below, I have a key to what each code I have uploaded represents (code file name - description).

hyposevere_conv.py - This is processing code for data scraped from HypoSevere database with information on 200 subjects' health statistics and glucose data. I have cleaned this large dataset which contained various columns and messy data organization to meet standards for easier data handling. I also applied date time aggregation so that glucose data can be read as a function of time.

chypo_processor.py - This is the processing code for dataset that has glucose data along with heart rate data, medication data, insulin data and more medical data for 50 children with Type 1 diabetes. In order to clean and compile all these different datsets into one, I performed merging techniques along with data cleaning.

accel_processor.py - This code processes accelerometer datasets for 9 different subjects. An accelerometer is a device that measures acceleration of body segments in the x, y, and z axis. In order to calculate the overall activity data, I found the euclidean norm of each axis, which was its own column in the dataset, and aggregated the calculation to a seperate data column. The data set was originally measurements for every minute, so I applied rolling means algorithm so that the euclidean norm of the activity counts can be read for every 5 minutes instead.

D1NAMO_Accel.py - This code portrays my data visualization for the data processed in accel_processor.py. I worked with plotting datatime functons and making a datset with more than 200 values look clean and easy to read for statistical methods.

2014_10_02-10_56_44_Activity.png - This png file shows one of the many data visualization graphs I have created. This file is specifically the result of the D1NAMO_Accel.py code stated above.
