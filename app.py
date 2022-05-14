import streamlit as st
import pandas as pd
import plotly.express as px

pie_chart_cols = ['Country,Other', 'TotalDeaths', 'TotalRecovered']
df = pd.read_csv('covid-info.csv', usecols=pie_chart_cols)

options = ["All"] + df['Country,Other'].tolist()
selection = st.selectbox('Country: ', options)

if selection == "All":
    st.write(df)
else:
    chart_options = ["Pie", "Bar", "Plot", "Map"]
    chart_selection = st.selectbox('Chart type:', chart_options)

    if chart_selection == "Pie":
        df.set_index("Country,Other", inplace=True)
        data = df.loc[selection].tolist()

        labels = ['value', 'type']

        if pd.isna(data[0]) or pd.isna(data[1]):
            st.write("Incomplete data")
        else:
            pie_df = pd.DataFrame(
                [(int(data[0].replace(',', '')), "Total Recovered"), (int(data[1].replace(',', '')), "Total Deaths")],
                columns=labels)
            fig = px.pie(pie_df, values='value', names='type')
            st.plotly_chart(fig)
