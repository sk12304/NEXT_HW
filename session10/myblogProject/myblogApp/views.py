from django.shortcuts import render, redirect
from .models import Article, Comment, Recomment

# Create your views here.
def new(request):
    categorys = ['daily', 'hobby', 'study']
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            category = request.POST['category'],
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('list')

    return render(request, 'new.html', {'categorys': categorys})

def list(request, category_name):
    articles = Article.objects.filter(category = category_name)
    all_count = Article.objects.all().count()
    count = articles.count()
    categorys = ['daily', 'hobby', 'study']
    return render(request, "list.html", {'articles': articles, 'categorys': categorys, 'count': count, 'all_count': all_count})

def home(request):
    articles = Article.objects.all()
    categorys = ['daily', 'hobby', 'study']
    count = articles.count()
    return render(request, "home.html", {'articles': articles, 'categorys': categorys, 'count': count})

def detail(request, list_id):
    article = Article.objects.get(pk=list_id)
    if request.method == "POST":
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('detail', article.pk)
    categorys = ['daily', 'hobby', 'study']
    return render(request, 'detail.html', {'article': article, 'categorys': categorys})


def recomment(request, list_id, comment_id):
    article = Article.objects.get(pk=list_id)
    comment = Comment.objects.get(pk=comment_id)
    if request.method == "POST":
        content = request.POST['content']
        Recomment.objects.create(
            comment = comment,
            content = content
        )
        return redirect('recomment', article.pk, comment.pk)
    categorys = ['daily', 'fashion', 'study']
    return render(request, 'recomment.html', {'article': article, 'comment': comment, 'categorys': categorys})

