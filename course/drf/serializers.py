import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import serializers
from rest_framework import viewsets

from ..models import *
from django.db.models import Model

from django_filters.rest_framework import DjangoFilterBackend


def datetime_now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class DrfContainer:
    def __init__(self, name: str, model: Model, serializer: serializers.ModelSerializer, _filter=None):
        self.name = name
        self.model = model
        self.serializer = serializer
        self.filter = _filter
        self.view_set = self.get_view_set()

    def get_view_set(self):
        parent_class = viewsets.ModelViewSet if "forpost" in self.name.lower() else viewsets.ReadOnlyModelViewSet

        kwarg = dict(filter_backends=[DjangoFilterBackend],
                     authentication_classes=(CsrfExemptSessionAuthentication, BasicAuthentication),
                     # authentication_classes=(TokenAuthentication, CsrfExemptSessionAuthentication, BasicAuthentication),
                     queryset=self.model.objects.all(),
                     serializer_class=self.serializer) | ({"filter_class": self.filter} if self.filter else {})

        return type(self.name, (parent_class,), kwarg)  # 临时类型 🐂 🍻


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ['type_id', 'name', 'color']


class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = ['info_id', 'type', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name', 'color']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'name', 'validity']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_id', 'period', 'semester', 'name']


class GroupField(serializers.ModelSerializer):
    def to_internal_value(self, data):
        return Group.objects.get(id=data)

    class Meta:
        model = Group
        fields = ['group_id']


class CoursePlanSerializer(serializers.ModelSerializer):
    # @staticmethod
    # def get_groups(obj):
    #     for group in obj.groups.all():
    #         print(group.name)
    #
    #     return "&".join([group.name for group in obj.groups.all()])

    class Meta:
        model = CoursePlan
        fields = ['plan_id', 'teacher', 'info', 'groups', 'method', 'teacher_name',
                  'color', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['room_id', 'name', "is_common"]


class CourseChangeLogSerializer(serializers.ModelSerializer):
    # update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CourseChangeLog
        fields = ['log_id', 'plan', 'action', 'description', 'update_time',
                  'color', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name',
                  'method', 'group_ids', 'teacher_name']


class SemesterConfigSerializer(serializers.ModelSerializer):
    week1_monday_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    current_period_display = serializers.SerializerMethodField()

    @staticmethod
    def get_current_period_display(obj):
        return get_period_display(obj.current_period)

    class Meta:
        model = SemesterConfig
        fields = ["current_period", "current_period_display", "week1_monday_date", "max_week"]


class CourseSerializer(serializers.ModelSerializer):
    # update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Course
        fields = ['course_id', 'plan', 'room', 'date', 'which_lesson', 'note', 'update_time',
                  'color', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name',
                  'method', 'group_ids', 'teacher_name', 'room_name']


class CourseForPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['plan', 'room', 'date', 'which_lesson', 'update_time', "note"]


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['notice_id', 'content', 'link', "priority", 'validity', 'update_time']


# --------- EXTRA DETAIL (2D 3D...) ---------
class CoursePlan2dSerializer(CoursePlanSerializer):
    # plan_course = CourseSerializer(many=True, help_text="排课记录")

    class Meta(CoursePlanSerializer.Meta):
        fields = CoursePlanSerializer.Meta.fields + ["plan_course"]
        depth = 1


class CourseInfo2dSerializer(CourseInfoSerializer):
    # info_plan = CoursePlanSerializer(many=True, help_text="教学计划")

    class Meta(CourseInfoSerializer.Meta):
        fields = CourseInfoSerializer.Meta.fields + ["info_plan"]
        depth = 1


class CourseInfo3dSerializer(CourseInfo2dSerializer):
    info_plan = CoursePlan2dSerializer(many=True, help_text="教学计划")

    class Meta(CourseInfo2dSerializer.Meta):
        pass


class Classroom2dSerializer(ClassroomSerializer):
    # room_course = CourseSerializer(many=True, help_text="排课记录")

    class Meta(ClassroomSerializer.Meta):
        fields = ClassroomSerializer.Meta.fields + ["room_course"]
        depth = 1


class Group2dSerializer(GroupSerializer):
    group_plan = CoursePlan2dSerializer(many=True, help_text="教学计划")

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ["group_plan"]


class Course2dSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id', 'date', 'which_lesson', 'plan', 'room', 'update_time', "note"]
        depth = 3


# region - Finally here is the serializers_dict
_key = _value = ""
serializers_dict = {}
for _key, _value in locals().items():
    if _key.endswith("Serializer"):
        serializers_dict[_key.replace("Serializer", '')] = _value
# endregion
