from django.contrib import admin
from django.urls import path, include

from myApp.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contacts/', include('myApp.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('accounts.urls')),
]
