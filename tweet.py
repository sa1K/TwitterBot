# importing the module
import tweepy
import auth

def main(message):
    # authentication of consumer key and secret
    authorization = tweepy.OAuthHandler(auth.consumer_key, auth.consumer_secret)

    # authentication of access token and secret
    authorization.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(authorization)

    # update the status
    api.update_status(status=message)

if __name__ == "__main__":
    temp=True
    while temp==True:
        message=input("Enter message here (type done to finish tweeting): ")
        if len(message)>279:
            print("too long try again")
        elif message=="done":
            print("done tweeting")
            temp=False
        else:
            main(message)