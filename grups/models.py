from django.db import models
from django.contrib.gis.db import models as gismodels
from django.utils.translation import gettext as _
from phone_field import PhoneField
from users.models import CustomUser



class ServisCategory(models.Model):
    """ Ընկերության տեսակները։ slug, names, image """

    names=models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="category_img", blank=True, null=True)

    class Meta:
        verbose_name = _("ծառայության տեսակ")
        verbose_name_plural = _("ծառայության տեսակներ")

    def __str__(self) -> str:
        return f"{self.names} {self.slug}"
    


class Company(models.Model):
    """ Ընկերություններ՝ names, specialcolumn , popularity, image, startwork, 
     stopwork, slug, category """
    
    names=models.CharField(max_length=50, unique=True)
    specialcolumn=models.CharField(max_length=50, blank=True, null=True)
    popularity = models.FloatField(default=5)
    image = models.ImageField(upload_to="grups_img", blank=True, null=True)
    startwork = models.TimeField(blank=True, null=True)
    stopwork = models.TimeField(blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    category = models.ForeignKey(to=ServisCategory, on_delete=models.PROTECT, related_name = 'cat_comp')

    class Meta:
        verbose_name = _("ընկերություն")
        verbose_name_plural = _("ընկերություններ")

    def __str__(self) -> str:
        return self.names


class CompanyDiscription(gismodels.Model):
    discription=models.TextField(blank=True, null=True)
    location=gismodels.MultiPolygonField()
    # geo_location = gismodels.PointField(srid=4326, null=True,blank=True)
    # geo_objects = gismodels.Manager()
    tel = PhoneField(blank=True, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    name = models.ForeignKey(to=Company, on_delete=models.PROTECT, related_name = 'grup')









class PopularityCompany(models.Model):
    """ Հաճախորդների գնահատականը ընկերություններին։ """
    gnahatakan = models.PositiveSmallIntegerField()
    post = models.TextField(blank=True, null=True)
    user = models.ForeignKey(to=CustomUser, on_delete=models.PROTECT, related_name = 'post')
    company = models.ForeignKey(to=Company, on_delete=models.PROTECT, related_name = 'ratings')

    class Meta:
        verbose_name = _("կարծիք")
        verbose_name_plural = _("կարծիքներ")

    def __str__(self) -> str:
        return self.post
    
