# -*- coding: utf-8 -*-
from django import forms
from .models import Student

# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性别', max_length=128)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.EmailField(label='邮箱', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手机号', max_length=128)


class StudentForm(forms.ModelForm):
    def clean_qq(self):
        clean_qq = self.cleaned_data['qq']
        if not clean_qq.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(clean_qq)

    class Meta:
        model = Student
        # fields = ['name', 'sex', 'profession', 'email', 'qq', 'phone']
        fields = '__all__'
        exclude = ['status']


