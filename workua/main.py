import requests
from bs4 import BeautifulSoup
from time import time, sleep
import random
from fake_useragent import UserAgent
import sqlite3
import csv
import json

ua = UserAgent()

BASE_URL = 'https://www.work.ua/ru/jobs/'
# BASE_URL = f'https://www.work.ua/ru/jobs/?ss=1'
# BASE_URL = f'https://www.work.ua/ru/jobs/?ss=1&page={page}'


def random_sleep():
    sleep(random.randint(1, 3))


def workua_parser():
    page = 0
    result_csv = [["job_id", "job_title", "job_salary", "job_address"]]
    result_json = []

    # while True:
    for i in range(3):
        page += 1

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

            JOB_DETAIL_URL = BASE_URL + job_id + "/"

            response = requests.get(JOB_DETAIL_URL, headers=headers)

            html_job_page = response.text

            soup = BeautifulSoup(html_job_page, 'html.parser')

            # job_description = soup.find(id="job-description").text
            details = soup.find("div", class_="card wordwrap")
            address = details.find("span",
                                   {"class": "glyphicon glyphicon-map-marker text-black glyphicon-large"}).next_sibling
            job_address = str(address).lstrip().rstrip()

            try:
                job_salary = details.find("span", {"class": "glyphicon glyphicon-hryvnia text-black glyphicon-large"})
                job_salary = job_salary.next_sibling.next_sibling.text.replace("\u202f", " ")
            except AttributeError:
                job_salary = "Зарплата не указана!"

            to_json = {'job_id': job_id,
                       'job_title': job_title,
                       'job_salary': job_salary,
                       'job_address': job_address,
                       }
            detail_list = [job_id, job_title, job_salary, job_address]

            result_json.append(to_json)
            result_csv.append(detail_list)

    return result_csv, result_json


csv_data, json_data = workua_parser()
filename_csv = f'./workua/jobs{time()}.csv'
filename_json = f'./workua/jobs{time()}.json'


def write_in_csv(filename, data):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def write_in_db(filename_csv):
    conn = sqlite3.connect("parser.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE parser_table
                          (job_id, job_title, job_salary, job_address)
                       """)
    except sqlite3.OperationalError:
        cursor.execute("""DELETE FROM parser_table;""")

    with open(filename_csv, 'r') as file:
        dict_reader = csv.DictReader(file)
        to_db = [(i['job_id'], i['job_title'], i['job_salary'], i['job_address']) for i in dict_reader]

    cursor.executemany("INSERT INTO parser_table (job_id, job_title, job_salary, job_address) "
                       "VALUES (?, ?, ?, ?);", to_db)
    conn.commit()
    conn.close()


def write_in_json(filename, data):
    with open(filename, "w", encoding='utf8') as write_file:
        me_data = json.dumps(data, ensure_ascii=False)
        write_file.write(me_data)


write_in_csv(filename_csv, csv_data)
write_in_db(filename_csv)
write_in_json(filename_json, json_data)
