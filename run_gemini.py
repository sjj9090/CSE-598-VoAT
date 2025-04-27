import google.generativeai as genai


def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

api_key = 'NEED GEMINI API KEY'
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash-lite")

from utils import save_history_to_txt
import pandas as pd
import numpy as np
import time


def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def ask_image_question(text):
    time.sleep(1)
    response = model.generate_content(contents=[text])
    return response.text
          

def main():    
    map_base_folder = 'examples_small/'
    saving_folder = 'gemini_lite_result/'
    processing_type = 'small_3d_2f_ex'
    for i in range(30):
        map_name = processing_type + str(i+1)
        map_txt = load_text_from_file(map_base_folder + map_name + '.txt')
        prompt_part1 = load_text_from_file('prompt_routfinding_3d_CoT_part1.txt')
        prompt_part2 = load_text_from_file('prompt_routfinding_3d_CoT_part2.txt')
        prompt_full = prompt_part1 + '\n' + map_txt + '\n\n' + prompt_part2
        #print(prompt_full)
        response_text = ask_image_question(prompt_full)
        print(response_text)
        save_history_to_txt([response_text], saving_folder + 'CoT_result/' + map_name + '.txt')

print("="*50)
main()
