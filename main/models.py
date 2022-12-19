from django.db import models

class Teachers(models.Model):
    subject=models.CharField('Subject',max_length=50)
    first_name=models.CharField('First Name',max_length=50)
    second_name=models.CharField('Second Name',max_length=50)
    date=models.DateField('Date')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name='Учитель'
        verbose_name_plural='Учителя'

class Teacher(models.Model):
    subject=models.CharField('Subject',max_length=50)
    first_name=models.CharField('First Name',max_length=50)
    second_name=models.CharField('Second Name',max_length=50)
    date=models.DateField('Date')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name='Старый Учитель'
        verbose_name_plural='Старые Учителя'
