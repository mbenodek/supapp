import requests
from requests import get
from bs4 import BeautifulSoup
from requests.exceptions import RequestException
from contextlib import closing
import smtplib
import json
import urllib3


headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/75.0.3770.100 Safari/537.36'}


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


def get_info_label():
   # URL = 'http://covid-19india-api.herokuapp.com/all'
    URL="https://covidtracking.com/"
    response = simple_get(URL)

    data = BeautifulSoup(response, "html.parser")
    print(data)
    key_list = []
    val_list = []
    newdict = dict()

    for col in data.find_all("div", class_='info_label'):
        key_list.append((col.text).lstrip().rstrip())

    for row in data.find_all("span", class_='icount'):
        val_list.append(row.text.lstrip().rstrip())

    index = 0
# loop key_list and add key pair to dict
    for key in key_list:
     newdict[key] = val_list[index]
     index += 1
    return(newdict)




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('askmayur@gmail.com', 'spvaulzgmojomovd')
    subject = 'Price is Changing mate!!!----sending mail through pyhton program --price checker---testing'
    body = 'Check the Link Dude https://www.amazon.in/Pigeon-Stovekraft-Favourite-Induction-Aluminium/dp/B00T6DHFO6/ref=sr_1_5?crid=3FJQYYSNNXYQ1&keywords=pressure+cooker+3+litre&qid=1562565755&s=gateway&sprefix=pressure+cooker+3+%2Caps%2C252&sr=8-5'
    msg = f"Subject={subject}\n\n{body}"

    server.sendmail(
        'askmayur@gmail.com',
        'bhawana.ratnaparakhee@gmail.com',
        msg
    )

    print('Hey Email Has been sent')
    server.quit()

#get_info_label()