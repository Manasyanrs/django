from django.urls import path
from .views import BasedView

urlpatterns = [
    path('article/', BasedView.as_view(), name='article')
]
