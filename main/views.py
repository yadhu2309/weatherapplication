from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def get_html_content(city):
    city = city.replace(' ','+')
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content
def home(request):
    weather=None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        print('html con',html_content)
        soup = BeautifulSoup(html_content,'html.parser')
        # print('soup',soup)
        weather = dict()
        weather['region'] = soup.find('span',attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
     
        weather['dayhour'] = soup.find('div',attrs={'class':'BNeawe tAd8D AP7Wnd'}).text
        weather['temp'] = soup.find('div',attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
        print('region',weather)

    #     print('html content',html_content)
    # print('hello world','city' in request.GET)
    return render(request,'home.html',{'weather':weather})