import sys
import praw
import tweepy

# Configure praw

client_id = sys.argv[1]
print(client_id)

client_secret = sys.argv[2]
print(client_secret)

password = sys.argv[3]
print(password)

user_agent = sys.argv[4]
print(user_agent)

username = sys.argv[5]
print(username)

# Configure tweepy

consumer_key = sys.argv[6]
print(consumer_key)

consumer_secret = sys.argv[7]
print(consumer_secret)

access_token = sys.argv[8]
print(access_token)

access_token_secret = sys.argv[9]
print(access_token_secret)

# Init praw
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password=password,
    user_agent=user_agent,
    username=username,
)

# Init tweepy
client = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

# Get Reddit comments
saved_comments = reddit.user.me().saved(limit=None)

# Send one saved comment as tweet then unsave it
for saved in saved_comments:
    if type(saved) is praw.models.Comment:
        composed = f'{saved.body} [Source](https://www.reddit.com{saved.permalink})'
        
        if len(composed) < 280:
            print(composed)
            response = client.create_tweet(
                text=composed
            )
            print(f"https://twitter.com/user/status/{response.data['id']}")
            saved.unsave()
            break