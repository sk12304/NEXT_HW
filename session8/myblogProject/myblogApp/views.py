from django.shortcuts import render
from .models import Article

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

