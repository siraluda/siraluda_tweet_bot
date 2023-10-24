# GPT-4 Content Creator
This is a content creator application powered by OpenAI's GPT-4. The application reads football/soccer related news articles and automatically generates a tweet based on the article.

### Application Infrastructure
<img src="images/X-bot%20application%20Infrastructure.png" alt="drawing" width="500"/>

### Approach to building this bot
- Curate news articles from an authoritative source via their RSS Feed.
- Randomly choose an article and feed it to the gpt-4 api.
- Use a prompt to instruct gpt-4 to read the article and generate a tweet based on the article.
- Use the X/twitter api to tweet the generated tweet.

### Tools and Resources
- Python for application code
- LangChain for GPT-4 Api
- Twitter Api for tweeting
- Terraform for AWS infrastructure

### What to do
If you want to reproduce or further develop this application, here are a few things to do:
- Create an account with [OpenAI](https://openai.com/) to generate API keys
- Create an account on X (twitter), go to the twitter developer [portal](https://developer.twitter.com/en/portal/dashboard) and generate API keys. Make sure api keys have read and write permissions.
- Create a `.env` file in the `src/` directory with the following variables:
    ```
    OPEN_AI_API_KEY= <From OpenAI>
    consumer_key= <From X/twitter>
    consumer_secret= <From X/twitter>
    access_token= <From X/twitter>
    access_token_secret= <From X/twitter>
    bearer_token= <From X/twitter>
    ```
- If you want to deploy this application using the terraform code in `/infrastructure` you have to install and configure aws cli. NOTE: I already had Amazon ECS configured so i did not add it to the terraform code. You can follow this [guide](https://docs.aws.amazon.com/AmazonECS/latest/userguide/create-container-image.html) on how to create a container image on ECS.

