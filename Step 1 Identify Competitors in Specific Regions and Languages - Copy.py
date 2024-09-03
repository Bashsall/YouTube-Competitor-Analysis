from googleapiclient.discovery import build

# Replace with your own YouTube Data API key
api_key = "YOUR_YOUTUBE_DATA_API_KEY"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for popular videos based on keywords, region, and language
request = youtube.search().list(
    q="YOUR_KEYWORDS",  # Replace with relevant keywords for your niche
    part="snippet",
    regionCode="YOUR_REGION_CODE",  # e.g., 'US' for United States, 'IN' for India
    relevanceLanguage="YOUR_LANGUAGE_CODE",  # e.g., 'en' for English, 'es' for Spanish
    type="video",
    maxResults=10  # You can adjust this number to get more results
)

# Execute the request and get the response
response = request.execute()

# Print out the results
for item in response['items']:
    print(f"Title: {item['snippet']['title']}, Channel: {item['snippet']['channelTitle']}, Video ID: {item['id']['videoId']}")
