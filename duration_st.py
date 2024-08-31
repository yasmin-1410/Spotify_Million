import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

data = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv")

data['duration_m'] = data['duration_ms'] / 60000
data['modified_at'] = pd.to_datetime(data['modified_at'],unit='s')
data['Release_year'] =data['modified_at'].dt.year
data_2017 = data[data['Release_year'] == 2017]
colors = ["#ffa8bd",'#c889c2','#9269c6','#5b4acb','#242acf']

track_duration_sum = data_2017.groupby('track_name')['duration_m'].sum().reset_index()

# Sort by duration and select the top N tracks
top_n = 10  # Adjust as needed
track_duration_sum = track_duration_sum.nlargest(top_n, 'duration_m')

# Set up the colors for the pie chart
colors = sns.color_palette(colors, len(track_duration_sum))

# Create the pie chart with a black background
plt.figure(figsize=(12, 8), facecolor='black')  # Set the figure background color to black
ax = plt.gca()
ax.set_facecolor('black')  # Set the axes background color to black

# Plot the pie chart
wedges, texts, autotexts = plt.pie(track_duration_sum['duration_m'], 
                                   labels=track_duration_sum['track_name'],
                                   autopct='%1.1f%%', 
                                   colors=colors,
                                   wedgeprops={'edgecolor': 'black'})  # Adds a border around each wedge for contrast

# Customize text colors to be visible on black background
plt.title('Top Track Duration Distribution in 2017 (in minutes)', color='white')

# Change the color of the pie chart text and percentages
for text in texts:
    text.set_color('white')
for autotext in autotexts:
    autotext.set_color('white')
st.pyplot(plt)
plt.show()
