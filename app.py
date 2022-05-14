import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

pie_chart_cols = ['Country,Other', 'TotalDeaths', 'TotalRecovered']
df = pd.read_csv('covid-info.csv', usecols=pie_chart_cols)
all_df = pd.read_csv('covid-info.csv')
del all_df['#']

options = ["All"] + df['Country,Other'].tolist()
selection = st.selectbox('Country: ', options)

if selection == "All":
    chart_options = ["Table", "Pie", "Bar"]
    chart_selection = st.selectbox('Chart type:', chart_options)

    if chart_selection == "Table":
        st.write(all_df)
    elif chart_selection == "Pie":
        cols = ['Country,Other', 'TotalCases']
        piedf = pd.read_csv('covid-info.csv', usecols=cols)

        countries = piedf['Country,Other'].tolist()
        values = piedf['TotalCases'].tolist()
        pie_labels = ['Country', 'Cases']

        number = st.slider(
            "Number of countries sorted by total number of cases: ",
            5, 25
        )

        for i in range(0, number):
            values[i] = int(values[i].replace(',', ''))

        data = {'Cases': values[0:number], 'Country': countries[0:number]}

        pie_df = pd.DataFrame(data)

        fig_pie = px.pie(pie_df, values='Cases', names='Country')
        st.plotly_chart(fig_pie)

    elif chart_selection == "Bar":
        pass

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
                [(int(data[0].replace(',', '')), "Total Deaths"), (int(data[1].replace(',', '')), "Total Recovered")],
                columns=labels)
            fig = px.pie(pie_df, values='value', names='type')
            st.plotly_chart(fig)

    elif chart_selection == "Bar":
        all_df.set_index("Country,Other", inplace=True)

        source = pd.DataFrame({
            'Number': [int(all_df.loc[selection]["Population"].replace(',', '')),
                       int(all_df.loc[selection]["TotalCases"].replace(',', '')),
                       int(all_df.loc[selection]["TotalRecovered"].replace(',', ''))],
            'Category': ['Population', 'Total Cases', 'Total Recovered']
        })

        st.altair_chart(
            alt.Chart(source).mark_bar().encode(y='Number', x='Category', tooltip=['Number', 'Category']).interactive(),
            use_container_width=True)
