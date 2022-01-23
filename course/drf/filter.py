from typing import Dict

import django_filters

from .serializers import *


class MyFilter(django_filters.FilterSet):
    @classmethod
    def filter_for_field(cls, field, field_name, lookup_expr='exact'):
        filter_class = super().filter_for_field(field, field_name, lookup_expr)
        filter_class.extra['help_text'] = field.help_text
        return filter_class


class TeacherFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索教师姓名')

    class Meta:
        model = Teacher
        fields = ['teacher_id', 'name']


class CourseTypeFilter(MyFilter):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', help_text='检索课程类名')

    class Meta:
        model = CourseType
        fields = ["type_id", "name"]


# region - Finally here is the drf_containers
_key = _value = ""
filters_dict: Dict[str, serializers.ModelSerializer] = {}
for _key, _value in locals().items():
    if _key.endswith("Filter"):
        filters_dict[_key.replace("Filter", '')] = _value

drf_containers: Dict[str, DrfContainer] = {}
for _serializer_key, _serializer in serializers_dict.items():
    if _serializer_key in filters_dict:
        drf_containers[_serializer_key] = DrfContainer(_serializer_key, _serializer.Meta.model,
                                                       _serializer, filters_dict[_serializer_key])
    else:
        drf_containers[_serializer_key] = DrfContainer(_serializer_key, _serializer.Meta.model, _serializer)
# endregion
