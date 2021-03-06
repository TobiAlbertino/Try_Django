from django.urls import path
from .views import home, products, customer, createOrder, deleteOrder, updateOrder, registerPage, loginPage, logoutUser, userPage, accountSettings

app_name = 'accounts'

urlpatterns = [
    path('register/', registerPage, name="register"),
	path('login/', loginPage, name="login"),  
	path('logout/', logoutUser, name="logout"),

    path('', home, name='home'),
    path('user/', userPage, name="user-page"),

    path('account/', accountSettings, name="account"),

    path('products/', products, name='products'),
    path('customer/<int:pk_test>/', customer, name='customer'),

    path('create_order/<int:pk>/', createOrder, name="create_order"),
    path('update_order/<int:pk>/', updateOrder, name="update_order"),
    path('delete_order/<int:pk>/', deleteOrder, name="delete_order"),
]