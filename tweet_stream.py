from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from keys_and_secrets import get_auth, twitter_api


#keyword_list = ['python', 'java', 'c#', 'ruby'] #track list
keyword_list = ['brexit']
 
class MyStreamListener(StreamListener):
 
    def on_data(self, data):
        print "on_data is called"
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True
 
    def on_error(self, status):
        print status
        return True

#api = twitter_api()
auth = get_auth()

print " About to create a child class of StreamListener"
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)