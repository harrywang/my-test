import streamlit as st
import pandas as pd
import numpy as np

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
st.line_chart(df.set_index('Date'))

# Display the data
st.subheader('Sample Data')
st.dataframe(df)
