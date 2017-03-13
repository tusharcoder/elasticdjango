# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-03-12T17:59:10+05:30
# @Email:  tamyworld@gmail.com
# @Filename: urls.py
# @Last modified by:   tushar
# @Last modified time: 2017-03-12T18:42:07+05:30



from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
