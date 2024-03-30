from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.group, name="groups")
    path('', views.account_login, name="accounts"),
    path('logout/', views.account_logout, name="logout"),
    path('register/', views.register, name="register"),
    path('reset_password/', views.reset_password, name="reset_password"),
    path('new_password/', views.new_password, name="new_password"),
    path('enter_number/', views.enter_number, name="enter_number"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)