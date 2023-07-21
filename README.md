# add-reddit-comments-to-twitter

Post comments you've saved in Reddit to Twitter as tweets.

# Overview

When reading Reddit, I often save comments that resonate with me. What else to do with all these saved comments but share them with the world via Twitter? This app will take one comment from your saved comments, post it as a tweet with a link back to the comment, then remove it from your saved comments.

# Dependencies

This app uses Praw to integrate with Reddit and Tweepy to integrate with Twitter.

# Running

The Python file takes 9 parameters.
- Praw client ID
- Praw client secret
- Praw password
- Praw user agent
- Praw username
- Tweepy consumer key
- Tweepy consumer secret
- Tweepy access token
- Tweepy access token secret

```
git clone https://github.com/drewmrobson/add-reddit-comments-to-twitter.git
cd add-reddit-comments-to-twitter
python main.py <praw client id> <praw client secret> <praw password> <praw user agent> <praw username> <tweepy consumer key> <tweepy consumer secret> <tweepy access token> <tweepy access token secret>
```
