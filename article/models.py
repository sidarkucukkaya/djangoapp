from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Article(models.Model):    # article uygulaması için oluşturduğumuz model class'ı
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar") # Oluşturduğumuz author alanının veritabanındaki auth.User alanına ait olduğu belirttik. Aynı zamanda bu alan silinirse eğer on_delete komutuyla veritabanından da silineceğini belirttik. ForeignKey, bir modeli başka bir modelle ilişkilendirmemizi sağlar.
    title = models.CharField(max_length=50, verbose_name="Başlık") # Başlık. verbose_name komutu, bizim admin panelinde görmek istediğimiz şekilde ekler. Mesela Title yerine Başlık yazılır.
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")  # Veritabanına bir veri eklendiğinde o an ki tarihi vermesi için auto_now_add komutunu kullandık.
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekleyin")  # Fotoğraf Ekleme
    def __str__(self):
        return self.title   # Bu fonksiyon sayesinde ekli olan makaleler 'Article object(1)' yerine makalenin başlığıyla görüntülenecek. Yazar bilgisini görmek istiyorsak title yerine author yazabiliriz.
    
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments") # related_name ile /article/comments'e ulaşabiliriz.
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=500,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content # site yönetiminde başlık olarak yorumu görmek için bu yapılabilir

    class Meta:
        ordering = ['-comment_date']
