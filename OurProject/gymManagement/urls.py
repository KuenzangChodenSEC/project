from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('plan/', views.plan, name='plan'),
    path('whyjoinus/', views.why_join_us, name='why_join_us'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('admin-page/', views.admin_page, name='admin_page'),
    path('pfp/', views.profile_page, name='pfp'),
    path('viewplan/', views.view_plan, name='view_plan'),
    path('viewpayment/', views.view_payment, name='view_payment'),
    path('viewmembers/', views.view_members, name='view_members'),
    path('inventory/', views.inventory, name='inventory'),
    path('update_payment_status/', views.update_payment_status, name='update_payment_status'),

]
