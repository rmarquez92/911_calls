import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('911.csv')

#BASIC QUESTIONS
#TOP 5 ZIP
df['zip'].value_counts().head()

#TOP 5 TOWNSHIPS
df['twp'].value_counts().head()

#Unique Title Codes
df['title'].nunique()
