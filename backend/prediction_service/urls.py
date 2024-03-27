# predict_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='predict'),
    path('list_images/', views.list_images, name='list_images'),
    path('churn_predict_decrypt/', views.churn_predict_decrypt, name='list_images'),
    # path('list_images_compare/', views.list_images, name='list_images_compare'),

]
