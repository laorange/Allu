import datetime

# from django.shortcuts import render
from .models import Classroom, SemesterConfig
from django.http.response import HttpResponseBadRequest, JsonResponse
from .drf.serializers import ClassroomSerializer


# Create your views here.
def advanced_classroom_api(request):
    try:
        all_classroom = Classroom.objects.all()
        semester_config = SemesterConfig.objects.get(config_id=1)

        weeks = [int(week) for week in request.GET.get("week", "").split(",") if week]

        what_days = [int(what_day) for what_day in request.GET.get("what_day", "").split(",") if what_day]

        which_lessons = [int(which_lesson) for which_lesson in request.GET.get("which_lesson", "").split(",") if which_lesson]
        if len(what_days) != len(which_lessons):
            raise Exception("what_day和which_lesson数量不相等")

        time_blocks = []
        for week in weeks:
            for _index, what_day in enumerate(what_days):
                time_blocks.append(
                    {"date": (semester_config.week1_monday_date + datetime.timedelta(days=7 * (week - 1) + what_day - 1)).date(),
                     "which_lesson": which_lessons[_index]}
                )

        for time_block in time_blocks:
            all_classroom = all_classroom.exclude(room_course__date=time_block["date"], room_course__which_lesson=time_block["which_lesson"])

        return JsonResponse(dict(results=ClassroomSerializer(instance=all_classroom, many=True).data,
                                 timeBlocks=time_blocks), safe=False)
    except Exception as e:
        return HttpResponseBadRequest(str(e))
