from django.shortcuts import render
from django.http import HttpResponse


def showTest(request):
    que = "Who Developed C Language?"
    a = "Ken Thompson"
    b = "Dennis Ritchie"
    c = "Bjarne Stroustrp"
    d = "James Gosling"
    level = "Easy"
    data = {'que': que, 'a': a, 'b': b, 'c': c, 'd': d, 'level': level}
    res = render(request, 'exam/test.html', context = data)
    return HttpResponse(res)

def showResult(reuqest):
    s="<h1>This is show Result Page</h1>"
    return HttpResponse(s)
