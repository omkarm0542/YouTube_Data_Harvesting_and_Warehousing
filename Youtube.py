#pip install streamlit google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pymongo
#python -m venv env
#source env/bin/activate


import streamlit as st
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pymongo import MongoClient
from googleapiclient.errors import HttpError
from datetime import datetime
import google.auth
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
# Create a MongoDB client
client = MongoClient()











youtube = build(api_name, api_version, developerKey=api_key)
api_key = 'AIzaSyCPbBuCVwWYq6aXGrfVQSKvdlkfMixfHCM'
api_name = 'youtube'
api_version = 'v3'

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

def get_channel_data(api_key, channel_id):
    # Build the YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Request the channel's details
    try:
        channel_response = youtube.channels().list(
            part='snippet, statistics',
            id=channel_id
        ).execute()
    except HttpError as e:
        print('An HTTP error occurred:')
        print(json.loads(e.content)['error']['message'])
        return None

    # Extract the channel details
    channel_info = channel_response['items'][0]
    channel_name = channel_info['snippet']['title']
    subscription_count = channel_info['statistics']['subscriberCount']
    channel_views = channel_info['statistics']['viewCount']
    channel_description = channel_info['snippet']['description']

    # Request the channel's playlists
    playlists_response = youtube.playlists().list(
        part='snippet',
        channelId=channel_id,
        maxResults=50
    ).execute()

    # Extract the playlist details
    playlist_ids = []
    for playlist_item in playlists_response['items']:
        playlist_ids.append(playlist_item['id'])

    # Request the videos in each playlist
    videos_data = []
    for playlist_id in playlist_ids:
        videos_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50
        ).execute()

        # Extract the video details
        for video_item in videos_response['items']:
            video_id = video_item['snippet']['resourceId']['videoId']
            video_name = video_item['snippet']['title']
            video_description = video_item['snippet']['description']
            published_at = video_item['snippet']['publishedAt']
            view_count = video_item['snippet']['statistics']['viewCount']
            like_count = video_item['snippet']['statistics']['likeCount']
            dislike_count = video_item['snippet']['statistics']['dislikeCount']
            favorite_count = video_item['snippet']['statistics']['favoriteCount']
            comment_count = video_item['snippet']['statistics']['commentCount']
            duration = video_item['snippet']['duration']
            thumbnail = video_item['snippet']['thumbnails']['default']['url']
            caption_status = video_item['snippet']['localized']['isDefaultLanguage']
            
            # Store the video data in a dictionary
            video_data = {
                'Channel_Name': channel_name,
                'Channel_Id': channel_id,
                'Subscription_Count': subscription_count,
                'Channel_Views': channel_views,
                'Channel_Description': channel_description,
                'Playlist_Id': playlist_id,
                'Video_Id': video_id,
                'Video_Name': video_name,
                'Video_Description': video_description,
                'PublishedAt': published_at,
                'View_Count': view_count,
                'Like_Count': like_count,
                'Dislike_Count': dislike_count,
                'Favorite_Count': favorite_count,
                'Comment_Count': comment_count,
                'Duration': duration,
                'Thumbnail': thumbnail,
                'Caption_Status': caption_status
            }
            
            videos_data.append(video_data)

    return videos_data


# Set your API key and channel ID
API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'YOUR_CHANNEL_ID'

# Call the function to extract the data
channel_data = get_channel_data(API_KEY, CHANNEL_ID)

# Print the extracted data
for video_data:

    # Insert the channel data and video data into the MongoDB database
    db = client['youtube']
    db['channels'].insert_one({
        'channel_id': channel_id,
        'channel_name': channel_data['title'],
        'subscriber_count': channel_data['subscriberCount'],
        'video_count': channel_data['videoCount'],
        'playlist_id': playlist_id
    })
    db['videos'].insert_many(video_data)

    return {
        'channel_name': channel_data['title'],
        'subscriber_count': channel_data['subscriberCount'],
        'video_count': channel_data['videoCount'],
        'playlist_id': playlist_id,
        'videos': video_data
    }




# Define the Streamlit app
def app():
    st.title("YouTube Channel Data Migration")

    # Get the channel ID from the user
    channel_id = st.text_input("Enter a YouTube Channel ID", value="UCS0N5baNlQWJCUrhCEo8WlA")

    # Retrieve and display the channel data
    if st.button("Retrieve Channel Data"):
        channel_data = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        ).execute()['items'][0]['snippet']

        st.subheader("Channel Data")
        st.write("Name:", channel_data['title'])
        st.write("Description:", channel_data['description'])
        st.write("Subscriber Count:", channel_data['subscriberCount'])
        st.write("Video Count:", channel_data['videoCount'])

        # Insert the channel data into the MongoDB database
        db = client['youtube']
        db['channels'].insert_one({
            'channel_id': channel_id,
            'channel_name': channel_data['title'],
            'subscriber_count': channel_data['subscriberCount'],
            'video_count': channel_data['videoCount']
        })

        st.success("Channel data migrated to MongoDB")

# Run the Streamlit app
if __name__ == '__main__':
    app()