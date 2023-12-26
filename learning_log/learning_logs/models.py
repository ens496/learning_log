from django.db import models


# Create your models here.
class Topic(models.Model):
    """A topic the user learning about"""
    # text adında bir charield tanımlıyoruz bu veritabanında bir sutun oluşturacaktır.Max karakter ise 200
    text = models.CharField(max_length=200)

    date_added = models.DateTimeField(auto_now_add=True)

    # Modelin string temsilini yazalım.
    def __str__(self):
        return self.text

#Topic (konular) altında belirli bir girdi girebilmek için Entry isimli model

class Entry(models.Model):
    """Something specific learnede about a topic"""
    #Foreignkey field'ı çoktan bire ilişkiyi temsil eder her entry bir tpoic ile ilişkilendirir.
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."