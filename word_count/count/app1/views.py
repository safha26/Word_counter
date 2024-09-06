from django.shortcuts import render
from . forms import *

# Create your views here.
def countpage(req):
    word_count=None
    count_with_space = None
    count_without_space = None
    form = TextInputForm(req.POST or None)

    if req.method == 'POST' and form.is_valid():
        text = form.cleaned_data['text']
        #To count words
        word_count = len(text.split())

        #To count text characters with spaces
        count_with_space = len(text)

        #To count text characters without spaces
        count_without_space = len(text.replace(' ',''))

    return render(req, 'count.html',{
        'word_count':word_count,
        'count_with_space':count_with_space,
        'count_without_space': count_without_space,
        'form':form,
    })