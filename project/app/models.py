from django.db import models
from django.shortcuts import reverse

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

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.post_index_value})

    class Meta:
        # Если managed = False, то Django не сможет редактировать базу данных
        managed = False
        # Порядок сортировки по выбранному полю
        ordering=['id']
        db_table = 'postindex'