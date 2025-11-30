from django.urls import path
from onlineproduce import views
from django.views.generic import TemplateView

app_name="onlineproduce"

urlpatterns = [
    path("ram/",views.name,name="ram"),
    path("home1/",views.new,name="home1"),
    path("product/",views.menu,name="product"),
    path("contact/",views.address,name="contact"),
    path("about/",views.info,name="about"),
    path("signin/",views.signin,name="signin"),
    path("signup/",views.signup,name="signup"),
    path("order/",views.payment,name="order"),
    path("success/",views.complete,name="success"),
    # path("placed/",views.details,name="placed"),
    path("home/",views.main,name='home'),
    path("enquiry/", views.enquiry_form, name="enquiry"),
    # path("signup/", views.signup, name="signup"),
    # path("signin/", views.signin, name="signin"),
    path("profile/", views.profile, name="profile"),
    # path('logout/', views.logout, name='logout')
    path("logout/", views.logout_view, name="logout"),





    
]