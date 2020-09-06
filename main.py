import tweepy
from creds import *
from lists import reporters, memers

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

def checkCreeper(m):
    print(m)
    test = api.lookup_friendships([m],reporters)
    for r in test:
        result = r.name
        if (r.is_followed_by == True):
            result = result + ": Yes"
        else:
            result = result + ": No"
        print(result)
    print("------------------------------------------------------------")


for m in memers:
    checkCreeper(m)
print("End of Report")
