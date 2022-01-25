from rest_framework import serializers
from rest_framework import viewsets

from ..models import *
from django.db.models import Model

from django_filters.rest_framework import DjangoFilterBackend


class DrfContainer:
    def __init__(self, name: str, model: Model, serializer: serializers.ModelSerializer, _filter=None):
        self.name = name
        self.model = model
        self.serializer = serializer
        self.filter = _filter
        self.view_set = self.get_view_set()

    def get_view_set(self):
        class TempViewSet(viewsets.ReadOnlyModelViewSet):
            filter_backends = [DjangoFilterBackend]

        kwarg = dict(queryset=self.model.objects.all(),
                     serializer_class=self.serializer) | ({"filter_class": self.filter} if self.filter else {})

        return type(self.name, (TempViewSet,), kwarg)  # 临时类型 🐂 🍻


class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ['type_id', 'name', 'color']


class CourseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInfo
        fields = ['info_id', 'type', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name']
        depth = 1


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'name', 'validity']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_id', 'period', 'semester', 'name']


# CoursePlan.objects.get().groups.all()
class CoursePlanSerializer(serializers.ModelSerializer):
    groups = serializers.SerializerMethodField()

    @staticmethod
    def get_groups(obj):
        for group in obj.groups.all():
            print(group.name)

        return "&".join([group.name for group in obj.groups.all()])

    class Meta:
        model = CoursePlan
        fields = ['plan_id', 'teacher', 'info', 'groups', 'method']
        depth = 1


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['room_id', 'name']


class CourseChangeLogSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    plan = CoursePlanSerializer()

    class Meta:
        model = CourseChangeLog
        fields = ['log_id', 'plan', 'action', 'description', 'update_time']
        depth = 2


class SemesterConfigSerializer(serializers.ModelSerializer):
    week1_monday_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    current_period_display = serializers.SerializerMethodField()

    @staticmethod
    def get_current_period_display(obj):
        return get_period_display(obj.current_period)

    class Meta:
        model = SemesterConfig
        fields = ["current_period", "current_period_display", "week1_monday_date"]


class CourseSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Course
        fields = ['course_id', 'plan', 'room', 'date', 'which_lesson', 'update_time']
        depth = 3


# --------- EXTRA DETAIL (2D 3D...) ---------
class CoursePlan2dSerializer(CoursePlanSerializer):
    plan_course = CourseSerializer(many=True, help_text="排课记录")

    class Meta(CoursePlanSerializer.Meta):
        fields = CoursePlanSerializer.Meta.fields + ["plan_course"]


class CourseInfo2dSerializer(CourseInfoSerializer):
    info_plan = CoursePlanSerializer(many=True, help_text="教学计划")

    class Meta(CourseInfoSerializer.Meta):
        fields = CourseInfoSerializer.Meta.fields + ["info_plan"]


class CourseInfo3dSerializer(CourseInfo2dSerializer):
    info_plan = CoursePlan2dSerializer(many=True, help_text="教学计划")

    class Meta(CourseInfo2dSerializer.Meta):
        pass


class Classroom2dSerializer(ClassroomSerializer):
    room_course = CourseSerializer(many=True, help_text="排课记录")

    class Meta(ClassroomSerializer.Meta):
        fields = ClassroomSerializer.Meta.fields + ["room_course"]


class Group2dSerializer(GroupSerializer):
    group_plan = CoursePlan2dSerializer(many=True, help_text="教学计划")

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ["group_plan"]


# region - Finally here is the serializers_dict
_key = _value = ""
serializers_dict = {}
for _key, _value in locals().items():
    if _key.endswith("Serializer"):
        serializers_dict[_key.replace("Serializer", '')] = _value
# endregion
