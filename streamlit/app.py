import streamlit as st
import pandas as pd
import numpy as np

##Title of the application
st.title("Hello JINIIIIIII")

##Display a simple text
st.write("This is a simple text for jini baby")

##Create a simple dataframe

df=pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})

##Display the dataframe

st.write("Here is the data frame")
st.write(df)

##Creating a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)