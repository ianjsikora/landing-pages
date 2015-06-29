from django.db import models

class Page(models.Model):
    url_string = models.CharField(max_length=200)
    image = models.ImageField()
    link = models.URLField(null=True)

    def __unicode__(self):
        return u"{}".format(self.url_string, self.image, self.link)