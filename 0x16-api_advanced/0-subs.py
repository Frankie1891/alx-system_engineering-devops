import requests

def number_of_subscribers(subreddit):
    """ Set a custom User-Agent to avoid issues with "Too Many Requests" error """
    headers = {'User-Agent': 'python:subscribers-check:v1.0 (by /u/yourusername)'}

    """ Reddit API URL for getting subreddit information """
    url = f'https://www.reddit.com/r/{}/hot/about.json'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        """ Check if the subreddit exists """
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
