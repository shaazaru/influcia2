from django.urls import path , include
from django import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from brand.views import BrandRegistration, brandlogin_view, BrandDashboardView, BrandHomeView


urlpatterns = [

    path('', BrandHomeView.as_view(template_name='brandhome.html'), name='home'),
    path('brandlogin_auth/', brandlogin_view),
    path('brandlogin/', auth_views.LoginView.as_view(template_name='brandlogin.html'),name='brandlogin'),
    path('brandregister/', BrandRegistration.as_view(), name='brandregister'),
    path('branddashboard/', BrandDashboardView.as_view(template_name='branddashboard.html'), name='branddashboard'),

]