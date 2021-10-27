from django.db import models

# Create your models here.


class Planilha(models.Model):

    class Meta:
        verbose_name = "Planilha"
        verbose_name_plural = "Planilhas"
        ordering = ["id"]

    external_key = models.CharField(max_length=255, null=False, blank=False)
    client_name = models.CharField(max_length=255, null=False, blank=False)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
    data = models.TextField(max_length=2555555555, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#{}".format(self.external_key)
