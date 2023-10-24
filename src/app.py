import os
import random
import curator, constants, ai_bot, tweet

from dotenv import load_dotenv


def run(event, context):

    # Load environment variables from .env file
    load_dotenv()

    # Access environment variables
    open_ai_key = os.environ.get("OPEN_AI_API_KEY")
    consumer_key = os.environ.get("consumer_key")
    consumer_secret = os.environ.get("consumer_secret")
    access_token = os.environ.get("access_token")
    access_token_secret = os.environ.get("access_token_secret")
    bearer_token = os.environ.get("bearer_token")

    # Access news article from RSS Feed
    try:
        feed_url = random.choice(constants.FEEDS)
        feed = curator.Curator(feed_url)
        article = dict(random.choice(feed.get_content()))
    except Exception:
        print("Cannot access news article")

    # Make GPT read article and provide opinion
    bot = ai_bot.GPT_bot(open_ai_key, constants.template, constants.human_template)
    chain = bot.initialize_invocation()
    limit = 160
    response = chain.invoke({"text": article["content"], "limit": limit}).content.replace("\\", "")
    content_text = response.replace('"', "")

    # Tweet bot's opinion
    tweetor = tweet.Tweetor(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        bearer_token
    )
    tweetor.tweet(content_text)

    return {
        "statusCode": 200,
        "body": {"message": "Tweet successfull!", "feed": feed_url}
    }