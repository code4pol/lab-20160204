import tweepy

class MyStreamListener(tweepy.StreamListener):

	def on_connect(self):
		print("\nConectou!!!\n")


	def on_data(self, data):
		print("\n",data)
		# print("%d,\"%s\"" % (data.id,data.text))

# consumer_key="suachave"
# consumer_secret="suachave"
# access_token="suachave"
# access_token_secret="suachave"

consumer_key="BZcGMGJTDGrpdVcZioyy2XeXQ"
consumer_secret="VRHcRLtGcKwVulTnfU7q9X2qDY006IOWBJOvvPjs23X2Ovocv6"
access_token="14147108-ooP2hAhZPXEOX6j6HoqE4sf3lg9nQ7Rke6fiOvHEx"
access_token_secret="I7WHX4FyNTuZ0MjPmoXyTHQFkFlcI0Eb4jbYG5cgR2YdV"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

criterio = "#justinbieber"

# Definindo a via pela qual trafegam os tweets
stream = tweepy.Stream(auth=api.auth, listener=MyStreamListener())

# Declarando os tweets do meu interesse
stream.filter(track=[criterio])