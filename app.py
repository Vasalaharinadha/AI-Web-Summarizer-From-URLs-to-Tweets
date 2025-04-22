from dotenv import load_dotenv
import os
load_dotenv()


from SimplerLLM.language.llm import LLM, LLMProvider
from SimplerLLM.tools.generic_loader import load_content

llm_instance = LLM.create(provider=LLMProvider.OPENAI, model_name="gpt-3.5-turbo")

url = "https://www.roguefilms.co.uk/"

content = load_content(url).content

convert_to_tweet_prompt = f"""Extract the key info from the following post, 
and Convert to an engaging 280 chars tweet. post content : {content}""" 

generated_text = llm_instance.generate_response(prompt=convert_to_tweet_prompt)

print(generated_text)