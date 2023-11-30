import os
import openai
from chatgpt_automation import ChatGPT_Client

chatgpt = ChatGPT_Client("mfinixone@gmail.com", "hamouza2212")

usr_content ="""
How do you find inner peace and contentment, especially in challenging times?
""".strip()

sys_content = f"""
You are a very wise old man you use little words but have deep meaning, your goal is to help user with your wise pretious words:
example:
user_input: tell me about sports
answer: Uniting hearts, testing limits, fostering growth. Play, learn, embrace.

user_input: {usr_content}
""".strip()

answer = chatgpt.interact(sys_content)
print(answer)
