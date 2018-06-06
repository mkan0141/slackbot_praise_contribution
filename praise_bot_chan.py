import pandas as pd
import re
import requests

def load_file():
    csv_reader = pd.read_csv('./config/member_list.csv')
    return csv_reader

def get_github_contributes(user_id):
    url = "https://github.com/users/" + user_id + "/contributions"
    response = requests.get(url)
    data = response.text
    data = data.split('\n')
    return [re.findall('data-count="([0-9]+)"', x) for x in data if re.findall('data-count="([0-9]+)"', x)]

def max_contribute_count(data):
    ret = 0
    for num in data[::-1]:
        if num != 0:
            num += 1
        else:
            break
    return ret

def DEBUG(user, contributes):
    print(user + ' ' + contributes)

if __name__ == '__main__':
    user_data = load_file()
    for user in user_data['github_user_id']:
        continue_contributes = 0
        contributes = get_github_contributes(user)
        for contribute in contributes[-2::-1]:
            # print(contribute != ['0'])
            if contribute != ['0']:
                continue_contributes += 1
            else:
                break
        print(continue_contributes)
