from tweepy import StreamListener
from slack_webhook_handler import send_webhook
from log_handler import get_logger
from config import get_config


logger = get_logger(__name__)


class PizzaStream(StreamListener):

    def on_status(self, status):
        if get_config().search_string in status.text:
            logger.info(f"User: @{status.user.screen_name} => {status.text}")
            send_webhook(status)
        return True

    def on_error(self, status_code):
        logger.error(status_code)
        return False


