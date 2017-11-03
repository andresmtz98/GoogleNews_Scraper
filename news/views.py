from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import News
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from newspaper.article import ArticleException




#User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39"

def getFechaPublicacion(texto):
    texto_fecha = None
    check = True
    for i in range(0,len(texto)):
        if texto[i] == '-':
            texto_fecha = texto[i+2:len(texto)]
            if texto_fecha[0] != 'h': # h del 'hace x minutos/horas'
                check = False
            break
    return texto_fecha, check


def search_news(list_news, query):
    index = 0
    check = True
    while(check):
        url = "https://www.google.com.co/search?q=%s&tbs=sbd:1,qdr:d&tbm=nws&start=%s" % (query, index)
        req = requests.get(url)
        if req.status_code == 200:
            html = BeautifulSoup(req.text, 'html.parser')
            entradas = html.find_all('h3', {'class': 'r'})
            fechas_publicacion = html.find_all('span', {'class': 'f'})
            for i, ent in enumerate(entradas):
                urlNew = ent.a['href']
                urlNew = urlNew[7:len(urlNew)]
                urlNew.capitalize()
                urlNew = urlNew[0:urlNew.find("&")]
                article = Article(urlNew, language='es')
                try:
                    article.download()
                    article.parse()
                    fecha_publicacion,  check = getFechaPublicacion(
                        fechas_publicacion[i].text)
                    new = News()
                    new.title = article.title
                    new.description = article.text
                    new.url = article.url
                    new.url_image = article.top_image
                    new.date = article.publish_date
                    new.latest_updated = fecha_publicacion
                    list_news.append(new)
                except ArticleException:
                    continue
        else:
            print(req.status_code)
        index += 10
        if index > 10:
            return list_news

def index(request):
    if request.method == "GET" and request.GET.get('query',None) is not None:
        query = request.GET.get('query',None)
        news = search_news([], query)
        template = loader.get_template('index.html')
        print(news)
        context = {
            'news': news
        }
        return render(request, "index.html", context)
    else:
        template = loader.get_template('index.html')
        context = {}
        return render(request, "index.html", context)
