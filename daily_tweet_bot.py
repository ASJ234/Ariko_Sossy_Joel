import os
import tweepy
from datetime import datetime
import schedule
import time

# Twitter API credentials (hardcoded from codes.env)
api_key = "focZYUIqcR6iwdgFwl9kn5mXm"
api_secret = "bBGHMn7Pl2TQ7XrnLZsSyIJ8UEpIZzOOSgZtB9mrf7bU7E17Jp"
access_token = "1623395378077831169-Ze3EAElkwBQUK4b89rCQuAnMGLnc7e"
access_secret = "1i6p1iSt4ZUMo77v0IKMUq5uiJMyyj1ifyJGLF3SlBkTv"

# Daily messages
messages = [
    "Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday Thoughts: Keep pushing forward—progress is progress, no matter how small! #TuesdayThoughts",
    "Wednesday Wisdom: The only limit to our realization of tomorrow is our doubts of today. #WednesdayWisdom",
    "Thursday Thoughts: Take a moment to reflect on your goals and progress. #ThursdayThoughts",
    "Friday Fun: It's almost the weekend! What are your plans? #FridayFun",
    "Saturday Spotlight: Highlighting our amazing community members! #SaturdaySpotlight",
    "Sunday Reflections: A time to relax and recharge for the week ahead. #SundayReflections"
]

# Function to post to Twitter
def post_to_twitter():
    # Get current weekday index: 0 = Monday, 6 = Sunday
    today_index = datetime.today().weekday()
    tweet_message = messages[today_index]
    
    try:
        # Initialize Tweepy v2 Client
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_secret
        )
        # Post tweet using v2 API
        response = client.create_tweet(text=tweet_message)
        print(f"✅ Tweeted at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {tweet_message}")
        return response
    except tweepy.TweepyException as e:
        print(f"❌ Error posting tweet at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {e}")
        raise

# Schedule the tweet to run daily at a specific time (e.g., 12:00 PM EAT)
schedule.every().day.at("12:00").do(post_to_twitter)

if __name__ == "__main__":
    post_to_twitter()