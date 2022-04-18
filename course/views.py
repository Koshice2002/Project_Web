from django.shortcuts import render, redirect
from .models import Category, Course
from .forms import CategoryForm, CourseForm

# CRUD Category.


def category_index(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "course/category/category_index.html", context)


def category_details(request, id):
    category = Category.objects.get(id=id)
    context = {"category": category}
    return render(request, "course/category/category_details.html", context)


def category_delete(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect(category_index)


def category_add(request):
    form = CategoryForm(request.POST or None)

    if form.is_valid():
        category = Category()

        category.name = request.POST["name"]
        category.description = request.POST["description"]

        category.save()

        return redirect(category_index)

    context = {"form": form}

    return render(request, "course/category/category_add.html", context)


def category_edit(request, id):
    category = Category.objects.get(id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if form.is_valid():
        category.name = request.POST["name"]
        category.description = request.POST["description"]

        form.save()

        return redirect(category_index)

    context = {"form": form}

    return render(request, "course/category/category_edit.html", context)


def back_to_categorylist(request):
    return redirect(category_index)


# CRUD Course.
def course_index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }
    return render(request, "course/course/course_index.html", context)


def course_details(request, id):
    course = Course.objects.get(id=id)
    context = {
        "course": course,
    }
    return render(request, "course/course/course_details.html", context)


def course_delete(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect(course_index)


def course_add(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        course = Course()

        course.code = request.POST["code"]
        course.description = request.POST["description"]
        course.name_vi = request.POST["name_vi"]
        course.name_en = request.POST["name_en"]
        course.credit = request.POST["credit"]
        course.hour = request.POST["hour"]

        category = Category.objects.get(id=int(request.POST["category"]))
        course.category = category

        course.save()

        return redirect(course_index)

    context = {"form": form}

    return render(request, "course/course/course_add.html", context)


def course_edit(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        course.code = request.POST["code"]
        course.description = request.POST["description"]
        course.name_vi = request.POST["name_vi"]
        course.name_en = request.POST["name_en"]
        course.credit = request.POST["credit"]
        course.hour = request.POST["hour"]

        category = Category.objects.get(id=int(request.POST["category"]))
        course.category = category

        form.save()

        return redirect(course_index)

    context = {"form": form}

    return render(request, "course/course/course_add.html", context)


def back_to_courselist(request):
    return redirect(course_index)