#!/bin/bash

URL=$1
EMAIL="test@gmail.com"
SUBJECT="I will always be here for PLD"

curl -X POST \
  $URL \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "email=$EMAIL&subject=$SUBJECT"
