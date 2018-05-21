from django.conf.urls import url
from . import views

urlpatterns = [
    # === POST ROUTES ===
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^sell$', views.sell),
    url(r'^logout$', views.logout),

    # === GET ROUTES ===
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^dashboard/(?P<user_id>\d+)$', views.dashboard),
    url(r'^shoes$', views.shoes),
    url(r'^buy/(?P<product_id>\d+)$', views.buy),
    url(r'^remove/(?P<product_id>\d+)$', views.remove),
]
