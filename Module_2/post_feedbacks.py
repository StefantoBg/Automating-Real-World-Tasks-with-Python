#!/usr/bin/env python3
import os 
import requests 

#set source dir
src_dir="/data/feedback/"

# get list of files
files = os.listdir(src_dir)

#function to read each file line 
def readperline(file):
  with open(src_dir + file) as f:
    lines = f.read().splitlines()
  reurn lines

# Make s list with entries

feedback = []
keys = ["title", "name", "data", "feedback"]
for file in files:
  lines = readperline(file)
  feedback.append(dict(zip(keys, lines)))

#set url 
url = "http://localhost/feedback/"

# post entries

for entry in feedback: 
  response = requests.post(url, data=entry)
  if response.ok:
    print("Feedback posted")
  else: 
    print(f"Server error: {response.status_code}")



