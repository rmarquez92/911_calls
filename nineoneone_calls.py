import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('911.csv')

#BASIC QUESTIONS
#TOP 5 ZIP
df['zip'].value_counts().head()

#TOP 5 TOWNSHIPS
df['twp'].value_counts().head()

#Unique Title Codes
df['title'].nunique()

#CREATING NEW FEATURES
#Get Reason - w/o details
df['Reason'] = df['title'].str.split(':').apply(lambda x: x[0])
df['Reason'].value_counts()

sns.countplot(x='Reason',data=df)
plt.show()
