import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("Student Score Predictor")
st.write("Predict student exam score based on study hours using Linear Regression.")

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Scores": [10, 20, 30, 40, 50, 60, 70, 80, 90]
}
df = pd.DataFrame(data)

if st.checkbox("Show Training Dataset"):
    st.subheader(" Sample Data")
    st.dataframe(df)

X = df[['Hours']]
y = df['Scores']
model = LinearRegression()
model.fit(X, y)

st.subheader(" Enter Study Hours")
input_hours = st.number_input("How many hours did the student study?", min_value=0.0, max_value=24.0, step=0.5)

if input_hours:
    prediction = model.predict([[input_hours]])
    st.success(f" Predicted Score: {prediction[0]:.2f}")

st.subheader(" Regression Line")
fig, ax = plt.subplots()
ax.scatter(X, y, color='blue', label='Actual Scores')
ax.plot(X, model.predict(X), color='red', label='Regression Line')
ax.set_xlabel("Hours Studied")
ax.set_ylabel("Score")
ax.legend()
st.pyplot(fig)
