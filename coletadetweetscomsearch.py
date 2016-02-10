import tweepy

consumer_key="suachave"
consumer_secret="suachave"
access_token="suachave"
access_token_secret="suachave"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

criterio = "#justinbieber"

tweets = api.search(criterio)

i = 1
while tweets:
	print("\nEncontrei %d tweets\n" % (len(tweets)))

	for tweet in tweets:
		# print(i,",",tweet.id,",","\"",tweet.text,"\"")
		print("%d,%d,\"%s\"" % (i,tweet.id,tweet.text))
		i = i + 1
		last_id = tweet.id

	tweets = api.search(criterio, max_id=last_id-1)