import requests
from datetime import date, timedelta


def get_data_from_github():
    week_ago = str(date.today() - timedelta(weeks=1))
    payload = {'q' :['created:>{}'.format(week_ago)],
               'language': 'python',
               'sort': 'stars',
               }
    url = 'https://api.github.com/search/repositories'
    top_repos = requests.get(url,params=payload).json()['items']
    return top_repos


def get_trending_repositories(top_repos_data, top_list_count):
    top_list = []
    for top_number in range(top_list_count+1):
        repository_name = top_repos_data[top_number]['name']
        repository_url = top_repos_data[top_number]['html_url']
        repository_issues = top_repos_data[top_number]['open_issues']
        repository = (repository_name, repository_url, repository_issues)
        top_list.append(repository)
    return top_list


def pprint_top_list(top_list):
    for repo in top_list:
        print('Name: {:10} URL: {:10} Open Issues: {}'.format(repo[0],repo[1],repo[2]))


if __name__ == '__main__':
    top_list_count = 20
    top_repos_data = get_data_from_github()
    top_list = get_trending_repositories(top_repos_data, top_list_count)
    pprint_top_list(top_list)
    pass
