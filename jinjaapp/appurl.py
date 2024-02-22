from django.urls import path
from jinjaapp import views

urlpatterns = [
    path('', views.index, name='Homepage'),
    path('About/', views.about, name='AboutPage'),
    path('Contact/', views.contact, name='ContactPage'),
    path('Gallery/', views.gallery, name='GalleryPage')
]
