import requests

from pprint import pprint
from argparse import ArgumentParser


def check(email):
    url = 'https://haveibeenpwned.com/api/breachedaccount/{}'
    try:
        data = requests.get(url.format(email)).json()
    except Exception:
        data = []
    return data


def main():
    parser = ArgumentParser()
    parser.add_argument('email', help='Say your email')
    args = parser.parse_args()
    pprint(check(args.email))
