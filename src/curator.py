import newspaper
import feedparser

class Curator:
    def __init__(self, feed_url):
        self.articles = []
        self.feed_url = feed_url
        self.size = 10

    def collect_articles(self):
        feed = feedparser.parse(self.feed_url)
        return feed.entries

    def get_content(self):
        feed_entries = self.collect_articles()
        count = 0
        for entry in feed_entries:
            article = newspaper.Article(entry.link)
            # download and parse the article
            article.download()
            article.parse()
            #append the article to our list of articles
            if article.text and (count < self.size):
                self.articles.append({
                    'title': article.title,
                    'content': article.text.replace("\n", ""),
                    'publish_date': article.publish_date,
                })
                count += 1

        return self.articles