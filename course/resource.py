from import_export import resources
from .models import *


class CourseTypeResource(resources.ModelResource):
    class Meta:
        model = CourseType


class CourseInfoResource(resources.ModelResource):
    class Meta:
        model = CourseInfo


class TeacherResource(resources.ModelResource):
    class Meta:
        model = Teacher


class GroupResource(resources.ModelResource):
    class Meta:
        model = Group


class CoursePlanResource(resources.ModelResource):
    class Meta:
        model = CoursePlan


class ClassroomResource(resources.ModelResource):
    class Meta:
        model = Classroom


class CourseChangeLogResource(resources.ModelResource):
    class Meta:
        model = CourseChangeLog


class SemesterConfigResource(resources.ModelResource):
    class Meta:
        model = SemesterConfig


class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
