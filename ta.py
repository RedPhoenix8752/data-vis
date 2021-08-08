import csv
import pandas as pd
import plotly.graph_objects as po
df = pd.read_csv("datav.csv")
student_df = df.loc[df['student_id']=="TRL_xsl"]
print(student_df.groupby("level")["attempt"].mean())
fig = po.Figure(po.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ['level 1', 'level 2', 'level 3', 'level 4'], orientation = 'v'))
fig.show()