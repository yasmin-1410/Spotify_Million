import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("D:\\Yasmin\\Study\\Spotify_Million.csv")
data['modified_at'] = pd.to_datetime(data['modified_at'],unit='s')
data['Release_year'] =data['modified_at'].dt.year
followers_per_year = data.groupby('Release_year')['num_followers'].sum().reset_index()
most_followers_year = followers_per_year.sort_values(by='num_followers', ascending=False).iloc[0]

plt.plot(followers_per_year['Release_year'], followers_per_year['num_followers'], marker='o', color='#c889c2', linestyle='-')

for i, row in followers_per_year.iterrows():
    plt.text(row['Release_year'], row['num_followers'], f'{int(row["num_followers"]):,}', 
             ha='center',  
             va='bottom',
             fontsize=10)

plt.xlabel('Year')
plt.ylabel('Total Number of Followers')
plt.title('Total Number of Followers per Year')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

st.pyplot(plt)

plt.show()