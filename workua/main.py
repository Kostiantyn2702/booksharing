import requests
from bs4 import BeautifulSoup
from time import time, sleep
import random
from fake_useragent import UserAgent

ua = UserAgent()

BASE_URL = 'https://www.work.ua/ru/jobs/'


def random_sleep():
    sleep(random.randint(1, 3))


page = 0

# while True:
with open(f'./jobs{time()}.txt', 'w') as file:
    for i in range(1):
        page += 1
        print(f'Page: {page}') # noqa

        # BASE_URL = f'https://www.work.ua/ru/jobs/?ss=1'
        # BASE_URL = f'https://www.work.ua/ru/jobs/?ss=1&page={page}'

        params = {
            'ss': 1,
            'page': page,
        }
        headers = {
            'User-Agent': ua.random,  # user-agent == 'python-3.9'
        }
        response = requests.get(BASE_URL, params=params, headers=headers)

        random_sleep()

        response.raise_for_status()  # stop program if status_code != 2xx

        html = response.text

        soup = BeautifulSoup(html, 'html.parser')
        jobs_list = soup.find(id="pjax-job-list")

        if jobs_list is None:
            break

        cards = jobs_list.find_all("div", {"class": "job-link"})

        for card in cards:
            tag_a = card.find("h2").find("a")
            job_title = tag_a.text
            job_id = tag_a['href'].split('/')[-2]

            result = f'{job_id} | {job_title}\n'
            file.write(result)
