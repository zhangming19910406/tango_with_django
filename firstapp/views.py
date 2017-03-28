from django.shortcuts import render, redirect, Http404, HttpResponse
from firstapp.models import Article, Comment, Ticket
from firstapp.forms import CommentForm, LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ObjectDoesNotExist


def detail(request, id, error_form=None):
    context = {}

    vid_info = Article.objects.get(id=id)
    voter_id = request.user.profile.id
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=vid_info)
        context['user_ticket'] = user_ticket_for_this_video
    except:
        pass

    article = Article.objects.get(id=id)
    context['article'] = article

    form = CommentForm
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form
    print(form.errors)
    return render(request, 'detail.html', context)


def detail_vote(request, id):
    voter_id = request.user.profile.id
    vote = request.POST['vote']
    try:
        user_ticket_for_this_video = Ticket.objects.get(voter_id=voter_id, video_id=id)
        user_ticket_for_this_video.choice = vote
        user_ticket_for_this_video.save()
    except ObjectDoesNotExist:
        new_ticket = Ticket(voter_id=voter_id, video_id=id, choice=vote)
        new_ticket.save()

    # return redirect(to='detail', id)
    return redirect(to='detail', id=id)


def detail_comment(request, page_num):
    form = CommentForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        content = form.cleaned_data["content"]
        a = Article.objects.get(id=page_num)
        c = Comment(name=name, content=content, belong_to=a)
        c.save()
    else:
        return detail(request, page_num, error_form=form)

    return redirect(to=detail, id=page_num)


def listing(request, cate=None):
    context = {}
    if cate is None:
        vids_list = Article.objects.all()
    elif cate == 'editors':
        vids_list = Article.objects.filter(editor_choice=True)
    else:
        vids_list = Article.objects.all()
    page_robot = Paginator(vids_list, 6)
    # article_list = page_robot.page(request.GET.get('page'))
    page_number = request.GET.get('page')
    try:
        article_list = page_robot.page(page_number)
    except EmptyPage:
        article_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        article_list = page_robot.page(1)
    context['article_list'] = article_list
    return render(request, 'listing.html', context)


def index_login(request):
    context = {}
    if request.method == 'GET':
        form = AuthenticationForm

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect(to='listing')
    context['form'] = form
    return render(request, 'register_login.html', context)


def register(request):
    context = {}
    if request.method == 'GET':
        form = UserCreationForm

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form'] = form
    return render(request, 'register_login.html', context)
