import threading
from fileinput import filename

import requests

def download_file(url,file_name):
        response = requests.get(url)
        with open(file_name,'wb') as file:
            file.write(response.content)
        print(f"Файл {file_name} успiшно завантажений.")

urls = [
    {"url":"https://www.youtube.com/", "file_name": "file1"},
    {"url":"https://www.google.com/", "file_name": "file2"},
]

threads = []
for file_info in urls:
    url = file_info["url"]
    file_name = file_info["file_name"]
    thread = threading.Thread(target=download_file, args=(url,file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Файли завантажені")


