from collections import Counter
import matplotlib.pyplot as plt

# Sample list of tags from the videos
tags_list = [
    ["keyword1", "keyword2", "keyword3"],  # Replace with actual tags from video 1
    ["keyword2", "keyword4", "keyword5"],  # Replace with actual tags from video 2
    # Add more tag lists from other videos
]

# Flatten the list of lists into a single list of keywords
all_keywords = [keyword for tags in tags_list for keyword in tags]

# Count the frequency of each keyword
keyword_counts = Counter(all_keywords)

# Print the most common keywords
print("Most common keywords:")
for keyword, count in keyword_counts.most_common():
    print(f"{keyword}: {count} times")

# Optional: Plot the keyword frequency distribution
top_n = 10  # Adjust this number to show more or fewer keywords
most_common_keywords = keyword_counts.most_common(top_n)
keywords, counts = zip(*most_common_keywords)

plt.figure(figsize=(10, 5))
plt.bar(keywords, counts, color='blue')
plt.xlabel('Keywords')
plt.ylabel('Frequency')
plt.title('Top Keywords Used by Competitors')
plt.xticks(rotation=45)
plt.show()
