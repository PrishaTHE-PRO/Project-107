import csv
import pandas as pd 
import plotly.graph_objects as go 
import plotly.express as px 

df = pd.read_csv('data.csv')
mean=df.groupby(['level','student_id'],as_index=False)['attempt'].mean()
fig=px.scatter(mean,x='student_id',y='level',size='attempt',color='attempt')
fig.show()