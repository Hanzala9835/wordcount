from django.shortcuts import render, redirect
import operator
def HomeViews(request):
    # if :
    #     return render(request,'counter.html')
    return render(request,'home.html')

def CounterViews(request):
    data= request.GET['fulltextarea']
    word_list = data.split()
    list_length = len(word_list)

    word_dict = {}


    for word in word_list:

        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word]=1
    sorted_dict = sorted(word_dict.items(), key = operator.itemgetter(1), reverse=True)
    return render(request,'counter.html',{'fulltext':data, 'word':list_length, 'word_dict':sorted_dict})