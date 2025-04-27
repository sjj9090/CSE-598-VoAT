from openai import OpenAI


def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

api_key = "CHATGPT API KEY"
client = OpenAI(api_key = api_key)

from utils import save_history_to_txt
import pandas as pd
import os
import numpy as np
import re
import time


def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def ask_image_question(text):
    response = client.chat.completions.create(
    #model="gpt-4o",
    model="o3-mini",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": text
            },
        ],
        }
    ],
    )
    return response.choices[0].message.content

          

def main():    
    map_base_folder = 'examples_small/'
    saving_folder = 'chatgpt_o3_mini_result_4f/'
    processing_type = 'small_3d_4f_ex'
    for i in range(30):
        map_name = processing_type + str(i+1)
        map_txt = load_text_from_file(map_base_folder + map_name + '.txt')
        prompt_part1 = load_text_from_file('prompt_routfinding_3d_CoT_part1.txt')
        prompt_part2 = load_text_from_file('prompt_routfinding_3d_CoT_part2.txt')
        prompt_full = prompt_part1 + '\n' + map_txt + '\n\n' + prompt_part2
        response_text = ask_image_question(prompt_full)
        print(response_text)
        save_history_to_txt([response_text], saving_folder + 'CoT_result/' + map_name + '.txt')

print("="*50)
main()