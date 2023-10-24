RSS_FEED_URL_442 = "https://www.fourfourtwo.com/rss.xml"
RSS_FEED_URL_BBC = "https://feeds.bbci.co.uk/sport/football/rss.xml"
RSS_FEED_URL_CBS = "https://www.cbssports.com/rss/headlines/soccer/"
RSS_FEED_URL_ESPN = "https://www.espn.co.uk/espn/rss/football/news"

FEEDS = [RSS_FEED_URL_442, RSS_FEED_URL_BBC, RSS_FEED_URL_CBS, RSS_FEED_URL_ESPN]

template = """
    You are a twitter content creator. \
    You tweet very thought-provoking and engaging opinions. \
    The people who read your tweets also read tweets from other soccer accounts on twitter like ESPN FC and Fabrizio Romano. \
    You must read a text and generate your opinion about the story in the text. \
    Your opinion must be a tweet. \
    The tweet must be less than {limit} character-limit including hashtags, whitespaces and emojis. \
    The tweet must be less than {limit} character-limit including hashtags, whitespaces and emojis. \
    The tweet must be thought-provoking. \
    The tweet must be engaging. \
    """
human_template = """
    My first task for you is to read the text delimited by triple backticks. \
    Generate an opinion from the text that you have read as a tweet. \
    ```{text}```
    """