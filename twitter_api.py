import ConfigParser
from rauth import OAuth1Session
from rauth import OAuth1Service
import json
import sys, codecs


class twitter_api:

    def init(self):
        inifile = ConfigParser.SafeConfigParser()
        inifile.read("./twitter_config.ini")
        self.consumer_key=inifile.get("twitter_app_config","consumer_key")
        self.consumer_secret=inifile.get("twitter_app_config","consumer_secret")
        self.access_token=inifile.get("twitter_app_config","access_token")
        self.access_token_secret=inifile.get("twitter_app_config","access_token_secret")


    def post_tweet(self,tweet_message):
        self.init()

        params = {"status": str(tweet_message)}
        oauth_settion = OAuth1Session(
                                self.consumer_key,
                                self.consumer_secret,
                                self.access_token,
                                self.access_token_secret)

        post_url="https://api.twitter.com/1.1/statuses/update.json"

        request = oauth_settion.post(post_url,params)

        if request.status_code == 200:
                print ("OK")
        else:
            print ("Error: %d" % request.status_code)


#obj =twitter_api()
#obj.post_tweet("test")
