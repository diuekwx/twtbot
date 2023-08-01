import tweepy
import keys
import requests
import shutil
import TenGiphPy


# use this to upload media ? 
def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    return tweepy.API(auth)

#client uses v2 endpoint only, required to use v1 endpoint for uploading media
client = tweepy.Client(keys.bearer, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)


t = TenGiphPy.Giphy(key)

url = t.random(tag="ghibli")['data']['images']['downsized_large']['url']

r = requests.get(url, stream=True)
r.raw.decode_content = True


with open('img.gif', 'wb') as f:
    shutil.copyfileobj(r.raw, f)

media = api().media_upload("C:/Users/jeris/OneDrive/Documents/twitterbot/cat.jpeg")
gif = api().media_upload('C:/Users/jeris/OneDrive/Documents/twitterbot/img.gif')
client.create_tweet(text = "hello my loves", media_ids=[gif.media_id])
