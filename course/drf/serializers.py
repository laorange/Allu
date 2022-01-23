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

        return type(self.name.upper(), (TempViewSet,), dict(queryset=self.model.objects.all(),
                                                            serializer_class=self.serializer,
                                                            filter_class=self.filter))  # 临时类型 🐂 🍻


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
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class CoursePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePlan
        fields = '__all__'
        depth = 1


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class CourseChangeLogSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    plan = CoursePlanSerializer()

    class Meta:
        model = CourseChangeLog
        fields = '__all__'
        depth = 2


class SemesterConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SemesterConfig
        fields = ["current_period", "week1_monday_date"]


class CourseSerializer(serializers.ModelSerializer):
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Course
        fields = '__all__'
        depth = 3


# --------- EXTRA DETAIL (XD) ---------
class CoursePlanXDSerializer(CoursePlanSerializer):
    plan_course = CourseSerializer(many=True, help_text="排课记录")

    class Meta:
        model = CoursePlan
        fields = ['plan_id', 'teacher', 'info', 'groups', 'method', "plan_course"]
        depth = 1


class CourseInfoXDSerializer(CourseInfoSerializer):
    info_plan = CoursePlanSerializer(many=True, help_text="教学计划")

    class Meta:
        model = CourseInfo
        fields = ['info_id', 'type', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name', "info_plan"]
        depth = 1


class CourseInfoXXDSerializer(CourseInfoSerializer):
    info_plan = CoursePlanXDSerializer(many=True, help_text="教学计划")

    class Meta:
        model = CourseInfo
        fields = ['info_id', 'type', 'period', 'semester', 'code', 'ch_name', 'en_name', 'fr_name', "info_plan"]
        depth = 1


class ClassroomXDSerializer(ClassroomSerializer):

    class Meta:
        model = CoursePlan
        fields = ['plan_id', 'teacher', 'info', 'groups', 'method', "plan_course"]
        depth = 1


# class GroupXDSerializer(GroupSerializer):
#     group_plan = CoursePlanSerializer(many=True, help_text="教学计划")


# region - Finally here is the serializers_dict
_key = _value = ""
serializers_dict = {}  # Dict[str, serializers.ModelSerializer]
for _key, _value in locals().items():
    if _key.endswith("Serializer"):
        serializers_dict[_key.replace("Serializer", '')] = _value
# endregion
