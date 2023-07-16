import requests
import random

class mail():
    def __init__(self, login='', domain='1secmail.com'):
        self.login = login
        self.domain = domain

    def generate_random_email_address(self) -> None:
        r = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=10')
        get_random = f'{random.choice(r.json())}'
        self.login, self.domain = get_random.split('@')

    @property
    def get_list_of_active_domains(self):
        return requests.get('https://www.1secmail.com/api/v1/?action=getDomainList').json()

    def get_list_of_emails(self):
        if not self.login or not self.domain:
            self.generate_random_email_address()
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={self.login}&domain={self.domain}')
        return r.json()

    def get_login(self) -> str:
        return self.login

    def get_domain(self) -> str:
        return self.domain
    
    def get_email(self) -> str:
        return self.login + "@" + self.domain
    
    def get_text(self, id: str) -> str:
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={self.login}&domain={self.domain}&id={id}').json()
        return r['body']




