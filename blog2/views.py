from django.shortcuts import render


def render_post(request):
    print('test')
    return render(request,'posts.html')