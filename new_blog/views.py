import datetime
import random
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.shortcuts import render
from new_blog.models import Blog, Comment  # importing models


def date_view(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))


def random_view(request):
    random_int = random.randint(1, 100)
    return HttpResponse(random_int)


def create_blog(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        title = data["title"]
        description = data["description"]
        image = files["image"]
        blog = Blog.objects.create(title=title, description=description, image=image)
        context = {"image": request.FILES.get('image'), 'title': title, 'description': description}
        return HttpResponse("Блог успешно добавлен ")
    elif request.method == "GET":
        return render(request, 'blog_form.html')


def detail_post(request, id):
    try:
        blog = Blog.objects.get(id=id)
    except Exception:
        return render(request, 'not_found.html')
    if request.method == "POST":
        text = request.POST.get("comment", None)
        if not text:
            comments = Comment.objects.filter(blog_id=id)
            return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})
        else:
            Comment.objects.create(text=text, blog=blog)
            comments = Comment.objects.filter(blog_id=id)
            return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})
    elif request.method == "GET":
        comments = Comment.objects.filter(blog_id=id)
        return render(request, "blog_detail.html", context={"blog": blog, "comments": comments})


def test_form(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        first_name = data["first_name"]
        last_name = data["last_name"]
        return HttpResponse(f"ваше имя {first_name} ваша фамилиия {last_name}")
    elif request.method == "GET":
        return render(request, "form.html")


def blog_view(request):
    blogs = Blog.objects.all()

    return render(request, 'blog.html', context={"blogs": blogs})


def profile_view(request):
    user = request.user

    return HttpResponse(
        f"username: {user.username}, password: {user.password}, name: {user.first_name}, surname: {user.last_name}")


def blog_change_view(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        if data.get("title"):
            blog.title = data["title"]
        if data.get("description"):
            blog.description = data["description"]
        if file.get("image"):
            blog.image = file["image"]
        blog.save()
        return HttpResponseRedirect(f"/blog/{blog.id}")
    elif request.method == "GET":
        context = {"blog": blog}
        return render(request, "blog_change.html", context)
    elif request.method == "GET":
        context = {"blog": blog}
        return render(request, "blog_change.html",context)
