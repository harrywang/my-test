import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set page title
st.title('Line Chart Demo')

# Generate sample data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='M')
values = np.random.randn(len(dates)).cumsum()

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Value': values
})

# Display the line chart
st.subheader('Line Chart')
st.line_chart(df.set_index('Date'))

# Create and display a pie chart
st.subheader('Pie Chart')
pie_data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [25, 30, 22, 23]
})
fig = plt.figure()
plt.pie(pie_data['Values'], labels=pie_data['Category'], autopct='%1.1f%%')
st.pyplot(fig)

# Display the data
st.subheader('Sample Data')
st.dataframe(df)
