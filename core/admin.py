# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-03-12T18:07:25+05:30
# @Email:  tamyworld@gmail.com
# @Filename: admin.py
# @Last modified by:   tushar
# @Last modified time: 2017-03-12T18:32:24+05:30



from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Subcategory)
admin.site.register(Category)
admin.site.register(Product)
