# templates klasörünün altındaki index.html'i oluşturduktan sonra bu klasörde sayfa yollarını belirtiyoruz.

"""blogprojesi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # include'u sonradan ekledik.
from article import views   # views.py de fonksiyon oluşturduktan sonra, o fonksiyonu burada birleştirmemiz gerekiyor.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),  # Anasayfayı görmek için (localhost:8000) direkt bu path'i yazıyoruz. 2. parametreye almak istediğimiz fonksiyonu yazıyoruz.
    path('about/', views.about,name="about"),    # Hakkımızda sayfası
    path('articles/', include("article.urls")),  # Burada şunu demek istedik: Eğer articles/ görürse, bizi direk articles'ın içindeki urls'e gönder.
    path('user/', include("user.urls")), # user/ ile başlayan adreslerimizde user'ın içindeki urls'e git
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)