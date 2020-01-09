from django.urls import path
from . import views

urlpatterns =[
    path('', views.user_detail),
    path('login/', views.user_login),
    path('profile', views.profile),
    path('fabrics',views.fabric),
    path('work',views.work),
    path('viewdesigner',views.fn_viewdesigner),
    path('designerprof',views.fn_designer_details),
    path('logout', views.fn_logout),
    path('editprofile/', views.fn_edit_profile),
    path('viewfabrics',views.fn_viewfabrics)
]