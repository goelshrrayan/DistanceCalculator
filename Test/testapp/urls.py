from django.conf.urls import url
from . import views


urlpatterns = [
    # General ChatBot
    url(r'^create-update-shop', views.CreateUpdateShop),
    url(r'^get-shop-data', views.GetShop),
    url(r'^delete-shop', views.DeleteShop),
    url(r'^shop-form', views.ShopForm),
    url(r'^submit-shop-form', views.SubmitShopForm),
    
    
]    