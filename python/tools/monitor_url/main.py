#script to check and monitor website
#TODO: extend monitoring function
import requests
import time
import logging


#set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logger.info(f"The website {url} is reachable.")
        else:
            logger.warning(f"The website {url} returned a non-200 status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error accessing the website {url}: {e}")


def monitor_website(url, interval):
    while True:
        check_website(url)
        time.sleep(interval)


def main():
    #enter the URL you want to monitor
    user_url = input('Enter web address:')
    url = f'https://{user_url}'  
    interval = 60  #time interval in seconds between checks

    #monitor the website continuously
    monitor_website(url, interval)


if __name__ == "__main__":
    main()