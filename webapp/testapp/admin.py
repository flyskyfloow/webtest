# 后台，可以用很少量的代码就拥有一个强大的后台。注册数据模型到后台
from django.contrib import admin
from testapp.models import Person
from testapp.models import Article
admin.site.register(Person)
admin.site.register(Article)
