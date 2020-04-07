from django.db import models

# Create your models here.
class Name(models.Model):
    name_value=models.CharField(max_length=100)

    def __str__(self):
        return self.name_value

# База данных почтовых индексов
class AppData(models.Model):
    post_index = models.IntegerField(blank=True, null=True)
    opsname = models.CharField(max_length=100, blank=True, null=True)
    opstype = models.CharField(max_length=100, blank=True, null=True)
    opssubm = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    autonom = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    city_1 = models.CharField(max_length=100, blank=True, null=True)
    actdate = models.DateField(blank=True, null=True)
    indexold = models.IntegerField(blank=True, null=True)

    class Meta:
        # Удалите строку `managed = False`, если вы хотите разрешить Django создавать, изменять и удалять таблицу
        managed = False
        # Не стесняйтесь переименовывать модели, но не переименовывайте значения db_table или имена полей
        db_table = 'app_data'
