from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View, CreateView, DetailView, UpdateView
from .models import News, Comments
from .forms import CommentsForm


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        all_news = News.objects.all()
        return render(request, "restaurants/all_news.html", context={
            "all_news": all_news
        })


class NewsDetailView(DetailView):
    model = News
    template_name = "restaurants/detail_news.html"
    context_object_name = "news_detail"

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context["comments"] = Comments.objects.filter(news=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        add_comment = CommentsForm(request.POST)

        if add_comment.is_valid():
            Comments.objects.create(news=self.get_object(), **add_comment.cleaned_data)
            return HttpResponseRedirect("/news/{}".format(kwargs["pk"]))

        return render(request, "restaurants/add_comments.html", context={"add_comment": add_comment})


class AddComments(CreateView):
    model = Comments
    template_name = "restaurants/add_comments.html"
    fields = ["name", "text"]

    def get_context_data(self, **kwargs):
        form_comment = CommentsForm()
        context = super(AddComments, self).get_context_data(**kwargs)
        context["comment_id"] = self.kwargs["pk"]
        context["form"] = form_comment

        return context


class AddNews(CreateView):
    model = News
    template_name = "restaurants/add_news.html"
    fields = ["title", "body"]


class UpdateNews(AddNews, UpdateView):
    template_name = "restaurants/update_news.html"
