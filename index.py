from bs4 import BeautifulSoup
import requests


def get_price():
    page = requests.get('https://www.goodreturns.in/gold-rates/hyderabad.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    value = soup.find('div', class_='gold_silver_table gold_silver_table_10_days')
    today_price = value.find_all('td')[5].get_text().strip()
    return " ".join(today_price.split())


def send_alert(price):
    print(price)
    print('sending alert')


if __name__ == '__main__':
    price = get_price()
    send_alert(price)
    input()
