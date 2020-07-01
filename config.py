import os


class Config:

    @property
    def consumer_key(self):
        return os.environ.get("CONSUMER_KEY")

    @property
    def consumer_secret(self):
        return os.environ.get("CONSUMER_SECRET")

    @property
    def api_token(self):
        return os.environ.get("API_TOKEN")
    
    @property
    def api_secret(self):
        return os.environ.get("API_SECRET")

    @property
    def search_string(self):
        return "🍕"

    @property
    def users(self):
        return [
            "1219477123250831360",  # ME
            "18450106",   # Papa Johns
            "31444922",   # Dominos
            "459507399",  # Mountain Mike's
            "46714602",   # Papa Murphys
            "11018442",   # Pizza Hut
            "23990896",   # Round Table
            "19370018",   # CPK
            "37031807",   # Jet's Pizza
            "22983825",   # Lou Malnatis
            "161420856",  # Giordanos Pizza
            "57824414",   # Little Caesars Pizza
            "22151553",   # DiGiorno
            ]

    @property
    def slack_webhook(self):
        return os.environ.get("SLACK_WEBHOOK")


def get_config():
    return Config()