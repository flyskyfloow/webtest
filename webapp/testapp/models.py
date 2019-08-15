# 与数据库操作相关，存入或读取数据时用到这个
from django.db import models
# from django.db import migrations

# 在数据库app增加一张表 表名 serverinfo 自动转换为小写url
class ServerInfo(models.Model):
    hostname = models.CharField(max_length=255, blank=True, null=True)
    cpu = models.IntegerField(unique=True)
    mem = models.IntegerField(unique=True)
    ip = models.CharField(max_length=255, blank=True, null=True)

# 在数据库app增加一张表 表名 Person 自动转换为小写2
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name, self.first_name


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

