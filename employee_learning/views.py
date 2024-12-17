from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import LearningCourse
from django.urls import reverse_lazy


class CourseList(ListView):
    
    # model = LearningCourse
    queryset = LearningCourse.objects.order_by('-title')
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'

class CourseDetail(DetailView):
    template_name = 'employee_learning/course_detail.html'
    model = LearningCourse
    context_object_name = 'course_object'

class CourseCreate(CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

class CourseUpdate(UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

class CourseDelete(DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')