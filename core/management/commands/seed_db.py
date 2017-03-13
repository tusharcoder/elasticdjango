# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-02-19T18:54:14+05:30
# @Email:  tamyworld@gmail.com
# @Filename: sample.py
# @Last modified by:   tushar
# @Last modified time: 2017-03-13T14:36:26+05:30



from django.core.management.base import BaseCommand
from model_mommy import mommy
import random
from core.models import *
from faker import Factory
from django.contrib.auth.models import User

faker = Factory.create()
def random_with_N_digits(n):
    """utility function to generate the random number of the length n"""
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)
class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('count', nargs=1, type=int)

    def handle(self, *args, **options):

        print("cleaning the database")
        Product.objects.all().delete()
        Category.objects.all().delete()
        Subcategory.objects.all().delete()
        UserProfile.objects.all().delete()
        users=User.objects.exclude(is_staff=True).delete()
        self.create_category()
        self.create_subcategpries()
        self.create_users()
        self.createProducts(options)
        print("production finished cheers:)")

    def createProducts(self,options):
        """function to create the products"""
        print( "finally, creating the products...")
        self.products=[]
        for i in range(options['count'][0]):
            price = random_with_N_digits(3)
            category=random.choice(self.categories)
            name='{}{} product'.format(faker.name(),category.name)
            subcategory=random.choice(list(filter(lambda x : x.category.name==category.name, self.subcategories)))
            seller=random.choice(self.userprofiles)
            product_type=random.choice(['downloadable_product','shipped_product'])
            product=mommy.prepare(Product,name=name,price=price,category=category,subcategory=subcategory,seller=seller,product_type=product_type)
            self.products.append(product)
        Product.objects.bulk_create(self.products)

    def create_category(self):
        """function to create the categories"""
        print( "categories...")
        _list=['books','toys','kitchenware','computer and accessories','mobile and tablets','clothing and Accessories','watches and eyeware']
        self.categories=[]
        for param in _list:
            category=mommy.make(Category,name=param)
            self.categories.append(category)
    def create_subcategpries(self):
        """function to create the sub categories"""
        print( "subcategories...")
        self.subcategories=[]
        for category in self.categories:
            sub_cat_name='{} {}'.format(faker.name(),category.name)
            subcategory=mommy.make(Subcategory, name=sub_cat_name, category=category)
            self.subcategories.append(subcategory)
    def create_users(self):
        """function to create the users"""
        print( "users...")
        self.userprofiles=[]
        domains=['gmail','outlook','yahoo','yahoo.co.in']
        for r in range(0,100):
            email = '{}{}@{}'.format(faker.name(),str(r),random.choice(domains))
            password=random_with_N_digits(10)
            user=User.objects.create_user(email,email,password)
            userprofile=mommy.make(UserProfile,user=user,user_type='vendor')
            self.userprofiles.append(userprofile)
