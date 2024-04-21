from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.group, name="groups")
    path('profile', views.profile, name="profile"),
    path('home', views.home, name="home"),
    path('camera', views.camera, name="camera"),
    path('chat', views.chat, name="chat"),
    path('searchCarNumber', views.searchCarNumber, name="searchCarNumber"),
    path('process_image', views.process_image, name="process_image"),
    path('recentReportedCars', views.recentReportedCars, name="recentReportedCars"),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)