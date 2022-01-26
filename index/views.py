from typing import List

from django.shortcuts import render


# from django.http import FileResponse, HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.
def index_view(request):
    class IndexFunction:
        def __init__(self, href, img_path, name):
            self.href = href
            self.img_path = img_path
            self.name = name

    funcs: List[IndexFunction] = [
        IndexFunction("/course/", "/static/index/timetable.svg", "查看课表"),
        IndexFunction("/admin/", "/static/index/admin.svg", "信息管理"),
        IndexFunction("/course/api/", "/static/index/API.svg", "API"),
        IndexFunction("/help/", "/static/index/info.svg", "使用帮助"),
    ]

    return render(request, "index/index.html", {"functions": [f.__dict__ for f in funcs]})
