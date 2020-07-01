from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
from tweepy import TweepError

from config import get_config
from stream_listener import PizzaStream

auth = OAuthHandler(get_config().consumer_key, get_config().consumer_secret)
auth.set_access_token(get_config().api_token, get_config().api_secret)
api = API(auth)

pizza_stream_listener = PizzaStream()
pizza_stream = Stream(auth=api.auth, listener=pizza_stream_listener)


if __name__ == "__main__":
    try:
        pizza_stream.filter(follow=get_config().users)
    except KeyboardInterrupt:
        print("Stream Was Cut!")


