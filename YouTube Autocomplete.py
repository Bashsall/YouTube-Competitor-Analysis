import requests

def get_youtube_autocomplete_suggestions(query, num_suggestions=20, region='US'):
    # Modified URL to include region
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={query}&num={num_suggestions}&gl={region}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        json_response = response.json()
        
        if isinstance(json_response, list) and len(json_response) > 1:
            suggestions = json_response[1]
            return suggestions
        else:
            print("Unexpected JSON structure.")
            print(f"Received: {json_response}")
            return []
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []
    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        print(f"Response content: {response.text}")
        return []

def print_suggestions(suggestions, query, region):
    if suggestions:
        print(f"Keyword Suggestions for '{query}' in region '{region}' ({len(suggestions)} results):")
        for i, suggestion in enumerate(suggestions, 1):
            print(f"{i}. {suggestion}")
    else:
        print(f"No suggestions found for '{query}' in region '{region}' or there was an error.")

# YouTube autocomplete request
query = "crypto trading"
num_suggestions = 20  # You can adjust this number
region = 'IN'  # You can change this to test different regions

print(f"\nFetching up to {num_suggestions} suggestions for: '{query}' in region '{region}'")
suggestions = get_youtube_autocomplete_suggestions(query, num_suggestions, region)
print_suggestions(suggestions, query, region)

# Test with a different region
region = 'GB'  # Great Britain
print(f"\nFetching up to {num_suggestions} suggestions for: '{query}' in region '{region}'")
suggestions = get_youtube_autocomplete_suggestions(query, num_suggestions, region)
print_suggestions(suggestions, query, region)

# Test with a different region
region = 'US'  # Great Britain
print(f"\nFetching up to {num_suggestions} suggestions for: '{query}' in region '{region}'")
suggestions = get_youtube_autocomplete_suggestions(query, num_suggestions, region)
print_suggestions(suggestions, query, region)