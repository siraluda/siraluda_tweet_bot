from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate


class GPT_bot:
    def __init__(self, open_ai_key, template, human_template) -> None:
        self.template = template
        self.human_template = human_template
        self.open_ai_key = open_ai_key

    def _get_chat_prompt(self):
        chat_prompt = ChatPromptTemplate.from_messages(
            [("system", self.template), ("human", self.human_template)]
        )
        return chat_prompt

    def initialize_invocation(self):
        _prompt = self._get_chat_prompt()

        chat_bot = ChatOpenAI(
            openai_api_key=self.open_ai_key,
            model="gpt-4",
            temperature=0.9,
        )
        return _prompt | chat_bot
