from django.db import models
from multiselectfield import MultiSelectField
from datetime import datetime

size_choices=[
        ('XXS','XXS'),('XS','XS'),('XS-S','XS-S'),('M','M'),('M-L','M-L'),('L','L'),('XL','XL')
    ]

color_choices=[
        ('White','White'),('Black','Black'),('Red','Red'),('Grey','Grey'),('Blue','Blue'),('Green','Green'),('Yellow','Yellow')
    ]


class Product(models.Model):
    category_choices=[
        ('women','women'),('men','men'),('kids','kids'),('accessories','accessories'),('cosmetic','cosmetic')
                     ]
    type_choices=[
        ('coat','coat'),('jacket','jacket'),('dress','dress'),('shirt','shirt'),('T-shirt','T-shirt'),('jeans','jeans')
                ]

    category=models.CharField(max_length=15,choices=category_choices,default='women')
    type=models.CharField(max_length=15,choices=type_choices,default='coat')
    name=models.CharField(max_length=30)
    description=models.TextField()
    price=models.IntegerField()
    PriceAfterDiscount=models.IntegerField(default=0,verbose_name='If the product has discounts, what is the price after the discounts?')
    quantity=models.IntegerField()
    size=MultiSelectField(choices=size_choices)
    color=MultiSelectField(choices=color_choices) 
    image_one = models.ImageField(upload_to='images/%y/%m/%d/')
    image_two = models.ImageField(upload_to='images/%y/%m/%d/',blank=True,null=True)
    image_three = models.ImageField(upload_to='images/%y/%m/%d/',blank=True,null=True)
    image_four = models.ImageField(upload_to='images/%y/%m/%d/',blank=True,null=True)
    image_five = models.ImageField(upload_to='images/%y/%m/%d/',blank=True,null=True)   
    publish_date=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.category +' & ' +self.type+' & '+self.name +' & '+ str(self.size)
    
    