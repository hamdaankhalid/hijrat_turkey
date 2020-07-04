from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('migrate',views.migrate, name='migrate'),
    path('faq',views.faq, name='faq')
] 