from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html',{'badgirl':'mess girl'})

def count(request):
    fulltext=request.GET['fulltext']
    k=fulltext.split()
    wrddic={}
    for i in k:
        if i in wrddic:
            wrddic[i]+=1
        else:
            wrddic[i] = 1
    sordic = sorted(wrddic.items(),key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'cnt':len(k),'dic':sordic})
def about(request):
    return render(request,'about.html')
