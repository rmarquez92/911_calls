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
#df['Reason'] = df['title'].apply(lambda title: title.split(':')[0]) works too
df['Reason'].value_counts()

#sns.countplot(x='Reason',data=df)
#plt.show()

#Find data type of time stamp (str)
type(df['timeStamp'].iloc[0])

df['Time']= pd.to_datetime(df['timeStamp'])
df['Hour'] = df['Time'].apply(lambda time: time.hour)
df['Month'] = df['Time'].apply(lambda time: time.month)
df['Day of Week'] = df['Time'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].apply(lambda dow: dmap[dow])

plt.figure(figsize=(12,6))
sns.countplot(x='Day of Week', data=df ,hue='Reason')
plt.legend(bbox_to_anchor=(1.125, 1))
plt.tight_layout()
#plt.show()

plt.figure(figsize=(12,6))
sns.countplot(x='Month', data=df ,hue='Reason')
plt.legend(bbox_to_anchor=(1.125, 1))
plt.tight_layout()
#plt.show()


byMonth = df.groupby('Month').count()
#Line Plot of Calls per Month
fig = plt.figure()
byMonth['Reason'].plot()
#plt.show()


#Linear Fit of Calls/Month
byMonth = byMonth.reset_index()
sns.lmplot(x='Month',y='Reason',data=byMonth)
plt.show()
 
