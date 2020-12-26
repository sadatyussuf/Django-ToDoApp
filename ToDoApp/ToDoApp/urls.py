
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projectApp.urls')),
    path('apis/v1/', include('apis.urls')), # new
]
