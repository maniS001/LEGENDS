from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('albert',views.albert ,name='albert'), 
    path('elon', views.elon ,name='elon'),
    path('tesla', views.tesla ,name='tesla'),
    path('abdul kalam', views.abdul ,name='abdul'),
   
    
] 

urlpatterns =urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 