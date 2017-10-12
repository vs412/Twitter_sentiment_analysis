from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import MySQLdb
import time
import json



#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("mysql.server","beginneraccount","cookies","beginneraccount$tutorial")

c = conn.cursor()

conn.set_character_set('utf8')
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;

#consumer key, consumer secret, access token, access secret.
ckey="x03DdEicjEhyGZLm2IVUdIyhN"
csecret="	fms86R3gYb3zDbm0w3WfjxqjJsT4IklT6AQghiW2as3xPsLyjG"
atoken="865054453405233153-YL43fv8gpsCEw9eXrtj7qq3bFj9tPfu"
asecret="UWOTewWLLM8Y54Ph0xkn78rQogVkfbdM5UdXH9EcmGBKj"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]

        username = all_data["user"]["screen_name"]

        c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

        conn.commit()

        print((username,tweet))

        return True

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
