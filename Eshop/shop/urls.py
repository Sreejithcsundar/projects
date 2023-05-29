from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodetail, name='prod_cat_detail'),
    path('search', views.SearchResultsView, name='SearchResultsView'),
    path('checkout', views.checkout_view, name='checkout')

]
