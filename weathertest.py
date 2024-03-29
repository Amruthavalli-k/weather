import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
logo = Image.open('logo1.png')
icon = Image.open('clouds1.jpg')

st.set_page_config(page_title="weather  EDA", page_icon=icon, layout="wide")
st.image(logo)
st.title("Exploratory Data Analysis on Weather Dataset")
st.image(icon,width=900)
# File upload
uploaded_file = st.file_uploader("Choose a Weather Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
    data.rename(columns = {'Weather' : 'Weather Condition'}, inplace=True)
# Define the list of names
names = ["K.NEERAJA", "K.AMRUTHA VALLI", "K.VAMSI","B.SAI RAM","CH.KALYAN RAM","T.MUKESH","A.HEMANTH"]

# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)

st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
st.sidebar.write("Dr.P.Srinivasulu")
st.header("Weather Data Analysis")
if st.checkbox("Show raw data"):
        st.write(data)
if st.checkbox("Show first 25 rows"):
        st.write(data.head(25))
st.header("Data Cleaning and Preprocessing")
if st.checkbox("Show null values count of all attributes"):
    st.write(data.isnull().sum())
if st.checkbox("Showing null values count of all attributes after data preprocessing :"):
      data=data.dropna()
      st.write(data.isnull().sum())  
if st.checkbox("show preprocessed data"):
    data=data.dropna() 
    st.write(data)
     
st.header("Basic information on dataset")
option=st.selectbox("Select any of the below basic informatiom on dataset",["Show shape","Show index","Show columns","Show data types","Show count of non-null values","Show unique values count for each column"])
if (option=="Show shape"):
        st.write(data.shape)
if (option=="Show index"):
        st.write(data.index)
if (option=="Show columns"):
        st.write(data.columns)
if (option=="Show data types"):
        st.write(data.dtypes)
if (option=="Show count of non-null values"):
        st.write(data.count())
if (option=="Show unique values count for each column"):
        st.write(data.nunique())
if st.checkbox("Show statistical analysis of the dataset"):
        st.write(data.describe())
st.header("Appling Special or Required Querirs based on the dataset")
unq = st.selectbox("Show unique values of:",data.columns)
if unq is not None:
        st.write(data[unq].unique())
w=data['Weather Condition'].unique()
weathr1 = st.selectbox("Show number of times 'Weather' is :",w)
if weathr1 is not None:
        st.write(data[data['Weather Condition'] == weathr1].shape[0])
if st.checkbox("Show number of times 'Wind Speed was exactly selected km/h'"):
        wd1=st.slider("Select the wind speed :",0,80)
        st.write(data[data['Wind Speed_km/h'] == wd1].shape[0])
        st.write(data[data['Wind Speed_km/h'] == wd1])
        
if st.checkbox("Mean values of attributes of the dataset"):
        men=st.selectbox("Select the desired column: ",['Temp_C','Dew Point Temp_C','Rel Hum_%','Wind Speed_km/h','Visibility_km'])
        st.write(data[men].mean())
if st.checkbox("Show Standard Deviation of 'Pressure'"):
        st.write(data.Press_kPa.std())
if st.checkbox("Show Variance of 'Relative Humidity'"):
        st.write(data['Rel Hum_%'].var())
    

wethr=st.selectbox("Show all instances when the following  'Weather Condition' was recorded:",w)
if wethr is not None:
    st.write('Number of instances of ',wethr,' are: ',data[data['Weather Condition']==wethr].shape[0])
    st.write(data[data['Weather Condition']==wethr])
 
if st.checkbox("Show all instances when 'Wind Speed' and 'Visibility' are greater than selected values"):
        wispeed = st.slider('Choose the wind speed:', 0, 100)
        visib= st.slider('Choose the visibility:', 0, 50)
        st.write(data[(data['Wind Speed_km/h'] > wispeed) & (data['Visibility_km'] >visib)])
if st.checkbox("Show all instances when 'Wind Speed' and 'Visibility' are less than selected values"):
        ws = st.slider('Choose the wind speed:', 0, 80)
        vb= st.slider('Choose the visibility:', 0, 60)
        st.write(data[(data['Wind Speed_km/h'] < ws) & (data['Visibility_km'] <vb)])
if st.checkbox("Show Mean value of each column against each 'Weather Condition'"):
        data["Date/Time"] = pd.to_datetime(data["Date/Time"])
        data["Month"] = data["Date/Time"].dt.month
        st.write(data.groupby('Weather Condition').mean())
if st.checkbox("Show Minimum value of each column against each 'Weather Condition'"):
        st.write(data.groupby('Weather Condition').min())
if st.checkbox("Show Maximum value of each column against each 'Weather Condition'"):
        st.write(data.groupby('Weather Condition').max())
if st.checkbox("Show all instances when "):
        wcond= st.selectbox("select the weather condition:",data['Weather Condition'].unique())
        rel1=st.slider('Choose the Relative humidity range:', 0, 100)
        visib2= st.slider('choose the visibilty level:',0,50)
        temp1=st.slider('choose the temperature:', -10, 40)
        wind1=st.slider('choose the windspeed_kmph:',1,80)
        x1=data[data['Weather Condition'] == wcond ]
        x1=x1[x1['Rel Hum_%'] == rel1] 
        x1=x1[x1['Visibility_km'] == visib2]
        x1=x1[x1['Wind Speed_km/h'] == wind1]
        st.write(x1)
        

# Convert date column to datetime
if uploaded_file is not None:
    data["Date/Time"] = pd.to_datetime(data["Date/Time"])
    # Create new column for month
    data["Month"] = data["Date/Time"].dt.month
    # Calculate mean temperature by month
    mean_temp_by_month = data.groupby("Month")["Temp_C"].mean()
if st.checkbox("Average temperatures of individual months throughout the year"):
    if st.checkbox("January"):
        st.write('the average temperature of january month:',mean_temp_by_month[1])
    if st.checkbox("February"):
        st.write('the average temperature of February month:',mean_temp_by_month[2])
    if st.checkbox("March"):
        st.write('the average temperature of March month:',mean_temp_by_month[3])
    if st.checkbox("April"):
        st.write('the average temperature of April month:',mean_temp_by_month[4]) 
    if st.checkbox("May"):
        st.write('the average temperature of may month:',mean_temp_by_month[5])
    if st.checkbox("June"):
        st.write('the average temperature of june month:',mean_temp_by_month[6])
    if st.checkbox("July"):
        st.write('the average temperature of july month:',mean_temp_by_month[7])   
    if st.checkbox("August"):
        st.write('the average temperature of August month:',mean_temp_by_month[8])
    if st.checkbox("September"):
        st.write('the average temperature of September month:',mean_temp_by_month[9])
    if st.checkbox("October"):
        st.write('the average temperature of October month:',mean_temp_by_month[10])
    if st.checkbox("November"):
        st.write('the average temperature of November month:',mean_temp_by_month[11])
    if st.checkbox("December"):
        st.write('the average temperature of December month:',mean_temp_by_month[12])
st.header("Data visualization on the dataset")
# Create histogram of temperatures
if st.checkbox("Frequency distribtion of temperatures throughout the year"):
   fig, ax = plt.subplots()
   sns.histplot(data=data, x="Temp_C", ax=ax)
   ax.set_xlabel("Temperature (Celsius)")
   ax.set_ylabel("Count")
   st.pyplot(fig)
#Is there a relationship between temperature and visibility?
# Data visualization question

# Create histplot of temperature and Relative humidity
if st.checkbox(" Relationship between Temperature and Relative Humidity"):
  if uploaded_file is not None:
    fig, ax = plt.subplots()
    sns.histplot(data=data, y="Temp_C", x="Rel Hum_%", ax=ax)
    ax.set_ylabel("Temperature (Celsius)")
    ax.set_xlabel("Relative Humidity (%)")
    st.pyplot(fig)
#  Create scatterplot of temperature and Dew point temp    
if st.checkbox(" Relationship between Temperature and Dew Point Temperature"):
  if uploaded_file is not None:
    fig, ax = plt.subplots()
    sns.histplot(data=data, x="Temp_C", y="Dew Point Temp_C", ax=ax)
    ax.set_xlabel("Temperature (Celsius)")
    ax.set_ylabel("Dew Point Temp_C (celsius)")
    st.pyplot(fig)
    st.header("The temperature and Dew point are observed to be strongly postively Correlated")
if uploaded_file is not None:
   fig, ax = plt.subplots()
   sns.scatterplot(data=data, x="Temp_C", y="Visibility_km", ax=ax)
   ax.set_xlabel("Temperature (Celsius)")
   ax.set_ylabel("Visibility (km)")
# Display scatterplot
if st.checkbox(" Relationship between Temperature and Visibility"):
   st.pyplot(fig)

#What is the average temperature by month?
# Create bar chart of mean temperature by month
if uploaded_file is not None:
    fig, ax = plt.subplots()
    mean_temp_by_month.plot(kind="bar", ax=ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Mean Temperature (Celsius)")
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=0)
# Display bar chart
if st.checkbox("show average temperature by month"):
   st.pyplot(fig)
#average pressure by weather condition
if st.checkbox("Show Average pressure by weather condition"):
    avg_pressure=data.groupby("Weather Condition")["Press_kPa"].mean()
    st.write("Average pressure by weather condition")
    st.write(avg_pressure)
    # Create bar chart of mean pressure by weather condition
    fig, ax = plt.subplots()
    avg_pressure.plot(kind="bar", ax=ax)
    ax.set_xlabel("Press_kPa")
    ax.set_ylabel("Weather Condition")
    #ax.set_xticklabels(["data.groupby('Weather Condition')"], rotation=0)
    # Display bar chart
    st.pyplot(fig)
