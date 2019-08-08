from django.conf.urls import url
import views


urlpatterns = [
    url(r'^cart$', views.cart),
    url(r'^cart_count/$', views.cart_count),
    url(r'^cart/add(\d+)_(\d+)/$', views.add_cart),
    url(r'^del_carts/(\d+)/$', views.del_carts),
    url(r'^cart/edit(\d+)_(\d+)/$', views.edit)
]