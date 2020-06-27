from django.urls import path , include
from django import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from influencer.views import InfluencerRegistration, influencerlogin_view, InfluencerHomeView, InfluencerDashboardView



urlpatterns = [

    path('', InfluencerHomeView.as_view(template_name='influencerhome.html'),name='influencerhome'),
    path('influencerlogin_auth/', influencerlogin_view),
    path('influencerlogin/',auth_views.LoginView.as_view(template_name='influencerlogin.html'), name='influencerlogin'),
    path('influencerregister/', InfluencerRegistration.as_view(),name='influencerregister'),
    path('influencerdashboard/', InfluencerDashboardView.as_view(template_name='influencerdashboard.html'),name='influencerdashboard'),

]