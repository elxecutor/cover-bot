# x_poster.py

import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# v1.1 API for media upload
auth = tweepy.OAuth1UserHandler(
    os.getenv("X_API_KEY"),
    os.getenv("X_API_SECRET"),
    os.getenv("X_ACCESS_TOKEN"),
    os.getenv("X_ACCESS_TOKEN_SECRET")
)
api_v1 = tweepy.API(auth)

# v2 Client for tweet creation
client_v2 = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
    bearer_token=os.getenv("X_BEARER_TOKEN"),
)

def post_tweet_with_image(text: str, image_path: str):
    try:
        media = api_v1.media_upload(image_path)
        response = client_v2.create_tweet(text=text, media_ids=[media.media_id])
        tweet_id = response.data.get("id")
        username = client_v2.get_me().data.username
        print(f"✅ Tweet posted: https://x.com/{username}/status/{tweet_id}")
        return response
    except tweepy.TweepyException as e:
        print(f"❌ Tweepy error: {e}")
    except Exception as e:
        print(f"❌ General error: {e}")
    return None
