from django.db import models
from django.contrib.gis.db import models as gismodels
from django.contrib.postgres.indexes import GinIndex
from django.utils.translation import gettext as _

class locationAvailable(gismodels.Model):
    """այն քաղաքներն են որտեղ հասանելի է ծառայությունը։ 
    sity։քաղաքի անվանումը, location multypolygon քաղաքի մակերեսը։ """
    sity = models.CharField(max_length = 50 , db_index = True)
    location=gismodels.MultiPolygonField()
    objects = gismodels.Manager()

    class Mete:
        indexes=[
            GinIndex(name = 'NewGinIndex',fields=['sity'])
        ]
        verbose_name = _("Բնակավայր")
        verbose_name_plural = _("Բնակավայրեր")

    def __str__(self):
        return self.sity




class Street(gismodels.Model):
    """ ճանապարհների աղյուսակ՝ name` անվանումը։ geometry: ճահապարհի կորդինատները """
    sity = models.ForeignKey(to=locationAvailable,
                             on_delete=models.PROTECT, 
                             related_name = 'street')
    name = models.CharField(max_length = 200, db_index = True)
    geometry = gismodels.MultiLineStringField( blank=True, null=True)

    class Mete:
        indexes=[
            GinIndex(name = 'NewGinIndex',fields=['name'])
        ]
        verbose_name = _("Ճանապարհ")
        verbose_name_plural = _("Ճանապարներ")
    def __str__(self):
        return self.name
    


class Building(gismodels.Model):
    """ շինություն պարունակում է sity->քաղաքի աղյուսակ stret -> ճահապարհի աղյուսակ 
     adres -> շինության Հասցեն center_point -> շինության կենտրոնը։ geometry -> շինության պոլիգոնը։ """
    sity = models.ForeignKey(to=locationAvailable,
                             on_delete=models.PROTECT, 
                             related_name = 'buildings')
    
    stret = models.ForeignKey(to=Street,
                             on_delete=models.PROTECT, 
                             related_name = 'buildings')
    adres = models.CharField(max_length = 70, db_index = True)
    center_point = gismodels.PointField()
    geometry=gismodels.PolygonField()

    class Mete:
        indexes=[
            GinIndex(name = 'NewGinIndex',fields=['adres'])
        ]
        varbose_name = _('Շինություն')
        varbose_name_plural = _('Շինություններ')

    def __str__(self):
        return self.adres



class search_model(models.Model):
    txt = models.TextField(max_length = 300, db_index = True)
    sity = models.ForeignKey(to=locationAvailable,
                             on_delete=models.PROTECT, 
                             related_name = 'src')
    
    stret = models.ForeignKey(to=Street,
                             on_delete=models.PROTECT, 
                             related_name = 'src')
    
    class Mete:
        indexes=[
            GinIndex(name = 'NewGinIndex',fields=['txt'])
        ]
        varbose_name = _('որոնման տվըալ')
        varbose_name_plural = _('որոնման տվյալներ')

    def __str__(self):
        return self.txt