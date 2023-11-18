#!/bin/bash

cd api
docker build . -t gabrielpains/gabrielcardoso-playlists-recommender:0.1
docker push gabrielpains/gabrielcardoso-playlists-recommender:0.1
cd ..

cd model
docker build . -t gabrielpains/gabrielcardoso-playlists-model:0.1
docker push gabrielpains/gabrielcardoso-playlists-model:0.1
cd ..

docker image rm gabrielpains/gabrielcardoso-playlists-recommender:0.1
docker image rm gabrielpains/gabrielcardoso-playlists-model:0.1

clear
echo Done!