# import datetime
from typing import List

# from course.models import *
from django.shortcuts import render


# from django.http import FileResponse, HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.
def index_view(request):
    class IndexFunction:
        def __init__(self, href, img_path, name):
            self.href = href
            self.img_path = img_path
            self.name = name

    funcs: List[IndexFunction] = []

    funcs += [
        IndexFunction("http://new.siae.top/", "/static/index/timetable1.svg", "课表"),
        IndexFunction("http://new.siae.top/#/classroom", "/static/index/freeClassroom.svg", "空闲教室"),
        IndexFunction("http://new.siae.top/#/exam", "/static/index/exam.svg", "考试安排"),
        IndexFunction("http://new.siae.top/#/news", "/static/index/query.svg", "更新日志"),
        IndexFunction("/admin/", "/static/index/admin.svg", "信息管理"),
        IndexFunction("https://siae.top/admin/#/admin/course/courseplan/", "/static/index/PDC.svg", "教学计划"),
        # IndexFunction("/course/api/", "/static/index/API.svg", "API"),
        # IndexFunction("/help/", "/static/index/info.svg", "使用帮助"),
    ]

    return render(request, "index/index.html", {"functions": [f.__dict__ for f in funcs]})
