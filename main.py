from googleapiclient.discovery import build

api_key = "AIzaSyAZBocBmigA4TGwQVUzfvhNXT_3uo1FEu0" 
   
# creating Youtube Resource Object
youtube_object = build("youtube","v3",developerKey = api_key)

print(youtube_object)