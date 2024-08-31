import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

colors = ["#ffa8bd", '#c889c2', '#9269c6', '#5b4acb', '#242acf']
data = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv")

data_artist = data[data['artist_name'] == 'Imagine Dragons']
followers_per_track = data_artist.groupby('track_name')['num_followers'].sum().reset_index()
top_tracks = followers_per_track.sort_values(by='num_followers', ascending=False).head(5)

plt.style.use('dark_background')
plt.figure(figsize=(12, 8))

bars = plt.bar(top_tracks['track_name'], top_tracks['num_followers'], color=colors)
plt.xlabel('Track Name', color='white')
plt.ylabel('Total Number of Followers', color='white')
plt.title('Top 5 Tracks by Number of Followers (Imagine Dragons)', color='white')

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().xaxis.set_ticks_position('none')
plt.gca().yaxis.set_ticks_position('none')
plt.grid(color='white', linestyle='--', linewidth=0.5)

st.pyplot(plt)

plt.show()
