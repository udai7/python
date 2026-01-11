import streamlit as st
import pandas as pd

st.title("Streamlt text input")

name=st.text_input("Enter your name:")

age=st.slider("Select your age:", 0,100,25)


st.write(f"Your age is, {age}")

options=["python","C","Javascript","Java","C++"]
choice=st.selectbox("Choose your fav programming language:", options)
st.write(f"your favourite programming language is:", choice)


if name:
    st.write(f"Hellow, {name}")

data = {
    "Name":["Doie", "Jini", "Bhai", "Goru"],
    "Age": [22,21,230,10],
    "city": ["Shibuya", "Zurich", "Sri lonka bosti", "Otawa"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a CSV file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)