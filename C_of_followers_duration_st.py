import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.ticker import ScalarFormatter

data = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv")

data['modified_at'] = pd.to_datetime(data['modified_at'],unit='s')
data['Release_year'] =data['modified_at'].dt.year
data['duration_m'] = data['duration_ms'] / 60000
data_2017 = data[data['Release_year'] == 2017]
track_data = data_2017.groupby('duration_m').agg({'num_followers': 'sum'}).reset_index()

# Set up the figure dimensions
fig, ax = plt.subplots(figsize=(15, 10))

# Scatter plot of the relationship between track duration and the total number of followers
sns.regplot(data=track_data, x='duration_m', y='num_followers', 
            scatter_kws={'s': 100, 'color': '#db57b2'}, 
            line_kws={'color': '#5770db'}, ax=ax)

# Set labels and title
ax.set_xlabel('Track Duration (minutes)', fontsize=14, color='white')
ax.set_ylabel('Total Number of Followers', fontsize=14, color='white')
ax.set_title('Comparison Between Track Duration and Total Number of Followers', fontsize=16, color='white')

# Customize the plot appearance
ax.set_facecolor('#000000')
fig.patch.set_facecolor('#000000')
plt.xticks(color='white')
plt.yticks(color='white')
plt.grid(True, linestyle='--', alpha=0.5, color='white')

# Set x-axis ticks to include 0, 5, 10, 15, ..., 160
ax.set_xticks(range(0, 165, 5))
ax.set_yticks(range(0,21001,500))
# Use scientific notation for the y-axis if needed
ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False, useMathText=True))

# Set the color of y-axis numbers to white
ax.tick_params(axis='y', colors='white')

# Display the plot in Streamlit
st.pyplot(fig)
