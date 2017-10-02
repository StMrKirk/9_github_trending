import requests
from datetime import date, timedelta


def get_data_from_github():
    week_ago = str(date.today() - timedelta(weeks=1))
    payload = {'q': 'created:>{}'.format(week_ago),
               'language': 'python',
               'sort': 'stars',
               }
    url = 'https://api.github.com/search/repositories'
    top_repos = requests.get(url,params=payload).json()['items']
    return top_repos


def get_trending_repositories(top_repos_data, top_list_count):
    for repo in range(top_list_count+1):
        print('Name: {:10} URL: {:10} Open Issues: {}'
              .format(top_repos_data[repo]['name'], top_repos_data[repo]['html_url'], top_repos_data[repo]['open_issues']))


if __name__ == '__main__':
    top_list_count = 20
    top_repos_data = get_data_from_github()
    get_trending_repositories(top_repos_data, top_list_count)
