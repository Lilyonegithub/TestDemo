from django.test import TestCase
from .models import Student
# Create your tests here.


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            name='Lily',
            sex=1,
            email='Lily@123.com',
            profession='程序员',
            qq='12333',
            phone='23344'
        )

    def test_create_and_sex_show(self):
        student = Student.objects.create(
            name='Lucy',
            sex=2,
            email='Lucy@123.com',
            profession='学生',
            qq='333333',
            phone='1133244'
        )
        self.assertEqual(student.sex_show, '男', '性别字段内容跟展示不一样！')

    def test_filter(self):
        Student.Object.create(
            name='Yin',
            sex=2,
            email='Yin@123.com',
            profession='学生',
            qq='22222222',
            phone='233232323'
        )
        name = 'Yin'
        students = Student.objects.filter(name=name)
        self.assertEqual(students.count(), 1, '应该值存在一个名称为{}的记录'.format(name))
