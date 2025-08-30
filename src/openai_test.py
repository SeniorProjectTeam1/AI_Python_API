import os
from dotenv import load_dotenv
from openai import OpenAI
from enum import StrEnum

load_dotenv()

API_KEY = os.getenv('API_KEY')
ROLE = "user"
CONTENT = "This is a test message respond by saying 'Hi this is a test at: ' and the date down to the second."

class SupportedModels(StrEnum):
    """Enum class for supported models within AI Class"""
    GPT4_O= "gpt-4o",
    GPT4_MINI = "gpt-4o-mini",
    GPT4_TURBO="gpt-4-turbo",
    GPT4 = "gpt-4",
    GPT3_TURBO = "gpt-3.5-turbo",

class AI:
    """This class object contains the following variables
    -api_key
    -model
    -role
    -content
    -store 
    
    """
    def __init__(self,api_key:str = API_KEY ,model:SupportedModels = SupportedModels.GPT4_MINI, role:str = ROLE, content:str = CONTENT, store:bool = True):
        
        self.selected_model = model
        self.role = role
        self.content = content
        self.store = store
    
    def get_model(self):
        return self.model
    
    def set_model(self, new_model):
        self.model = new_model    
        
    def get_role(self):
        return self.role
    
    def set_role(self, new_role):
        self.role = new_role 
        
    def get_api_key(self):
        return self.api_key
    
    def set_api_key(self, new_api_key):
        self.api_key = new_api_key 
        
    def toggle_store(self):
        self.store = not self.store
        return self.store
    
    def set_message(self, message:str):
        self.content = message
    
    def get_response(self):
        """return a message based on class variables"""
        client = OpenAI(api_key=API_KEY)

        response = client.chat.completions.create(
        model=self.selected_model,
        messages=[{"role": str(self.role), "content": str(self.content)}],
        store=True,   
        )

        return response.choices[0].message.content


#Example useage of the the class objects
if __name__ == "__main__":
    gpt = AI()
    gpt.set_message("Tell me 3 computer engineering project idea for 500 dollars that has a 40 percent innovative and has to do with a oxygen reader for astmah using iot, embedded design, and electronic design.")
    print(gpt.get_response())