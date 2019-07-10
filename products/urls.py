from django.conf.urls import url, include
from .views import all_products,product_detail

urlpatterns = [
    url(r'^$', all_products,name='index'),
    url(r'^product/(?P<id>\d+)/$', product_detail,name='productdetail'),

]