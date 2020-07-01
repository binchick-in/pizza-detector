# Pizza Delivery

A simple project that will detect when myself or various pizza companies tweet a pizza emoji (🍕) and post that to Slack via a webhook.

The Twitter Streaming API is used to establish a feed listener, ingest incoming tweets from the listed companies in the config, and determine if those tweet contain the pizza emoji. If the tweet does, it will create a payload for Slack's webhook and send it alone to the Slack channel.

Companies this project will listen to (in addition to my own feed)
* Papa Johns
* Dominos
* Mountain Mike's
* Papa Murphy's
* Pizza Hut
* Round Table
* California Pizza Kitchen
* Jet's Pizza
* Lou Malnati's
* Giordanos Pizza
* Little Caesars Pizza
* DiGiorno

This is currently running on my personal dev server and will deliver notifications to #pizza in Slack.

To use with your own Twitter developer account, create a `start.sh` file and fill in the values.

If you don't have `API_TOKEN` or `API_SECRET`, run `register_app.py` with your consumer keys to get a fresh set of API Tokens.

```
#!/bin/sh
echo "Starting..."
export CONSUMER_KEY=""
export CONSUMER_SECRET=""
export API_TOKEN=""
export API_SECRET=""
export SLACK_WEBHOOK=""
/usr/bin/python3 /code/main.py
```