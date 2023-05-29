import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In search for happiness")

options = ("country", "happiness", "gdp", "social_support", "life_expectancy",
           "freedom_to_make_life_choices", "generosity", "corruption")
filename = "/Users/amitabhishek/Desktop/workingDir/Python/happiness/happy.csv"
df = pd.read_csv(filename)

# Selections
x_axis = st.selectbox("Select the data for x-axis", options)
y_axis = st.selectbox("Select the data for y-axis", options)

# Use the match ... case construct to handle different options
match (x_axis, y_axis):
    case pair if pair in [(x, y) for x in options for y in options if x != y]:
        # figure = px.scatter(df[options], df[options], labels={"x": f"{x_axis}", "y": f"{y_axis}"})
        figure = px.scatter(df[pair[0]], df[pair[1]], labels={"x": f"{x_axis}", "y": f"{y_axis}"})
        st.plotly_chart(figure)

        st.write(f'You selected {pair[0]} for x-axis and {pair[1]} for y-axis.')
        # Here is where you would insert the code to handle this specific combination
    case _:
        st.write('Invalid combination.')

# st.subheader(f"{x_axis} and {y_axis}")



