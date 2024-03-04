
from django.db import models
from django.utils.translation import gettext as _


class Typefutur(models.Model):
    """ ֆուտուռի տեսակները։ """
    names = models.CharField(max_length = 50, unique= True)
    slug = models.SlugField(max_length=50, unique=True)
    publish = models.BooleanField()

    class Meta:
        verbose_name = _('Մեր մասին')
        verbose_name_plural = _('Մեր մասին')

    def __str__(self):
        return f"{self.names} {self.publish}"
    
    
class TypeFuturNavigation(models.Model):
    
    names = models.CharField(max_length = 50, unique = True)
    discriptions = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank = True, null = True)
    img = models.ImageField(upload_to= 'mayin_img', blank = True, null = True)
    publish = models.BooleanField()
    caregory = models.ForeignKey(to = Typefutur, on_delete = models.PROTECT, related_name = 'cat_fut')

    class Meta:
        verbose_name= _('Նորություն աշխատանք ...')
        verbose_name_plural =_('Նորություններ աշխատանք ...') 

    def __str__(self):
        return f"{self.names} {self.publish}"

    def get_url(self):
        return f'{self.caregory.slug}/{self.slug}'
