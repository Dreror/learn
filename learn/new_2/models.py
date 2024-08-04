from django.db import models


class Info(models.Model):
    title = models.CharField("Name", max_length=50)
    anons = models.CharField("Anons", max_length=250)
    full_text = models.TextField("Article")
    date = models.DateTimeField("Date")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/new_2/{self.id}"


    class Meta:
        verbose_name = "Info"
        verbose_name_plural = "Infos"
