import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed


def download(url):
    resp = requests.get(url,timeout =2)
    return url, resp.text
    
def get_links(url):
    _,html = download(url)
    soup = BeautifulSoup(html,"html.parser")
    links = []
    for a in soup.find_all('a', href = True):
        href = a['href']
        if href.startswith("http"):
            links.append(href)
    return links
    
def download_all(urls):
    out = []
    with ThreadPoolExecutor(max_workers = 10) as executer:
        tasks = [executer.submit(download,url) for url in urls]
        for task in as_completed(tasks):
            out.append(task.result())
        return out
        
if __name__ == "__main__":
    
    main_url = r"https://www.harrypotter.com/"
    print(f"Downloading the URL : {main_url}")
    
    links = get_links(main_url)
    print(f"found {len(links)} links")
    
    results = download_all(links)
    
    for url, content in results:
        print(f"{url}---> {len(content)} bytes")
    
