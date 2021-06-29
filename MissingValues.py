#Missing Values

threshold = 0.7
#Dropping columns with missing value rate higher than threshold
data = data[data.columns[data.isnull().mean() < threshold]]

#Dropping rows with missing value rate higher than threshold
data = data.loc[data.isnull().mean(axis=1) < threshold]

##################################################################################

#Numerial Missing Values
#Filling all missing values with 0
data = data.fillna(0)

##################################################################################

#Filling missing values with medians of the columns
data = data.fillna(data.mean())
data = data.fillna(data.median())
data = data.fillna(data.mode())
##################################################################################

#Categorical Missing Values
#Max fill function for categorical columns
data['column_name'].fillna(data['column_name'].value_counts()
.idxmax(), inplace=True)

##################################################################################

#KNN Imputation
import sys
from impyute.imputation.cs import fast_knn
sys.setrecursionlimit(100000) #Increase the recursion limit of the OS
# start the KNN training
imputed_training=fast_knn(train.values, k=30)

##################################################################################

#MICE Imputation (Multivariate Imputation by Chained Equation )
from impyute.imputation.cs import mice
# start the MICE training
imputed_training=mice(train.values)

##################################################################################

#Deep Learning Imputation
import datawig

df_train, df_test = datawig.utils.random_split(train)

#Initialize a SimpleImputer model
imputer = datawig.SimpleImputer(
    input_columns=['1','2','3','4','5','6','7', 'target'], # column(s) containing information about the column we want to impute
    output_column= '0', # the column we'd like to impute values for
    output_path = 'imputer_model' # stores model data and metrics
    )

#Fit an imputer model on the train data
imputer.fit(train_df=df_train, num_epochs=50)

#Impute missing values and return original dataframe with predictions
imputed = imputer.predict(df_test)
