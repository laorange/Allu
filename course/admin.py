from django.contrib import admin
from .models import *

# 修改网页title和站点header
admin.site.site_title = "中欧航空工程师学院-课程管理系统"
admin.site.site_header = "SIAE-课程管理系统"


# Register your models here.
@admin.register(CourseType)
class CourseTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')


@admin.register(CourseInfo)
class CourseInfoAdmin(admin.ModelAdmin):
    list_display = ('period', "semester", 'type', 'ch_name', 'en_name', "fr_name")
    ordering = ['period', "semester", 'type']
    list_filter = ['period', "semester", 'type']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_delete_permission(self, *args):
        return False


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('period', "semester", "name")
    ordering = ['period', "semester", "name"]
    list_filter = ['period', "semester"]


@admin.register(CoursePlan)
class CoursePlanAdmin(admin.ModelAdmin):
    list_display = ('info', "method", "teacher")


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseChangeLog)
class CourseChangeLogAdmin(admin.ModelAdmin):
    # date_hierarchy = ['update_time']
    list_filter = ["update_time", "action"]
    ordering = ["-update_time"]


@admin.register(SemesterConfig)
class SemesterConfigAdmin(admin.ModelAdmin):
    list_display = ["current_period", "week1_monday_date"]

    def has_add_permission(self, *args):
        return False

    def has_delete_permission(self, *args):
        return False


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # add_form_template = ...
    # change_form_template = ...
    pass
