from fpgrowth_py import fpgrowth
import pandas as pd
import pickle

# Dataset file
file = "/shared/2023_spotify_ds1.csv"

# Persistent volume path
pvPath = "/shared/model.pickle"

# Read dataset
df = pd.read_csv(file)

df.drop(columns=['track_uri', 'album_name', 'album_uri', 'artist_name', 'artist_uri', 'duration_ms'], inplace=True)

# Group playlists songs
df = df.groupby(['pid']).agg({'track_name': ';; '.join})

# Get list of songs per playlist
playlistSongsList = []

for index, row in df.iterrows():
    songs = str(row['track_name']).split(sep=';; ')

    playlistSongsList.append(songs)

# Train model yay :)
freqItemSet, rules = fpgrowth(playlistSongsList, minSupRatio=0.07, minConf=0.5)

# Dump rules
pickle.dump(rules, open(pvPath, 'wb'))