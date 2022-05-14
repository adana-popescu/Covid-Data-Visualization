import streamlit as st
import pandas as pd
import plotly.express as px

pie_chart_cols = ['Country,Other', 'TotalDeaths', 'TotalRecovered']
df = pd.read_csv('covid-info.csv', usecols=pie_chart_cols)

options = df['Country,Other'].tolist()
selection = st.selectbox('Country: ', options)

df.set_index("Country,Other", inplace=True)
data = df.loc[selection].tolist()

labels = ['value', 'type']

pie_df = pd.DataFrame([(int(data[0].replace(',', '')), "Total Recovered"), (int(data[1].replace(',', '')), "Total Deaths")], columns=labels)
fig = px.pie(pie_df, values='value', names='type', title='ad')
st.plotly_chart(fig)
