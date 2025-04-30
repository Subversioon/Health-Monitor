import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import PATIENT_DATA_FILE

# Load data
df = pd.read_csv(PATIENT_DATA_FILE)

st.title("🩺 Health Monitoring Dashboard")

st.header("Distribution of Health Parameters")

# Plot 1
fig1, ax1 = plt.subplots()
sns.histplot(df['bp'], kde=True, ax=ax1)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
sns.histplot(df['sugar_level'], kde=True, ax=ax2)
st.pyplot(fig2)

# Plot 2
st.header("Scatter Plots")

fig3, ax3 = plt.subplots()
sns.scatterplot(x='age', y='cholesterol', data=df, ax=ax3)
st.pyplot(fig3)

fig4, ax4 = plt.subplots()
sns.scatterplot(x='bp', y='sugar_level', data=df, ax=ax4)
st.pyplot(fig4)

# Plot 3
st.header("Blood Pressure by Gender")

fig5, ax5 = plt.subplots()
sns.boxplot(x='gender', y='bp', data=df, ax=ax5)
st.pyplot(fig5)

# Plot 4
st.header("Correlation Heatmap")

fig6, ax6 = plt.subplots()
correlation_matrix = df[['age', 'bp', 'sugar_level', 'cholesterol', 'hemoglobin']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax6)
st.pyplot(fig6)
