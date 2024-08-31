import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv")

data['modified_at'] = pd.to_datetime(data['modified_at'],unit='s')
data['Release_year'] =data['modified_at'].dt.year

colors = ["#ffa8bd",'#c889c2','#9269c6','#5b4acb','#242acf']

data_2017 = data[data['Release_year'] == 2017]
followers_per_track = data_2017.groupby('artist_name')['num_followers'].sum().reset_index()
top_tracks = followers_per_track.sort_values(by='num_followers', ascending=False).head(10)
plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
bars = plt.barh(top_tracks['artist_name'], top_tracks['num_followers'], color=colors)

for bar in bars:
    width = bar.get_width()
    plt.text(width - width * 0.05, bar.get_y() + bar.get_height() / 2, 
             f'{int(width):,}',
             ha='right',
             va='center',
             color='white',
             fontsize=10) 

plt.xlabel('Total Number of Followers', color='white')
plt.title('Top 10 Artists by Number of Followers', color='white')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_color('black')
plt.gca().spines['bottom'].set_color('black')
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.grid(color='white', linestyle='--', linewidth=0.5)
plt.gca().invert_yaxis()

st.pyplot(plt)

plt.show()

