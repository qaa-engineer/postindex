from django.db import models

# Create your models here.
class Name(models.Model):
    name_value=models.CharField(max_length=100)

    def __str__(self):
        return self.name_value

# База данных почтовых индексов
class Postindex(models.Model):
    id = models.BigAutoField(primary_key=True)
    post_index_value = models.IntegerField(blank=True, null=True)
    post_name = models.TextField(blank=True, null=True)
    post_type = models.TextField(blank=True, null=True)
    post_sub = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    autonomy = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    city_1 = models.TextField(blank=True, null=True)
    actual_date = models.DateField(blank=True, null=True)
    index_old = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'postindex'
