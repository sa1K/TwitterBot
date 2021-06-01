# importing the module
import tweepy
import auth
import Spotify

def main(message):
    # authentication of consumer key and secret
    authorization = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)

    # authentication of access token and secret
    authorization.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(authorization)

    # update the status
    api.update_status(status=message)

if __name__ == "__main__":
    message=""
    while True:
        oldMess=message
        message=Spotify.getSong()
        if(message!=oldMess):
            main(message)