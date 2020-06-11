# Bu app için oluşturacağımız formları buraya ekliyoruz.

from django import forms    # Formumuzu dahil ettik.

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,label="Kullanıcı Adı") # label:Nasıl görüneceği
    password = forms.CharField(max_length=20,label="Parola",widget=forms.PasswordInput) # widget:Parola gösterimi(*)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget=forms.PasswordInput)

    def clean(self):    # clean, Django için üretilen bir fonksiyon. password ve confirm'in eşit olup olmamasını kontrol edecek.
        username = self.cleaned_data.get("username")    # Önce, kullancının yukarda girdiği değerleri almasını sağlıyoruz.
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar uyumlu değil!")  # Hata fırlatma

        values = {
            "username" : username,
            "password" : password
        }   # Eğer girilen değerleri döndürmek istiyorsak mutlaka sözlük tipinde yazmalıyız.
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(label="Parola",widget=forms.PasswordInput)

