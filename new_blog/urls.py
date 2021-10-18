from django.urls import path
from .views import date_view, random_view, blog_view, test_form, create_blog, detail_post
from . import views

urlpatterns = [
    path("", blog_view),
    path("<int:id>",detail_post),
    path("date", date_view),
    path("random", random_view),
    path("view",test_form),
    path("create",create_blog),

]
