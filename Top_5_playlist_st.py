import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Specify data types for specific columns
dtype = {
    'num_followers': 'int32',
    'name': 'string',
    'modified_at': 'int64',
}

# Read CSV in chunks if it's too large to load at once
chunk_size = 100000 
chunks = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv", dtype=dtype, chunksize=chunk_size)

# Process chunks and concatenate them into a single DataFrame
data = pd.concat(chunk for chunk in chunks)

# Process data as before
colors = ["#ffa8bd", '#c889c2', '#9269c6', '#5b4acb', '#242acf']
data['modified_at'] = pd.to_datetime(data['modified_at'], unit='s')
data['Release_year'] = data['modified_at'].dt.year
data_2017 = data[data['Release_year'] == 2017]
followers_per_playlist = data_2017.groupby('name')['num_followers'].sum().reset_index()
top_playlists = followers_per_playlist.sort_values(by='num_followers', ascending=False).head(5)

plt.style.use('dark_background')
plt.figure(figsize=(12, 8))
bars = plt.barh(top_playlists['name'], top_playlists['num_followers'], color=colors)

for bar in bars:
    width = bar.get_width()
    plt.text(width - width * 0.05, bar.get_y() + bar.get_height() / 2,
             f'{int(width):,}',
             ha='right',
             va='center',
             color='white',
             fontsize=10) 

plt.xlabel('Total Number of Followers', color='white')
plt.title('Top 5 Playlists by Number of Followers in 2017', color='white')

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
