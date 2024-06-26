from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

class Analytics(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, blank=True, null=True)
    analytics_code = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % (self.analytics_code)
    
    class Meta:
        verbose_name_plural = "Analytics"
