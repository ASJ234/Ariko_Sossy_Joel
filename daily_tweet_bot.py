import os
import tweepy
from datetime import datetime
from dotenv import load_dotenv
import schedule
import time

# Load the specific .env file
load_dotenv(dotenv_path="codes.env")

# Twitter API credentials
api_key = os.getenv("TWITTER_API_KEY")
api_secret = os.getenv("TWITTER_API_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret = os.getenv("TWITTER_ACCESS_SECRET")

# Daily messages
messages = [
    "Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday Tips: Did you know that staying hydrated can boost your productivity? #TuesdayTips",
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
    print("Starting Twitter bot scheduler...")
    # Run the scheduler in an infinite loop
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait 60 seconds before checking again