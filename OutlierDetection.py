
#BOX PLOT

import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=random_data)

#ScatterPlot
fig, ax = plt.subplots(figsize = (18,10))
ax.scatter(data['column'], data['column'])
# x-axis label
ax.set_xlabel('(Proportion non-retail business acres)/(town)')
  
# y-axis label
ax.set_ylabel('(Full-value property-tax rate)/( $10,000)')
plt.show()



'''Outlier Detection with Standard Deviation
If a value has a distance to the average higher than x * standard deviation, it can be assumed as an outlier. Then what x should be?
There is no trivial solution for x, but usually, a value between 2 and 4 seems practical.
'''
#Dropping the outlier rows with standard deviation
factor = 3
upper_lim = data['column'].mean () + data['column'].std () * factor
lower_lim = data['column'].mean () - data['column'].std () * factor

data = data[(data['column'] < upper_lim) & (data['column'] > lower_lim)]

'''
Outlier Detection with Percentiles
Another mathematical method to detect outliers is to use percentiles. You can assume a certain percent of the value from the top or the bottom as an outlier. The key point is here to set the percentage value once again, and this depends on the distribution of your data as mentioned earlier.

'''
#Dropping the outlier rows with Percentiles
upper_lim = data['column'].quantile(.95)
lower_lim = data['column'].quantile(.05)

data = data[(data['column'] < upper_lim) & (data['column'] > lower_lim)]


# Z score
from scipy import stats
import numpy as np
  
z = np.abs(stats.zscore(data['column']))
print(z)

#Threshold
threshold = 3
# Position of the outlier
print(np.where(z > 3))


# IQR
Q1 = np.percentile(data['column'], 25, 
                   interpolation = 'midpoint') 
  
Q3 = np.percentile(data['column'], 75,
                   interpolation = 'midpoint') 
IQR = Q3 - Q1 



#DBSCAN Clustering
from sklearn.cluster import DBSCAN
seed(1)
random_data = np.random.randn(50000,2)  * 20 + 20

outlier_detection = DBSCAN(min_samples = 2, eps = 3)
clusters = outlier_detection.fit_predict(random_data)
list(clusters).count(-1)




