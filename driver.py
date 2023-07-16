import time
import random
import re

from datetime import datetime
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from mail import mail
from db import db

class Alterzone:
    def __init__(self, limited_offer=False):
        self.limited_offer = limited_offer
        self.counter: int = 0
        self.options = webdriver.EdgeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument('--headless')
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] {Fore.GREEN}Usluga utworzona")
        print(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] {Fore.GREEN}Generowanie kodow, to moze chwile potrwac...")

    def __get_points(self, driver: webdriver.Edge, wait: WebDriverWait):
        try:
            # Nowy Rok z Alter Zone
            driver.get('https://alterzone.pl/aktywnosci/styczen1_2023/gra')
            time.sleep(5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]')))
            prawda = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]')
            falsz = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)

            """
            # Pierwsze doświadczenie
            driver.get('https://alterzone.pl/aktywnosci/wrzesien3_2022/gra')
            time.sleep(5)
            dwa = driver.find_element(By.XPATH, '//*[@id="checkbox-1"]')
            trzy = driver.find_element(By.XPATH, '//*[@id="checkbox-2"]')
            cztery = driver.find_element(By.XPATH, '//*[@id="checkbox-3"]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', cztery)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', trzy)
            driver.execute_script('arguments[0].click();', dalej)
            """

            # 7 błędów głównych
            driver.get('https://alterzone.pl/aktywnosci/styczen4_2023/gra')
            time.sleep(5)
            prawda = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]')
            falsz = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)

            """
            # Znajdź intruza
            driver.get('https://alterzone.pl/aktywnosci/wrzesien2_2022/gra')
            time.sleep(5)
            jeden = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/button[1]')
            cztery = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/button[4]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', cztery)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            """

            """
            # Pierwsze doświadczenie
            driver.get('https://alterzone.pl/aktywnosci/wrzesien3_2022/gra')
            time.sleep(5)
            dwa = driver.find_element(By.XPATH, '//*[@id="checkbox-1"]')
            trzy = driver.find_element(By.XPATH, '//*[@id="checkbox-2"]')
            cztery = driver.find_element(By.XPATH, '//*[@id="checkbox-3"]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', cztery)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', trzy)
            driver.execute_script('arguments[0].click();', dalej)
            """

            # Subskrypcja neo™
            driver.get('https://alterzone.pl/aktywnosci/luty1_2023/gra')
            time.sleep(5)
            prawda = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[1]')
            falsz = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[4]/button[2]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', falsz)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', prawda)
            driver.execute_script('arguments[0].click();', dalej)

            # Poznaj warianty smakowe neo™
            driver.get('https://alterzone.pl/aktywnosci/luty2_2023/gra')
            time.sleep(5)
            jeden = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/div[2]/button[1]')
            dwa = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/div[2]/div[2]/button[2]')
            dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div/div/button')
            # pytanie 1
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 2
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 3
            driver.execute_script('arguments[0].click();', dwa)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 4
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 5
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 6
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 7
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 8
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
            # pytanie 9
            driver.execute_script('arguments[0].click();', jeden)
            driver.execute_script('arguments[0].click();', dalej)
        except Exception as e:
            print(e)

    def __redeem(self, driver: webdriver.Edge, wait: WebDriverWait, counter: int, site: str, suffix: str):
        try:
            # nagrody
            driver.get(site)
            odbierz_xpath = ""
            kod_xpath = ""

            time.sleep(5)
            if 'zone_awards_3wcenie1' in site:
                odbierz_xpath = '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div[6]/button'
                kod_xpath = '//*[@id="root"]/div/div[2]/div/div/section/div[2]/button'
            elif 'neo_1+1_nastart' in site:
                odbierz_xpath = '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div[7]/button'
                kod_xpath = '//*[@id="root"]/div/div[2]/div/div/section/div[2]/div[4]/button'
                
            wait.until(EC.presence_of_element_located((By.XPATH, odbierz_xpath)))
            odbierz_nagrode = driver.find_element(By.XPATH, odbierz_xpath)
            driver.execute_script('arguments[0].click();', odbierz_nagrode)
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div/div[3]/button')))
            potwierdz = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div/section/div/div[3]/button')
            driver.execute_script('arguments[0].click();', potwierdz)

            # kopiuj kod
            wait.until(EC.presence_of_element_located((By.XPATH, kod_xpath)))
            kod = driver.find_element(By.XPATH, kod_xpath)
            append_text("kody.txt", kod.text.replace('KOD: ', '') + f' ({suffix})')
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{Fore.WHITE}│ [{Fore.GREEN}ALTERZONE AIO{Fore.WHITE}] [{Fore.GREEN}{now}{Fore.WHITE}] [{Fore.GREEN}{counter}{Fore.WHITE}] {Fore.GREEN}Dodano kod {Fore.WHITE}{kod.text.replace('KOD: ', '')}{Fore.WHITE} [{Fore.GREEN}{suffix}{Fore.WHITE}]")
            del kod, potwierdz, odbierz_nagrode
        except Exception as e:
            print(e)

    def execute(self, alterzone_link: str):
        while True:
            driver = webdriver.Edge(options=self.options, service=Service(EdgeChromiumDriverManager().install()))
            wait = WebDriverWait(driver, 30)
            driver.get(alterzone_link)
            temp_mail = mail()
            try:
                # potwierdzenie wieku
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]')))
                potwierdzam_wiek = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]')
                driver.execute_script('arguments[0].click();', potwierdzam_wiek)

                # cookies
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="accept_cookies"]')))
                cookies = driver.find_element(By.XPATH, '//*[@id="accept_cookies"]')
                driver.execute_script('arguments[0].click();', cookies)

                # rejestracja
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/button')))
                wchodze_w_to = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/div[2]/button')
                driver.execute_script('arguments[0].click();', wchodze_w_to)

                # imie
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[1]/input')))
                imie = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[1]/input')
                imie.send_keys(random.choice(db['imie']))

                # nazwisko
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[2]/input')))
                nazwisko = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[2]/input')
                nazwisko.send_keys(random.choice(db['nazwisko']))

                # email
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[3]/input')))
                email = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[3]/div[3]/input')
                temp_mail.generate_random_email_address()
                email.send_keys(temp_mail.get_email())

                # zgody
                consent_agreement = driver.find_element(By.XPATH, '//*[@id="consentAgreement"]')
                age_verified = driver.find_element(By.XPATH, '//*[@id="ageVerified"]')
                conset_data = driver.find_element(By.XPATH, '//*[@id="consentData"]')
                driver.execute_script('arguments[0].click();', consent_agreement)
                driver.execute_script('arguments[0].click();', age_verified)
                driver.execute_script('arguments[0].click();', conset_data)

                # dalej
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button')))
                dalej = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button')
                driver.execute_script('arguments[0].click();', dalej)

                # zarejestruj sie
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button')))
                zarejestruj_sie = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/div[2]/div/form/div[4]/button')
                driver.execute_script('arguments[0].click();', zarejestruj_sie)

                # czekanie na email
                email_id = ""
                while True:
                    time.sleep(5)
                    emails = temp_mail.get_list_of_emails()
                    if len(emails) > 0:
                        email_id = emails[0]['id']
                        break

                # aktywacja email
                email_list= temp_mail.get_text(email_id).split('\n')
                email_list[:] = [url for url in email_list if any(sub in url for sub in ["aHR0cHM6Ly9hbHRlcnpvbmUucGwvaGFzbG8vdXN0YXc"])]
                email_text = ""
                match = re.search(r'(http):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', email_list[0])
                if match:
                    email_text = match.group(0)

                # ustawianie hasla
                driver.get(email_text)
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="passwd"]')))
                haslo = driver.find_element(By.XPATH, '//*[@id="passwd"]')
                powtorz_haslo = driver.find_element(By.XPATH, '//*[@id="repeatPasswd"]')
                haslo.send_keys("Unknown1234!@")
                powtorz_haslo.send_keys("Unknown1234!@")

                # ustaw haslo
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[3]/button')))
                ustaw_haslo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[3]/button')
                driver.execute_script('arguments[0].click();', ustaw_haslo)

                # konto aktywne
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div[2]/div')))
                zaloguj_sie = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/div/button')
                driver.execute_script('arguments[0].click();', zaloguj_sie)

                # logowanie
                wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[3]/div[1]/input')))
                email = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[3]/div[1]/input')
                haslo = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[3]/div[2]/input')
                zaloguj_sie = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/div/div/div/div/form/div[5]/button')
                email.send_keys(temp_mail.get_email())
                haslo.send_keys("Unknown1234!@")
                driver.execute_script('arguments[0].click();', zaloguj_sie)

                # glowna strona
                wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div/div/div[2]/div/div[3]/button[1]')))
                odrzuc = driver.find_element(By.XPATH, '/html/body/div[9]/div/div/div[2]/div/div[3]/button[1]')
                driver.execute_script('arguments[0].click();', odrzuc)

                # nagrody
                self.__redeem(driver, wait, self.counter, 'https://alterzone.pl/nagrody/odbior/neo_1+1_nastart', '2 w cenie 1')
                if self.limited_offer:
                    self.__get_points(driver, wait)
                    self.__redeem(driver, wait, self.counter, 'https://alterzone.pl/nagrody/odbior/drop/zone_awards_3wcenie1', '3 w cenie 1')
                self.counter += 1
            except Exception as e:
                print(e)
            finally:
                driver.delete_all_cookies()
                driver.close()
                driver.quit()

def append_text(file_path: str, kod: str):
    file = open(file_path, "a")
    file.write(kod + "\n")
    file.close()