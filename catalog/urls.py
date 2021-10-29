from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    url(r'^$', views.index, name='index1'),
    url(r'^book/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^date/$', views.DateListView.as_view(), name='dates'),
    path('pdf/', views.some_view, name='pdf'),

    #Передача дополнительных настроек в ваши преобразования URL-адресов
    # url(r'^/url/$', views.my_reused_view, {'my_template_name': 'some_path'}, name='aurl'),
    # url(r'^/anotherurl/$', views.my_reused_view, {'my_template_name': 'another_path'}, name='anotherurl'),


]

