import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
	
import pandas as pd
matplotlib.style.use('ggplot') # Look Pretty
from sqlalchemy import create_engine
from scipy import misc

# Histogram Demo ---------------------------------------------------------
matplotlib.style.use('ggplot') # Look Pretty
# If the above line throws an error, use plt.style.use('ggplot') instead
	
student_dataset1 = pd.read_csv("E:\DAT210x-master\DAT210x-master\Module3\Datasets\students.data", index_col=0)
	
my_series = student_dataset1.G3
my_dataframe = student_dataset1[['G3', 'G2', 'G1']] 
	
my_series.plot.hist(alpha=0.5)
my_dataframe.plot.hist(alpha=0.5)

a=my_dataframe
print(a)

print('Next----Scatter')
student_dataset = pd.read_csv("E:\DAT210x-master\DAT210x-master\Module3\Datasets\students.data", index_col=0) 
c=student_dataset.plot.scatter(x='G1', y='G3')
print(c)


# If the above line throws an error, use plt.style.use('ggplot') instead
print('Next----3-D')
student_dataset2 = pd.read_csv("E:\DAT210x-master\DAT210x-master\Module3\Datasets\students.data", index_col=0)
	
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('Final Grade')
ax.set_ylabel('First Grade')
ax.set_zlabel('Daily Alcohol')
	
ax.scatter(student_dataset2.G1, student_dataset2.G3, student_dataset2['Dalc'], c='r', marker='.')
d=plt.show()
print(d)