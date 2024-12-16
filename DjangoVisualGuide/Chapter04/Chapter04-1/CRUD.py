# # for list page
# # for Detail page
# # for Create page
# # for Update page
# # for Delete page
# # add five urls patterns each view
# # add five Views using Generic Views
# # create 5 template
# # list.html
# # detail.html
# # create.html
# # update.html
# # delite.html

# from django.views.generic import ListView
# from .models import MyModel
# # 1. Import generic views and models used in this view
# # 2. Create a new view using a generic view
# # 3. Set'attribute values' for each attribute defined for each generic view
# # 4. Customize the generic view(e.g., set a new context)

# class MyView(ListView):
#     template_name = "list.html"
#     model = MyModel

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["now"] = timezone.now()
#         return context
