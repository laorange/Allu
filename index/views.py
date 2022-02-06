import datetime
from typing import List

from course.models import *
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

    semester_config = SemesterConfig.objects.get(config_id=1)
    # semester_config.current_period
    period_b = 1 - (semester_config.current_period % 2)
    # week = (semester_config.week1_monday_date - datetime.now()).min // 10080 + 1
    now = datetime.datetime.now()
    weekday = now.isoweekday()
    after = (datetime.datetime.now() - datetime.timedelta(days=weekday - 1)).strftime("%Y-%m-%d")
    before = (datetime.datetime.now() + datetime.timedelta(days=7 - weekday)).strftime("%Y-%m-%d")

    funcs += [
        IndexFunction(f"/course/api/Course/?format=json&semester={semester + period_b}&after={after}&before={before}",
                      f"/static/index/timetable{_index + 1}.svg",
                      semester_choice[semester + period_b - 1][1]) for _index, semester in enumerate(range(1, 12, 2))
    ]

    funcs += [
        IndexFunction("/", "/static/index/freeClassroom.svg", "空闲教室"),
        IndexFunction("/", "/static/index/PDC.svg", "教学计划"),
        IndexFunction("/", "/static/index/exam.svg", "考试安排"),
        IndexFunction("/admin/", "/static/index/admin.svg", "信息管理"),
        IndexFunction("/course/api/", "/static/index/API.svg", "API"),
        IndexFunction("/help/", "/static/index/info.svg", "使用帮助"),
    ]

    return render(request, "index/index.html", {"functions": [f.__dict__ for f in funcs]})
