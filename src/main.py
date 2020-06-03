import typer
import tweepy
from typing import List

creds = open("./auth.txt", "r")
twitter_credentials = creds.read().splitlines()

API_KEY = twitter_credentials[0]
API_SECRET_KEY = twitter_credentials[1]
ACCESS_TOKEN = twitter_credentials[2]
ACCESS_TOKEN_SECRET = twitter_credentials[3]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def main(tweet: List[str]):
    ret = ' '.join(tweet)
    typer.echo(ret)
    api.update_status(ret)

if __name__ == '__main__':
    typer.run(main)