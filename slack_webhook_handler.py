import requests

from log_handler import get_logger
from config import get_config


logger = get_logger(__name__)


def send_webhook(status):
    """ Send a webhook into Slack
    :param: username - The username of the account that posted the tweet
    :param: status_text - The body of the webhook message.
    """
    message_body = f"""
    <https://twitter.com/{status.user.screen_name}|@{status.user.screen_name}> tweeted:
    ```{status.text}```
    <https://twitter.com/{status.user.screen_name}/status/{status.id}|Link to full Tweet!>
    """
    payload = {
        "username": "Pizza Delivery",
        "icon_emoji": ":pizza:",
        "text": message_body
    }
    resp = requests.post(get_config().slack_webhook, json=payload)
    logger.info(resp.status_code)
