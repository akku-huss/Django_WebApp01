from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request, 'index.html', {'key':'I am coming from python code'})

def result(request):
    article = request.GET['article']
    word_count, var_dict = counter.count(article)
    return render(request, 'result.html', {'article':article, 'word_count':word_count, 'var_dict':var_dict})