from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

ckey="x03DdEicjEhyGZLm2IVUdIyhN"
csecret="	fms86R3gYb3zDbm0w3WfjxqjJsT4IklT6AQghiW2as3xPsLyjG"
atoken="865054453405233153-YL43fv8gpsCEw9eXrtj7qq3bFj9tPfu"
asecret="UWOTewWLLM8Y54Ph0xkn78rQogVkfbdM5UdXH9EcmGBKj"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
        	output = open("twitter-out.txt","a")
        	output.write(sentiment_value)
        	output.write('\n')
        	output.close()

        return True

        def on_error(self, status):
            print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])