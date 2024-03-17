from django.views.generic import ListView
from .models import Article


class BasedView(ListView):
    queryset = (
        Article.objects
        .defer("content")
        .select_related("author")
        .select_related("category")
        .prefetch_related("tags")
    )
    template_name = "blogapp/article_list.html"
    context_object_name = "article_list"
