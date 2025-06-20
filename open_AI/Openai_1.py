'''
Created on Nov 5, 2024

@author: admin
'''

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OPENAI_API_KEY')


if __name__ == '__main__':
    pass