from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favorites/', include('favorites.urls')),
    path('', lambda request: HttpResponseRedirect('/favorites/')),  # 기본 페이지를 favorites로 리디렉션
]