from django.db import models

STATUS_CHOICES = (
    ('n', 'New'),
    ('p', 'In process'),
    ('t', 'Tested'),
)

class Method(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date = models.DateField()

    def __unicode__(self):
        return "%s, %s created %s " %(self.name, self.status, self.date)
