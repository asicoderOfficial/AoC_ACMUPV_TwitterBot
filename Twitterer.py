import tweepy


CONSUMER_KEY = "TuAXDUsCuKgOFnkqhHvBPgAu5"
CONSUMER_SECRET = "HZdDZK6O4FISImOCDwyPVvNkNB1YUzUEyngTPv6aeu7iWd9zb0"
ACCESS_KEY = "1233058749927100416-tote23vM5O6Nj4XhXzAC3G7SXRiB6X"
ACCESS_SECRET = "UXjcEVqCVGtfxnM6thOD3FW6u0NgfQdqapabTV9wE9mUc"
BOT_ID = "@AdventOfCodeAC1"

def leaderboard_tweet():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    api.update_status("Hello, make a response NOW (please).")
    api.update_status("{} Response made, NOW MOTHERFUCKER yeah!".format(BOT_ID))