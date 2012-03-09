from django.db import models


class Model(models.Model):

    char = models.CharField('Char field', max_length=100)
    decimal = models.DecimalField('Decimal field', decimal_places=2, max_digits=10)
    float = models.FloatField('Float field')
    integer = models.IntegerField('Integer field')
    email = models.EmailField('Email field')
    ip = models.IPAddressField('IP address field')
    text = models.TextField('Text field')

    boolean = models.BooleanField('Boolean field')
    null_boolean = models.NullBooleanField('Null boolean field')

    date = models.DateField('Date field')
    time = models.TimeField('Time field')
    datetime= models.DateTimeField('Datetime field')

    file = models.FileField('File field', upload_to='media')
    file_path = models.FilePathField('File path field')
    image = models.ImageField('Image field', upload_to='media')

    class Meta:
        verbose_name = 'Test record'
