import requests
import multiprocessing
import time
session = None

import logging
logging.basicConfig(filename="multiprocessing.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("MultiProcessing")


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


def download_all_sites(sites):
    logger.debug("Calling The download_all_sites Functions")
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)


sites = ["https://www.jython.org","http://olympus.realpython.org/dice"] * 5
start_time = time.time()
download_all_sites(sites)
duration = time.time() - start_time
print(f"Downloaded {len(sites)} in {duration} seconds")



# import multiprocessing
# print("Number of cpu : ", multiprocessing.cpu_count())

