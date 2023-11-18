#!/bin/bash

#kubectl -n gabrielcardoso apply -f claim.yaml
kubectl -n gabrielcardoso apply -f service.yaml
kubectl -n gabrielcardoso apply -f deployment.yaml

kubectl -n gabrielcardoso get pvc
kubectl -n gabrielcardoso get deployment
kubectl -n gabrielcardoso get service
kubectl -n gabrielcardoso get pods --watch