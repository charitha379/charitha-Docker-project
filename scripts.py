import os
import socket
from collections import Counter
import re

def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w']", " ", text)
    text = text.replace("'", " ")  # Split contractions like can't to can t
    return text.split()

def get_top_words(text, top_n=3):
    word_counts = Counter(text)
    return word_counts.most_common(top_n)

def get_ip():
    return socket.gethostbyname(socket.gethostname())

def write_output(output_path, results):
    with open(output_path, 'w') as file:
        file.write(results)

if __name__ == "__main__":
    file1 = "/home/data/IF-1.txt"
    file2 = "/home/data/AlwaysRememberUsThisWay-1.txt"
    output_path = "/home/data/output/result.txt"
    os.makedirs("/home/data/output", exist_ok=True)

    text1 = clean_text(read_file(file1))
    text2 = clean_text(read_file(file2))

    total_words1 = len(text1)
    total_words2 = len(text2)
    grand_total = total_words1 + total_words2

    top_words1 = get_top_words(text1)
    top_words2 = get_top_words(text2)

    ip_address = get_ip()

    result = (
        f"Total words in {file1}: {total_words1}\n"
        f"Total words in {file2}: {total_words2}\n"
        f"Grand Total Words: {grand_total}\n\n"
        f"Top 3 Words in {file1}:\n{top_words1}\n\n"
        f"Top 3 Words in {file2}:\n{top_words2}\n\n"
        f"IP Address: {ip_address}\n"
    )

    print(result)
    write_output(output_path, result)
