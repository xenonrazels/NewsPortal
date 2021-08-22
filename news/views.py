from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import News
from django.views.generic.edit import DeleteView,UpdateView
from .forms import NewsForm
import os
from dotenv import load_dotenv
import requests

# Create your views here.
def newsList(request):
    '''This function display models news list'''
    news=get_list_or_404(News)
    return render(request,'index.html',{'newslist':news})

def addNews(request):
    new_news=False
    if request.method=='POST':
        forms=NewsForm(request.POST,request.FILES)
        if forms.is_valid():
            new_news=forms.save()
            new_news=True
    else:
        forms =NewsForm()
    return render(request,'addNews.html' ,{'forms':forms,'new_news':new_news})

load_dotenv()

def apiNews(request):
    ''' This function allows to retrieve news and display news '''
    url = "https://free-news.p.rapidapi.com/v1/search"
    search_word="Elon Musk"
    if request.method == 'GET':
        if 'search' in request.GET:
            search_word=request.GET['search']   
        
    querystring = {"q":search_word,"lang":"en"}

    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': os.getenv('X-RAPIDAPI-KEY')
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    content=response.json()

    context={
        'articles':content['articles'],
        'search_word':search_word
    }
    

    return render(request,'apiNews.html',context)
def editNews(request):
    '''Display the news List so we can edit operations like Update, Delete'''
    news=get_list_or_404(News)
    
    return render(request,'editNews.html',{'newsList':news})


class NewsDeleteView(DeleteView):
    '''Lets you delete News'''
    model = News
    template_name = "delete.html"
    success_url='/editNews'




class NewsUpdateView(UpdateView):
    model = News
    template_name = "update.html"
    fields='__all__'
    success_url='/editNews'


