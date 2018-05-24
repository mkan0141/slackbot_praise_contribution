import requests
import csv
import re

def load_file():
    with open('member_list.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',',quotechar='"')
        next(csv_reader)
    csvfile.close()
    return csv_reader

def get_github_contributes(user_id):
    url = "https://github.com/users/" + user_id + "/contributions"
    response = requests.get(url)
    data = response.text
    data = data.split('\n')
    return [re.findall('data-count="([0-9]+)"', x) for x in data if re.findall('data-count="([0-9]+)"', x)]

if __name__ == '__main__':
    user_data = load_file()
    for user in user_data:
        contributes = get_github_contributes(user[0])

        for contribute in contributes[::-1]
