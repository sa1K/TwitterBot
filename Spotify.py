import spotipy
import SpotAuth


CLIENT_ID = SpotAuth.clientID
CLIENT_SECRET = SpotAuth.clientSecret
username = SpotAuth.username
scope = "user-read-currently-playing"
redirect_uri = SpotAuth.redirect_uri
sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=redirect_uri,scope=scope)
token_info = sp_oauth.get_cached_token()
if not token_info:
    auth_url = sp_oauth.get_authorize_url(state=True)
    print(auth_url)
    response = input('Paste the above link into your browser, then paste the redirect url here: ')

    code = sp_oauth.parse_response_code(response)
    token_info = sp_oauth.get_access_token(code)

    token = token_info['access_token']
    #For future versions: token=token_info
else:
    token=token_info['access_token']
    #For future versions: token=token_info

sp = spotipy.Spotify(auth=token)

currentsong = sp.currently_playing()
song_name = currentsong['item']['name']
song_artist = currentsong['item']['artists'][0]['name']
print("Now playing "+ song_name+" by "+ song_artist )


