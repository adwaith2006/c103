import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
#fig=px.bar(df,x="Population",y="Per capita",color="Country",title="POPULATION AND PCI",orientation="h")
fig=px.scatter(df,x="Population",y="Per capita",color="Country",title="POPULATION AND PCI",size="Percentage",size_max=60)
fig.show()

