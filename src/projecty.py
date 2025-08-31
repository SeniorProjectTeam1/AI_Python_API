import os
from dotenv import load_dotenv
from openai import OpenAI
from supported_models import SupportedModels
from loader import Loader
from threading import Thread

load_dotenv()

API_KEY = os.getenv("API_KEY")
ROLE = "user"
CONTENT = "This is a test message respond by saying 'Hi this is a test at: ' and the date down to the second."


class AI:
    """This class object contains the following variables
    -api_key
    -model
    -role
    -content
    -store

    """

    def __init__(
        self,
        api_key: str = API_KEY,
        model: SupportedModels = SupportedModels.GPT4_MINI,
        role: str = ROLE,
        content: str = CONTENT,
        store: bool = True,
    ):
        self.api_key = api_key
        self.selected_model = model
        self.role = role
        self.content = content
        self.store = store

    def get_model(self):
        """Gets the currently selected model.

        Returns:
            SupportedModels: A StrEnum class of supported models
        """
        return self.selected_model

    def set_model(self, new_model):
        """Sets the currently selected model.

        Args:
            new_model (SupportedModels): The newly selected model from the StrEnum class of supported models
        """
        self.selected_model = new_model

    def get_role(self):
        """Gets the currently selected role to be used during prompt generation.

        Returns:
            Str: A str with the role (user, developer, etc).
        """
        return self.role

    def set_role(self, new_role):
        """Sets the currently selected role to be used during prompt generation.

        Args:
            new_role (Str): The newly selected role.
        """
        self.role = new_role

    def get_api_key(self):
        """Gets the API key currently selected for the AI object.

        Returns:
            Str: A str which represents the API Key selected.
        """
        return self.api_key

    def set_api_key(self, new_api_key):
        """Sets the API key currently selected for the AI object.

        Args:
            new_api_key (Str): A str which represents the API Key.
        """
        self.api_key = new_api_key

    def toggle_store(self):
        """A bool command which toggles the store variable within openai.

        Returns:
            bool: The current state of the store attribute.
        """
        self.store = not self.store
        return self.store

    # TODO change message to be a str or some schema to aid in a skeleton for prompt gen.
    def set_message(self, message: str):
        """Sets the message or messages to be sent to the selected AI model.

        Args:
            message (str): The message(s) to be sent within the prompt.
        """
        self.content = message

    def get_response(self):
        """return a message based on class variables"""
        client = OpenAI(api_key=self.api_key)
        loading = Loader()
        loading.start()
        response = client.chat.completions.create(
            model=self.selected_model,
            messages=[{"role": str(self.role), "content": str(self.content)}],
            store=True,
        )
        loading.stop()
        loading.join()
        return response.choices[0].message.content
