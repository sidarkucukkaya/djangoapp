# urls.py adında bir dosya zaten blogprojesi2'nin altında var. Biz bu dosyayı sonradan oluşturduk ve article'ın içinde oluşturduk.

from django.contrib import admin
from django.urls import path
from . import views # nokta, şu an buradaki views'i al demek.

app_name = "article"

urlpatterns = [
    path("dashboard/",views.dashboard,name="dashboard"), # blog'dan gelen urls'teki path dosyasından bu işlemi yap. articles/dashboard/ görünce bizi Kontrol Paneli'ne götür. Buradaki amaç şu: articles/'tan gelen dashboard iki py dosyasını yönettik.
    path("addarticle/",views.addArticle,name="addarticle"), # addarticle linki
    path("article/<int:id>",views.detail,name="detail"),
    path("update/<int:id>",views.updateArticle,name="update"),
    path("delete/<int:id>",views.deleteArticle,name="delete"),
    path("",views.articles,name="articles"),    # blogprojesi2'nin altındaki urls.py'de biz zaten article'ı eklemiştik. O yüzden o kısmı boş bıraktık.
    path("comment/<int:id>",views.addComment,name="comment"),
]
