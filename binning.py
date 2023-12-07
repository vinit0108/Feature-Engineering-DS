#Numerical Binning Example
import pandas as pd


data['bin'] = pd.cut(data['value'], bins=[0,30,70,100], labels=["Low", "Mid", "High"])


#reading file
df_bin = pd.read_csv('stroke_prediction.csv')

#Creating bins and labels
bins = [1,19,30,50,100]
labels = ['minor','young','old','very_old']

df_bin['age_range'] = pd.cut(df_bin['age'],bins = bins, labels = labels)
##New change

