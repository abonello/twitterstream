from tweepy import Stream
from tweepy.streaming import StreamListener
from keys_and_secrets import get_auth, twitter_api


keyword_list = ['python', 'java', 'c#', 'ruby'] #track list
 
class MyStreamListener(StreamListener):
 
    def on_data(self, data):
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


auth = get_auth
 
twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)