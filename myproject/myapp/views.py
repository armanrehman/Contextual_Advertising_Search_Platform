from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from rake_nltk import Rake
import nltk
import collections
from .models import Tag
from .models import Advert
import difflib

from pathlib import Path


import os

nltk.download('stopwords')


# Create your views here.
def index(request):
    if request.method=='POST':
        url = request.POST.get('url')
        response = requests.get(url=url, verify=False)
       #print(response)

        soup = BeautifulSoup(response.content,'html.parser')
    
        all_text = ''

        for para in soup.find_all('p'):

            all_text += str(para.get_text())
        
        #print(all_text)
        
        rake_var = Rake()
        rake_var.extract_keywords_from_text(all_text)
        keywords = rake_var.get_ranked_phrases()
        #print(keywords)

        adtags = []
        tags = Tag.objects.all()

        for tag in tags:
            adtags.append(tag.tagname)

        
        #set to find matches 
        seta = set(keywords)
        setb = set(adtags)

        commonwords=[]

        #using intersection of sets to find matches
        if seta & setb:
            commonwords = list(seta & setb)
        
        #print(commonwords)

        relevantads = []

        #looping for all advertisements and advert tags
        for advert in Advert.objects.all():
            for tag in advert.tags.all():
                if tag.tagname in commonwords:
                    relevantads.append(advert)

                    #to avoid duplicate ads
                    relevantads = set(relevantads)
                    relevantads = list(relevantads)

        print(relevantads)
        
        context= {
            'relevantads' : relevantads,
            'commonwords' : commonwords
        }

        


        return render(request, 'myapp/index.html', context)

        
            








    return render(request, 'myapp/index.html')
        





        



        

       
    
       
