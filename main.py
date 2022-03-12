import datetime
import bs4
import requests
import gspread


def req():
    text = input("enter what to search")
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    google_search = requests.get("https://www.google.com/search?q="+text, headers=headers)
    soup = bs4.BeautifulSoup(google_search.text, 'lxml')
    return soup


def Items(soup):
    date = datetime.datetime.now()
    title = soup.find('h3').text.strip()
    descriptions = soup.find('div', class_='BNeawe s3v9rd AP7Wnd').text.strip()
    links = soup.find('div', class_="egMi0 kCrYT").text.strip()
    product = {'date': date, 'title': title, 'descriptions': descriptions, 'links': links}
    return product


def output(product):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open('Scraper_results').sheet1
    sh.append_row([str(product['date']), str(product['title']), str(product['descriptions']), str(product['links'])])
    return


data = req()
product = Items(data)
output(product)


