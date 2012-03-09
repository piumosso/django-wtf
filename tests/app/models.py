from django.db import models


class Model(models.Model):

    char = models.CharField('Char field', max_length=100)
    decimal = models.DecimalField('Decimal field', decimal_places=2, max_digits=10, null=True, blank=True)
    float = models.FloatField('Float field', null=True, blank=True)
    integer = models.IntegerField('Integer field', null=True, blank=True)
    email = models.EmailField('Email field', null=True, blank=True)
    ip = models.IPAddressField('IP address field', null=True, blank=True)
    text = models.TextField('Text field', null=True, blank=True)

    boolean = models.BooleanField('Boolean field')
    null_boolean = models.NullBooleanField('Null boolean field', null=True, blank=True)

    date = models.DateField('Date field', null=True, blank=True)
    time = models.TimeField('Time field', null=True, blank=True)
    datetime= models.DateTimeField('Datetime field', null=True, blank=True)

    file = models.FileField('File field', upload_to='media', null=True, blank=True)
    file_path = models.FilePathField('File path field', null=True, blank=True)
    image = models.ImageField('Image field', upload_to='media', null=True, blank=True)

    class Meta:
        verbose_name = 'Test record'
