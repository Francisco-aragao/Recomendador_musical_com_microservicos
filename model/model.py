from fpgrowth_py import fpgrowth
import pandas as pd
import pickle
import time
import os
import ssl

# Disable ssl so read_csv can work properly
ssl._create_default_https_context = ssl._create_unverified_context

# Dataset url (Environment variable)
datasetUrl = os.environ.get('DATASET_URL')

# Persistent volume path
pvPath = "./shared/model.pickle"

# Read dataset
df = pd.read_csv(datasetUrl)

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

# Avoid termination
while (True):
    time.sleep(300)