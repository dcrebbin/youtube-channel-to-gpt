import os
import json
from googleapiclient.discovery import build 
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API setup
API_KEY = os.getenv("YOUTUBE_API_KEY")
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Constants
CHANNEL_ID = 'UCcefcZRL2oaA_uBNeo5UOWg' 
MAX_RESULTS = 50

# Get medium videos
medium_videos = youtube.search().list(
    part='snippet', 
    channelId=CHANNEL_ID,
    type='video',
    videoDuration='medium',
    maxResults=MAX_RESULTS
).execute()

# Get long videos  
long_videos = youtube.search().list(
    part='snippet',
    channelId=CHANNEL_ID,
    type='video', 
    videoDuration='long',
    maxResults=MAX_RESULTS
).execute()

# Extract video IDs
video_ids = []

for video in medium_videos['items'] + long_videos['items']:
    if video['id']['kind'] == 'youtube#video':
        video_ids.append(video['id']['videoId']) 
        
# Save video IDs to file
with open('./src/youtube-ids.json', 'w') as f:
    json.dump(video_ids, f)

print("Saved video IDs to constants file")