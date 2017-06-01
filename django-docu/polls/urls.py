from django.conf.urls import url
from polls import views

app_name = 'polls'
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name = 'detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = 'vote'),
]
