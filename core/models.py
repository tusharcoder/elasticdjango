# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-03-12T18:07:25+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-03-12T18:27:27+05:30



from django.db import models
from django.contrib.auth.models import User
import django.db.models.options as options
options.DEFAULT_NAMES=options.DEFAULT_NAMES+('es_index_name','es_type_name','es_mapping')

# Create your models here.
class Product(models.Model):
    """Product Model"""
    CHOICES=(('downloadable_product','DOWNLOADABLE PRODUCT'),('shipped_product','SHIPPED PRODUCT'))
    name=models.CharField(max_length=150)
    price=models.PositiveIntegerField(default=0)
    category=models.ForeignKey('Category')
    subcategory=models.ForeignKey('Subcategory')
    seller=models.ForeignKey('UserProfile')
    product_type=models.CharField(choices=CHOICES,max_length=50,default='downloadable_field')
    def __unicode__(self):
        return self.name
    def es_repr(self):
        data={
            "name":self.name,
            "price":self.price,
            "category":{
                "name": self.category.name,
            },
            "subcategory":{
                "name": self.subcategory.name,
            },
            "seller":{
                "email": self.seller.user.email,
            },
            "product_type":self.product_type
        }
        return data

    class Meta:
        es_index_name='ecommerce'
        es_type_name='products'
        es_mapping={
            'properties':{
                'name':{'type':'text'},
                'price':{'type':"long"},
                'category':{
                        'properties':{
                            'name':{'type':'keyword'},
                        }
                    },
                'subcategory':{
                        'properties':{
                            'name':{'type':'keyword'},
                        }
                    },
                'seller':{
                    'properties':{
                        'email':{'type':'text'}
                        }
                    },
                'product_type':{'type':"keyword"},
                }
        }

class Category(models.Model):
    """Category Model"""
    name=models.CharField(max_length=150)
    def __unicode__(self):
        return self.name

class Subcategory(models.Model):
    """Category Model"""
    name=models.CharField(max_length=150)
    category=models.ForeignKey(Category)
    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    """User Profile model"""
    CHOICES=(('vendor','VENDOR'),('consumer','CONSUMER'))
    user_type=models.CharField(choices=CHOICES,default='consumer',max_length=150)
    user=models.ForeignKey(User)
    def __unicode__(self):
        return self.user_type
