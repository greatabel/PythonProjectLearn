from os import environ
import requests


YOUR_DOMAIN_NAME = environ.get('YOUR_DOMAIN_NAME', '')
YOUR_API_KEY = environ.get('YOUR_API_KEY', '')

def send_simple_message(YOUR_DOMAIN_NAME, YOUR_API_KEY):
    return requests.post(
        "https://api.mailgun.net/v3/" + YOUR_DOMAIN_NAME + "/messages",
        auth=("api", YOUR_API_KEY),
        data={"from": "Abel <mailgun@" + YOUR_DOMAIN_NAME + ">",
              "to": ["greatabel2@126.com", "YOU@abelCorp"],
              "subject": "email test: hello world",
              "text": "Testing some Mailgun awesomness!"})


if __name__ == "__main__":
    r = send_simple_message(YOUR_DOMAIN_NAME, YOUR_API_KEY)
    print(r, type(r), r.json())