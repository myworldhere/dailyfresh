from django.conf.urls import url
import views


urlpatterns = [
    url(r'^handle_cart/$', views.handle_cart),
    url(r'^place_order/$', views.place_order),
    url(r'^create_order/$', views.create_order),

]