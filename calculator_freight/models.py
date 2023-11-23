from django.db import models

class Stevedoring(models.Model):
    portname = models.CharField(blank=True, max_length=200)
    stevedoring_1 = models.FloatField(default=0)
    stevedoring_2 = models.FloatField(default=0)
    stevedoring_3 = models.FloatField(default=0)
    stevedoring_nodriver_1 = models.FloatField(default=0)
    stevedoring_nodriver_2 = models.FloatField(default=0)
    stevedoring_nodriver_3 = models.FloatField(default=0)

    def __str__(self):
        return f'{self.portname}'

class FreightParams(models.Model):
    route = models.CharField(max_length=200)
    freight = models.FloatField(default=0)
    freight_nodriver = models.FloatField(default=0)
    BAF = models.FloatField(default=0)
    ISPS = models.FloatField(default=0)
    freightForwarding = models.FloatField(default=0)
    transitdecl = models.FloatField(default=0)
    el_connection = models.FloatField(default=0)
    seconddriver = models.FloatField(default=0)
    ADR = models.FloatField(default=0)
    stevedoring_pol = models.ManyToManyField(Stevedoring, blank=True, related_name='stevpol')
    stevedoring_pod = models.ManyToManyField(Stevedoring, blank=True, related_name='stevpod')

    def __str__(self):
        return f'{self.route}'





