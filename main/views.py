from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import News, Category, Comment, Member
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth


def home(request):
    other_news = News.objects.all().order_by('-view', '-time')
    news_paginator = Paginator(other_news, 3)
    page = request.GET.get('page', 1)
    try:
        nnews = news_paginator.page(page)
    except PageNotAnInteger:
        nnews = news_paginator.page(1)
    except EmptyPage:
        nnews = news_paginator.page(news_paginator.num_pages)
    all_cat = Category.objects.all()
    return render(request, 'home.html', {
        'all_cat': all_cat,
        'nnews': nnews,

    })


def index(request):
    other_news = News.objects.all().order_by('-view', '-time')
    news_paginator = Paginator(other_news, 3)
    page = request.GET.get('page', 1)
    try:
        nnews = news_paginator.page(page)
    except PageNotAnInteger:
        nnews = news_paginator.page(1)
    except EmptyPage:
        nnews = news_paginator.page(news_paginator.num_pages)
    all_cat = Category.objects.all()
    return render(request, 'home.html', {
        'all_cat': all_cat,
        'nnews': nnews,

    })


def detail(request, id):
    news = News.objects.get(pk=id)
    news.view = news.view + 1
    news.save()
    try:
        comment = Comment.objects.filter(news=news).filter(status=True).order_by('-time')
    except Comment.DoesNotExist:
        comment = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            body=msg,
        )
        news.cmtCount = Comment.objects.filter(news=news).filter(status=True).count()
        news.save()
        messages.success(request, 'کامنت با موفقیت ارسال شد. بعد از تایید مدیر نشان داده میشود.')
    return render(request, 'detail.html', {
        'detail': news,
        'comment': comment
    })


def cat(request, id):
    cate = Category.objects.get(id=id)
    news = News.objects.filter(category=cate)
    return render(request, 'cat.html', {
        'nnews': news
    })


def reg(request):
    if request.method == 'POST':
        username = request.POST['user']
        email = request.POST['email']
        password = request.POST['pass']
        repassword = request.POST['repass']
        cate = request.POST['cat']
        if password == repassword:
            try:
                user = Member.objects.get(username=username)
            except Member.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = Member(username=username)
                user.is_staff = True
                user.is_superuser = False
                user.email = email
                user.set_password(password)
                user.save()
                if cate == "technology":
                    user.interest.add('3')
                elif cate == "politics":
                    user.interest.add('2')
                elif cate == "econimies":
                    user.interest.add('1')
                elif cate == "sports":
                    user.interest.add('4')
                elif cate == "health":
                    user.interest.add('5')
                user.groups.add('1')
        messages.success(request, '.کاربر با موفقیت ثبت شد')
    return render(request, 'registration/register.html', {

    })


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('user', '')
        password = request.POST.get('pass', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/index")
        else:
            # Show an error page
            print(username, password)
            return HttpResponseRedirect("/signin")
    return render(request, 'registration/signin.html')


def signout(request):
    auth.logout(request)

    return HttpResponseRedirect("/")
