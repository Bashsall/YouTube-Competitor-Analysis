from googleapiclient.discovery import build
from collections import Counter

# Replace with your own YouTube Data API key
api_key = "AIzaSyBokIO83StHfMBnrHaw4ISlTRKy_atHsy4"

# Create a YouTube API client
youtube = build('youtube', 'v3', developerKey=api_key)

# Define thresholds for channel sizes (adjust these numbers as needed)
large_channel_threshold = 1000000  # 1 million subscribers or more
medium_channel_threshold = 100000  # Between 100,000 and 1 million subscribers

# List of keywords to analyze
keywords = ["cryptocurrency", "crypto", "altcoin", "altcoin daily", "news", "best investment", "top altcoins", "best crypto investment", "ethereum", "xrp", "crash", "bottom", "price", "prediction", "interview", "finance", "investment", "too late", "bitcoin", "cryptocurrency news", "bitcoin news", "cryptocurrency news media online", "best crypto investments", "coin bureau", "binance", "coinbase", "trade", "make money", "cryptosrus", "bitcoin today", "bitcoin cnbc", "altcoin news", "housing market", "how much to buy a home", "house", ".01 bitcoin", ".001 bitcoin", "Peter Dunworth", "altcoins", "trading altcoins", "crypto", "cryptocurrency", "bitcoin", "crypto news", "bitcoin news", "altcoin news", "bitcoin price", "crypto trading for beginners", "crypto trading strategies", "crypto market", "crypto market update", "bitcoin today", "bitcoin technical analysis", "btc technical analysis", "best altcoins", "best crypto", "top altcoins", "bitcoin price target", "bitcoin target", "btc price target", "crypto banter", "kyledoops", "kyle doops", "where to learn crypto trading for free", "is the btc pi cycle top in", "crypto", "bitcoin", "ethereum", "Bitcoin", "Ethereum", "Solana"]  # Replace with actual keywords

# Function to classify channels by size
def classify_channel(subscriber_count):
    if subscriber_count >= large_channel_threshold:
        return "Large"
    elif subscriber_count >= medium_channel_threshold:
        return "Medium"
    else:
        return "Small"

# Analyze keyword difficulty
keyword_difficulty = {}

for keyword in keywords:
    print(f"Analyzing keyword: {keyword}")
    
    # Search for videos using the keyword
    request = youtube.search().list(
        q=keyword,
        part="snippet",
        type="video",
        maxResults=10  # Adjust this number to analyze more videos
    )
    response = request.execute()
    
    # Track the size of channels using this keyword
    channel_sizes = {"Large": 0, "Medium": 0, "Small": 0}
    
    for item in response['items']:
        channel_id = item['snippet']['channelId']
        
        # Get channel details
        channel_request = youtube.channels().list(
            part="statistics",
            id=channel_id
        )
        channel_response = channel_request.execute()
        channel_info = channel_response['items'][0]['statistics']
        
        subscriber_count = int(channel_info.get('subscriberCount', 0))
        channel_size = classify_channel(subscriber_count)
        channel_sizes[channel_size] += 1
    
    keyword_difficulty[keyword] = channel_sizes

# Calculate and print difficulty rankings
for keyword, sizes in keyword_difficulty.items():
    large = sizes["Large"]
    medium = sizes["Medium"]
    small = sizes["Small"]
    
    if large > medium + small:
        difficulty = "Hard"
    elif medium > large + small:
        difficulty = "Medium"
    else:
        difficulty = "Low"
    
    print(f"Keyword: {keyword}")
    print(f"Difficulty: {difficulty} (Large: {large}, Medium: {medium}, Small: {small})")
    print("=" * 50)
