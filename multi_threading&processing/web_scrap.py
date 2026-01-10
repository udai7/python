
import requests
import threading
from bs4 import BeautifulSoup

urls=[
'https://ai.google.dev/gemini-api/docs',

'https://ai.google.dev/gemini-api/quickstart',

'https://ai.google.dev/gemini-api/api-key'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetch {len(soup.text)} characters from {url}')

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All threads completed')