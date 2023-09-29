import streamlit as st
import seaborn as sns
import pandas as pd
import seaborn as sd
import matplotlib.pyplot as plt


df_walmart=pd.read_csv('WALMART_SALES_DATA.csv')

st.set_page_config(page_title="Walmart Sales Analysis", layout="wide")
st.title('Walmart Sales Analysis')
st.divider()

#options = st.sidebar.radio(", [‘All Data’, ‘Link’])

col1,col2=st.columns([1,1])


plt.figure(figsize=(25,10))
col1.markdown('Weekly sales of 35 stores')
col1.pyplot(sns.barplot(data=df_walmart, x="Store", y="Weekly_Sales").figure)

plt.figure(figsize=(25,10))
col2.markdown('Influence of Holiday on weekly_sales')
col2.pyplot(sns.histplot(data=df_walmart, x="Weekly_Sales", hue="Holiday_Flag", kde=True).figure)

col3,col4=st.columns([1,1])
plt.figure(figsize=(25,12))
col3.markdown('Temperature V/s Weekly Sales')
col3.pyplot(sns.scatterplot(data=df_walmart, x='Temperature', y='Weekly_Sales').figure)

plt.figure(figsize=(25,12))
col4.markdown('Fuel Price V/s Weekly Sales')
col4.pyplot(sns.scatterplot(data=df_walmart, x='Fuel_Price', y='Weekly_Sales').figure)

col5,col6=st.columns([1,1])

plt.figure(figsize=(6,6))
col5.markdown('Holiday Season with Weekly Sales using cat plot')
col5.pyplot(sns.catplot(df_walmart[0:1000], x="Holiday_Flag", y="Weekly_Sales",kind="swarm").figure)

plt.figure(figsize=(25,12))
col6.markdown('Holiday Season with Weekly Sales using bar plot')
col6.pyplot(sns.barplot(x='Holiday_Flag', y='Weekly_Sales', data=df_walmart).figure)

