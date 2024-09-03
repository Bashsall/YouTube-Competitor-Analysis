from googleapiclient.discovery import build

# Replace with your own YouTube Data API key
api_key = "YOUR_YOUTUBE_DATA_API_KEY"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# List of video IDs obtained from the previous step
video_ids = [
    "VIDEO_ID_1",  # Replace with actual video IDs
    "VIDEO_ID_2",  # Add more video IDs as needed
    # ...
]

# Get detailed information about each video
request = youtube.videos().list(
    part="snippet,statistics",
    id=','.join(video_ids)
)

# Execute the request and get the response
response = request.execute()

# Print out details for each video
for item in response['items']:
    title = item['snippet']['title']
    description = item['snippet']['description']
    tags = item['snippet'].get('tags', [])
    view_count = item['statistics']['viewCount']
    like_count = item['statistics'].get('likeCount', 'N/A')
    comment_count = item['statistics'].get('commentCount', 'N/A')
    
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Tags (Keywords): {', '.join(tags)}")
    print(f"Views: {view_count}, Likes: {like_count}, Comments: {comment_count}")
    print("=" * 50)
