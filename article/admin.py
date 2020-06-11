from django.contrib import admin
from .models import Article,Comment # models.py dosyasında oluşturduğumuz class'ı burada import ettik.

# Register your models here.

#admin.site.register(Article)    # Article class'ını admin panelinde göstermek için bu fonksiyonu kullandık.
admin.site.register(Comment)

@admin.register(Article)    # Oluşturduğumuz decorator, yukarıdaki metodla aynı işlevi görür. Django, decorator kullanımını önerir.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]   # list_display ile Article bölümümüzde hem başlık, hem de yazar adı görünmesini istedik. Aksi takdirde sadece başlık kısmı görünecekti.
    list_display_links = ["title","created_date"]   # Normal şartlarda sadece makalenin başlığının üzerinde limk vardı ve bu linke tıklayarak biz makaleye ulaşabiliyorduk. Biz bu özelliği 'Oluşturulma Tarihi'ne de ekledik.
    search_fields = ["title"]   # Bu özellikle 'title'a göre arama bölümü oluşturabiliriz.
    list_filter = ["created_date"]  # Bu özellikle Oluşturulma Tarihi'ne göre ekranın sağ tarafında süzgeç oluştur
    class Meta:
        model = Article