#表单，用户在浏览器上输入数据提交，对数据的验证工作以及输入框的生成等工作
from django import forms
from .models import Person

# 对person 提交的表单进行过滤
class PersonForm(forms.Form):
    first_name = forms.CharField(required=True, min_length=5,label='留言标题')
    last_name = forms.CharField(required=True, min_length=5)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

