# from django.urls import path
# from . import views


# urlpatterns =[
#     path('index/', views.index, name='index'),
# ]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('product_list', views.product_list, name='product_list'),
# ]


# myapp/urls.py or project/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('product_list', views.product_list, name='product_list'),
    # Other paths for your application
]