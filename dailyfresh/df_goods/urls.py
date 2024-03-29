from django.conf.urls import url
import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^list_(\d+)_(\d+)_(\d+)$', views.list),
    url(r'^(\d+)$', views.detail),
    url(r'^search/', views.MySearchView())
]