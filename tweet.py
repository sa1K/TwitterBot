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
    message = ""
    while True:
        oldMess = message
        message = Spotify.getSong()
        if (message == False):
            break
        elif (message != oldMess):
            try:
                print(message)
                main(message)
            except tweepy.error.TweepError as e:
                if e.api_code==187:
                    print("this was the same song that you were playing last time you ran the program")
                else:
                    raise e
