from django.shortcuts import render
from .models import *
# Create your views here.


# Home view is the home page for coding and data structures blogs
def home(request):
    articles = Article.objects.all()
    return render(request, 'coding/home.html', {'articles': articles})

# Artcle views will return the template with given article id


def article(request, article_id=None):
    path = f"coding/articles/{article_id}.html"
    article = Article.objects.get(article_id=article_id)
    return render(request, path, {'article': article})
