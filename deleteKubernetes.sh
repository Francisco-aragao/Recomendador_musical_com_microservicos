#!/bin/bash

kubectl delete pvc project2-pv-gabrielcardoso
kubectl delete service gabrielcardoso-playlist-recommender-service
kubectl delete deploy gabrielcardoso-playlist-recommender-deployment