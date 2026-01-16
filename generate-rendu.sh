#!/bin/bash

set -e

mkdir -p generated-manifests
kompose convert -f docker-compose.yml -o generated-manifests/

mkdir -p "MichaudMael"
cp generated-manifests/*.yaml "MichaudMael/"

zip -r "MichaudMaelWordpress.zip" "MichaudMael/"