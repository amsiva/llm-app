from pydantic import BaseModel, Field
from typing import Literal
from commons import client_connection

class Feedback(BaseModel):
    product:str = Field(description="Name of the product")
    name:str = Field(description="Name of the user")
    email:str = Field(description="Email of the user")
    rating:Literal[1,2,3,4,5] = Field(description="Rating of the user")
    feeback:Literal["positive","negative"] = Field(description="Feedback of the user")


client = client_connection()

response = client.messages.create(
    model='claude-haiku-4-5',
    system="AI to identify the feedback of the user",
    messages=[{"role": "user", "content": "I am Sivakumar Selvaraj recently purchased iphone 15 pro max and I am extremely unsatisfied with its performance. "
    "The camera quality is exceptional, but the battery life lasts within a day. "
    "The design is sleek and feels premium in hand. Overall, it's a device that doesn't meet my expectations. "
    "i will definitely say its 1 stars out of 5 and i can't buy more products from this brand using abc@gmail.com"}],
    max_tokens=1000,
    tools=[{"name": "feedback", 
            "description": "A tool to identify the feedback of the user", 
            "input_schema": Feedback.model_json_schema()}],

    tool_choice={"name": "feedback", "type": "tool"},
)

print(response)