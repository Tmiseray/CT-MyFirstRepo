
# Exercise 4: Social Media Sentiment Analysis
"""
Objective:
Develop a Python script to perform basic sentiment analysis on social media comments, categorizing them as positive, negative, or neutral based on specific keywords using regex.

Problem Statement:
You're working on a project that involves analyzing social media comments to gauge public sentiment. The task is to automatically categorize each comment as positive, negative, or neutral based on the presence of certain keywords indicative of the sentiment.

Instructions:
1. Utilize a predefined list of social media comments for analysis.
2. Create regex patterns for positive, negative, and neutral keywords or phrases.
3. Analyze each comment and categorize it according to the identified sentiment.
4. Handle exceptions or edge cases in the categorization process.
5. Output the categorized comments, showing the distribution of sentiments.

Hints:
- Define separate regex patterns for positive, negative, and neutral sentiments.
- Use a loop to process each comment, applying regex to identify the sentiment.
- Store the categorized comments in a dictionary or separate lists.
- Implement try-except blocks for handling ambiguous or unclear comments.

"""

import re

def analyze_sentiment(comment):
    positive_pattern = r"\b(thank|love|happy|great|excellent|good)\b"
    negative_pattern = r"\b(hate|angry|bad|terrible|poor|worst)\b"
    try:
        if re.search(positive_pattern, comment, re.IGNORECASE):
            return "Positive"
        elif re.search(negative_pattern, comment, re.IGNORECASE):
            return "Negative"
        else:
            return "Neutral"
    except Exception as e:
        print(f"Error analyzing comment: {e}")
        return  "Neutral"

comments = [
    "I love this product!", 
    "Terrible service, I'm angry.", 
    "Not sure about the quality.", 
    "Excellent customer support, thank you!", 
    "Worst experience ever."
]

# Categorize comments
sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
for comment in comments:
    sentiment = analyze_sentiment(comment)
    sentiment_count[sentiment] += 1

# Displaying categorized sentiments
for sentiment, count in sentiment_count.items():
    print(f"{sentiment} Comments: {count}")