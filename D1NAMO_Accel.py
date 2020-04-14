import matplotlib.pyplot as plt
import pandas as pd

# read the cleaned accelerometer data (change n depending on file)
df = pd.read_csv('n_Accel_processed.csv')

# change data type to date time for readability
df['Time'] = pd.to_datetime(df['Time'])
df['Time'] = df['Time'].dt.time

# date time to just time column csv used for plotting
df.to_csv(r'n_time_processed.csv', index=False)

# read the csv from above
gp = pd.read_csv('n_time_processed.csv')

# plot the time and activity count
plt.plot(gp['Time'], gp['Norm'])
plt.grid()

# format the x ticks for better looking plot
plt.tick_params(axis='x', width=0.1, labelrotation=90, labelsize=7)

# label x, y, and Title
plt.title(label='Accelerometer Graph for 2014_10_03-06_20_53')
plt.xlabel(xlabel='Time')
plt.ylabel(ylabel='Activity Count')

# fixing gap between x ticks for even better graph
plt.gca().margins(x=0)
plt.gcf().canvas.draw()
tl = plt.gca().get_xticklabels()
maxsize = max([t.get_window_extent().width for t in tl])
m = 0.2 # inch margin
s = maxsize/plt.gcf().dpi*400+2*m
margin = m/plt.gcf().get_size_inches()[0]
plt.gcf().subplots_adjust(left=margin, right=1.-margin, bottom=0.19)
plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

# save the final plot as .png file (again, change n depending on file)
plt.savefig('n_Accel.png')
