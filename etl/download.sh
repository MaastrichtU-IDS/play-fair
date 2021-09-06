#!/bin/bash

wget -N -P data/ https://ludii.games/downloads/database.zip

APP_NAME="${1:-vscode}"
oc project play-fair
pod_id=$(oc get pod --selector app=$APP_NAME --no-headers -o=custom-columns=NAME:.metadata.name)
echo "Preparing Pod on the DSRI with ID: $pod_id"

oc exec $pod_id -- mkdir -p /home/coder/project/etl/data/

oc cp data/database.zip $pod_id:/home/coder/project/etl/data/
