import logging
logging.basicConfig(filename="multiprocessing.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("MultiProcessing")
