import pandas 
import plotly.express as px

df=pandas.read_csv("line_chart.csv")
#fig=px.line(df,x="Year",y="Per capita income" ,color="Country",title="Per Capita Income")
#fig=px.bar(df,x="Year",y="Per capita income" ,color="Country",title="Per Capita Income")
fig=px.scatter(df,x="Year",y="Per capita income" ,color="Country",title="Per Capita Income")
fig.show()
