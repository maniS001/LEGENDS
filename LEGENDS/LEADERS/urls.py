from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.data ,name='data'),
    path("login",views.login,name='login'),
    path("details",views.details,name='details')
]

urlpatterns =urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 