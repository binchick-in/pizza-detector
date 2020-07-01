from tweepy import OAuthHandler
from tweepy import TweepError

from config import get_config
from log_handler import get_logger


logger = get_logger(__name__)
CONSUMER_KEY = get_config().consumer_key
CONSUMER_SECRET = get_config().consumer_secret
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

try:
    redirect_url = auth.get_authorization_url()
    print(f"Go here, get the code => {redirect_url}")
    verification_code = input("Verification Code: ")
    auth.request_token.update({"oauth_token_secret" : verification_code})
    auth.get_access_token(verification_code)
    print("---")
    print(f"Access Token => {auth.access_token}")
    print(f"Secret Token => {auth.access_token_secret}")
    print("---")
except TweepError as e:
    print("Unable to continue...")
    logger.error(e)




