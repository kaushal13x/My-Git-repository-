import tweepy

# Your credentials from Twitter Developer Portal
API_KEY = "1942506142552530944For98x"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Your tweet message
tweet = "🚀 Posting this tweet using Python and Tweepy! #python #twitterapi"

# Post the tweet
try:
    api.update_status(tweet)
    print("✅ Tweet posted successfully!")
except Exception as e:
    print("❌ Failed to post tweet:", e)
