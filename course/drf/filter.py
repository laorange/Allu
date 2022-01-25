from typing import Dict

import django_filters

from .serializers import *


class MyFilter(django_filters.FilterSet):
    @classmethod
    def filter_for_field(cls, field, field_name, lookup_expr='exact'):
        filter_class = super().filter_for_field(field, field_name, lookup_expr)
        filter_class.extra['help_text'] = field.help_text
        return filter_class


class CourseTypeFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索课程类名')

    class Meta(CourseTypeSerializer.Meta):
        pass


class CourseInfoFilter(MyFilter):
    ch_name = django_filters.CharFilter(field_name='ch_name', lookup_expr='icontains', help_text='检索课程中文名')
    en_name = django_filters.CharFilter(field_name='en_name', lookup_expr='icontains', help_text='检索课程英语名')
    fr_name = django_filters.CharFilter(field_name='fr_name', lookup_expr='icontains', help_text='检索课程法语名')

    class Meta(CourseInfoSerializer.Meta):
        fields = CourseInfoSerializer.Meta.fields + ["ch_name", "en_name", "fr_name"]


class TeacherFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索教师姓名')

    class Meta(TeacherSerializer.Meta):
        pass


class GroupFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索分组名')

    class Meta(GroupSerializer.Meta):
        pass


class CoursePlanFilter(MyFilter):
    group_name = django_filters.CharFilter(field_name='groups__name', lookup_expr='icontains', help_text='检索分组名')

    class Meta(CoursePlanSerializer.Meta):
        fields = CoursePlanSerializer.Meta.fields + ["group_name"]


class ClassroomFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索教室名')

    class Meta(ClassroomSerializer.Meta):
        pass


class CourseChangeLogFilter(MyFilter):
    after = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='gte', help_text='更新时间不晚于...')
    before = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='lte', help_text='更新时间不早于...')
    description = django_filters.CharFilter(field_name='description', lookup_expr='icontains', help_text='检索变动描述')

    class Meta(CourseChangeLogSerializer.Meta):
        fields = ['log_id', 'plan', 'action', 'description', "after", "before"]


class CourseFilter(MyFilter):
    after = django_filters.DateFilter(field_name='date', lookup_expr='gte', help_text='上课时间不早于...')
    before = django_filters.DateFilter(field_name='date', lookup_expr='lte', help_text='上课时间不晚于...')

    update_after = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='gte', help_text='更新时间不早于...')
    update_before = django_filters.DateTimeFilter(field_name='update_time', lookup_expr='lte', help_text='更新时间不晚于...')

    type_id = django_filters.NumberFilter(field_name='plan__info__type_id', help_text='检索课程分类id')
    semester = django_filters.CharFilter(field_name='plan__info__semester', help_text='检索开课学期 ∈ [1,14]')
    ch_name = django_filters.CharFilter(field_name='plan__info__ch_name', lookup_expr='icontains', help_text='检索课程中文名')
    en_name = django_filters.CharFilter(field_name='plan__info__en_name', lookup_expr='icontains', help_text='检索课程英语名')
    fr_name = django_filters.CharFilter(field_name='plan__info__fr_name', lookup_expr='icontains', help_text='检索课程法语名')

    teacher_id = django_filters.NumberFilter(field_name='plan__teacher_id', help_text='检索老师id')
    teacher_name = django_filters.CharFilter(field_name='plan__teacher__name', lookup_expr='icontains', help_text='检索老师姓名')
    method = django_filters.CharFilter(field_name='plan__method', help_text='检索授课方式：Course/TD/TP/DS')

    class Meta(CourseSerializer.Meta):
        fields = ['course_id', 'plan', 'room', 'date', 'which_lesson',
                  "after", "before", "update_after", "update_before",
                  'type_id', 'semester', 'ch_name', 'en_name',
                  'fr_name', 'teacher_id', 'teacher_name', 'method']


# --------- EXTRA DETAIL (2D 3D...) ---------
class CoursePlan2dFilter(CoursePlanFilter):
    class Meta(CoursePlanFilter.Meta):
        pass


class CourseInfo2dFilter(CourseInfoFilter):
    class Meta(CourseInfoFilter.Meta):
        pass


class CourseInfo3dFilter(CourseInfo2dFilter):
    class Meta(CourseInfo2dFilter.Meta):
        pass


class Classroom2dFilter(ClassroomFilter):
    class Meta(ClassroomFilter.Meta):
        pass


class Group2dFilter(GroupFilter):
    class Meta(GroupFilter.Meta):
        pass


# region - Finally here is the drf_containers
_key = _value = ""
filters_dict: Dict[str, MyFilter] = {}
for _key, _value in locals().items():
    if _key.endswith("Filter") and _key != "MyFilter":
        filters_dict[_key.replace("Filter", '')] = _value

drf_containers: Dict[str, DrfContainer] = {}
for _serializer_key, _serializer in serializers_dict.items():
    if _serializer_key in filters_dict:
        drf_containers[_serializer_key] = DrfContainer(_serializer_key, _serializer.Meta.model,
                                                       _serializer, filters_dict[_serializer_key])
    else:
        drf_containers[_serializer_key] = DrfContainer(_serializer_key, _serializer.Meta.model, _serializer)
# endregion
