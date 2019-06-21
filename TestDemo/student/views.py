from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.views import View
# Create your views here.


def index(request):
    # example1
    # students = Studet.objects.all()
    # return render(request, 'index.html', context={"students": students})

    # example2
    students = Student.get_all()
    if request.method == 'POST':
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.save()
            return HttpResponseRedirect(reverse('student:index'))
    else:
        studentForm = StudentForm()
    context = {
            "students": students,
            "studentForm": studentForm
    }
    return render(request, 'index.html', context=context)


class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = {
            'students': students
        }
        return context

    def get(self, request):
        context = self.get_context()
        studentForm = StudentForm()
        context.update({
            "studentForm": studentForm
        })
        return render(request, self.template_name, context=context)

    def post(self, request):
        studentForm = StudentForm(request.POST)
        if studentForm.is_valid():
            studentForm.save()
            return HttpResponseRedirect(reverse('student:index'))
        context = self.get_context()
        context.update({
            'studentForm': studentForm
        })
        return render(request, self.template_name, context=context)
