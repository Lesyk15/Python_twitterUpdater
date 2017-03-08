import tweepy
from PIL import Image, ImageDraw
import os.path


# http://dev.twitter.com/apps/myappid
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
# http://dev.twitter.com/apps/myappid/my_token
ACCESS_TOKEN_KEY= ''
ACCESS_TOKEN_SECRET= ''

obrazek = ""
def tweet(status):
    '''
    updates the status of my twitter account
    requires tweepy (https://github.com/joshthecoder/tweepy)
    '''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    image = Image.open("D:/image.png")
    result = api.update_status(image)
    return result

def text2img (imgtext):
    img = Image.new('RGB', (200, 100))
    d = ImageDraw.Draw(img)
    d.text((20, 20), (str(imgtext)), fill=(255, 0, 0))
    img.save("D:/image.png")
    #obrazek = Image.open("D:/image.png")
    tweet("ahoj")
    return

text2img("Hello from python 2")


