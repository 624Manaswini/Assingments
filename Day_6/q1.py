from bs4 import BeautifulSoup
import asyncio 
import sys
import aiohttp

#setup
if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#setup end 
    
    
async def download(url):
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as resp:
            return url, await resp.text()


    
async def get_links(url):
    _,html = await download(url)
    soup = BeautifulSoup(html,"html.parser")
    links = []
    for a in soup.find_all('a', href = True):
        href = a['href']
        if href.startswith("http"):
            links.append(href)
    return links
    

async def download_all(urls):
    tasks = [asyncio.create_task(download(url)) for url in urls]
    out = []
    for task in asyncio.as_completed(tasks): 
        out.append(await task)
    return out     

if __name__ == "__main__":
    
    main_url = r"https://www.harrypotter.com/"
    print(f"Downloading the URL : {main_url}")
    
    links = asyncio.run(get_links(main_url))
    print(f"found {len(links)} links")
    
    results = asyncio.run(download_all(links))
    
    for url, content in results:
        print(f"{url}---> {len(content)} bytes")
