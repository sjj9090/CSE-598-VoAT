import numpy as np
import os

def load_list_from_txt(filename):
    with open(filename, "r") as file:
        return list(map(int, file.read().split()))


def save_history_to_txt(history, filename="chat_history.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for entry in history:
            file.write(entry + "\n")
            file.write("=" * 50 + "\n")  # 구분선 추가
    print(f"Record saved on : '{filename}'.")