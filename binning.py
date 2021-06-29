#Numerical Binning Example
data['bin'] = pd.cut(data['value'], bins=[0,30,70,100], labels=["Low", "Mid", "High"])
 import pandas as pd


#reading file
df_bin = pd.read_csv('stroke_prediction.csv')

#Creating bins and labels
bins = [1,19,30,50,100]
labels = ['minor','young','old','very_old']

df_bin['age_range'] = pd.cut(df_bin['age'],bins = bins, labels = labels)
