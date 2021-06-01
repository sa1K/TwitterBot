import spotipy
import SpotAuth

CLIENT_ID = SpotAuth.clientID
CLIENT_SECRET = SpotAuth.clientSecret
username = SpotAuth.username
scope = "user-read-currently-playing"
redirect_uri = SpotAuth.redirect_uri
sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=redirect_uri,
                                       scope=scope)
token_info = sp_oauth.get_cached_token()


def getSong():
    #gets the token from the cache if it exists
    token_info = sp_oauth.get_cached_token()
    #if it doesn't exist get the token
    if not token_info:
        auth_url = sp_oauth.get_authorize_url(state=True)
        print(auth_url)
        response = input('Paste the above link into your browser, then paste the redirect url here: ')

        code = sp_oauth.parse_response_code(response)
        token_info = sp_oauth.get_access_token(code)

        token = token_info['access_token']
        # For future versions: token=token_info
    else:
        token = token_info['access_token']
        # For future versions: token=token_info

    #access the spotify api
    sp = spotipy.Spotify(auth=token)
    try:
        #gets the current song
        current_song = sp.currently_playing()
        song_name = current_song['item']['name']
        i=0
        allArtists=[]
        #gets all the artisits on the song
        while True:
            try:
                allArtists.append(current_song['item']['artists'][i]['name'])
                i=i+1
            except IndexError:
                break
        joined_string = ", ".join(allArtists)
        #returns what is being played and who is the artist
        to_return = "Now playing \"" + song_name + "\" by " + joined_string
        return to_return
    #handles nothing being played
    except TypeError:
        print("Nothing is playing")
        return False

