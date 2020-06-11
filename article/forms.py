from django import forms    # formlarımızı dahil ettik.
from .models import Article # models.py'den Article'ı import ettik.

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content","article_image"]    # title ve content alanlarının input alanı olmasını istediğimiz için bu şekilde yazdık.
        
