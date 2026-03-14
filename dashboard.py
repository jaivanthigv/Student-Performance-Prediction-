import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.title("🎓 Student Performance Dashboard")

# Load dataset
data = pd.read_csv("data/students.csv")

# Show dataset
st.subheader("Dataset Preview")
st.write(data)

# Chart 1: Study Hours vs Result
st.subheader("Study Hours vs Performance")

fig, ax = plt.subplots()
sns.boxplot(x="final_result", y="study_hours", data=data, ax=ax)
st.pyplot(fig)

# Chart 2: Attendance Distribution
st.subheader("Attendance Distribution")

fig, ax = plt.subplots()
sns.histplot(data["attendance"], bins=10, kde=True, ax=ax)
st.pyplot(fig)

# Chart 3: Previous Score vs Result
st.subheader("Previous Score vs Result")

fig, ax = plt.subplots()
sns.boxplot(x="final_result", y="previous_score", data=data, ax=ax)
st.pyplot(fig)

# Chart 4: Correlation Heatmap
st.subheader("Feature Correlation")

fig, ax = plt.subplots()
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)