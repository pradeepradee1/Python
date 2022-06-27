import requests
import multiprocessing
import time
session = None
from Log import logger

def set_global_session():
    logger.debug("Calling The  set_global_session Functions")
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    logger.debug("Calling The  download_sites Functions")
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

class download_all_sites:
    def download_all_sites(self,sites):
        logger.debug("Calling The download_all_sites Functions")
        with multiprocessing.Pool(initializer=set_global_session,processes=5) as pool:
            pool.map(download_site, sites)
        # pool.close()

        


obj=download_all_sites()
sites = ["https://www.jython.org","http://olympus.realpython.org/dice"] * 50
start_time = time.time()
obj.download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")

