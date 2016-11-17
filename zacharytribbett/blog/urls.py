from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    url(r'^$', views.IndexView.as_view(), name='post_list'),
]