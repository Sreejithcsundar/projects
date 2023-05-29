from django.urls import path

from cartapp import views

app_name = 'cartapp'
urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.Cart_Remove, name='Cart_Remove'),
    path('full_remove/<int:product_id>/', views.Full_Remove, name='Full_Remove')

]
