from django.urls import path


# Add path to link with config/urls.py under the app directory e.g,
#     path('app/', include('app.urls')),

# Add app urls.py

# 1. Add URL e.g,   ## * Typical case stile kebab-case
# * for ListView: 'course-list/'
# * for DetailView: 'course-detail/<init:pk>/'

# 2. Add a view name followed by.as_view() e.g., ##* PascalCase
# * for ListView: CourseList.as_view()

# 3. Add URL name e.g., #* snake_case
# * for ListView: 'course_list'

# urlpatterns = [path("URL", ViewName.as_view(), name="URL name")]
