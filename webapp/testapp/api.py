# rest api 定义区域
# 导入数据模型 中的类
from testapp.models import Person

# 序列化器，把数据包装成类似字典的格式
from rest_framework import serializers

# 这两个模块把序列化后的数据包装成 api
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 创建一个 Book 的序列化器
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person  # 序列化的对象
        fields = '__all__'  # 序列化的属性
        # fields = ('title', 'author')  # 如果只需要序列化某几个属性可以用元组


@api_view(['GET'])  # 装饰器，使得 book 函数具有 api_view 的相关方法
def person(request):
    person_list = Person.objects.all() # Person 的全部数据
    serializer = PersonSerializer(person_list, many=True) # 序列化 person 的数据
    return Response(serializer.data)

