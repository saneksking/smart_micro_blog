from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=50)
    site_description = models.TextField(default='')

    def __str__(self):
        return self.site_name
