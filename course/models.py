from django.db import models
from uuslug import slugify

semester_choice = [('1', '大一上'), ('2', '大一下'),
                   ('3', '大二上'), ('4', '大二下'),
                   ('5', '大三上'), ('6', '大三下'),
                   ('7', "S1"), ('8', "S2"),
                   ('9', "S3"), ('10', "S4"),
                   ('11', "S5"), ('12', "S6"),
                   ('13', "S7"), ('14', "S8")]

method_choice = [("Course", "理论课"),
                 ("TD", "习题课"),
                 ("TP", "实验课"),
                 ("DS", "考试")]

which_lesson_choice = [("1", "第1,2节课"),
                       ("2", "第3,4节课"),
                       ("3", "第5,6节课"),
                       ("4", "第7,8节课"),
                       ("5", "第9,10节课")]

action_choice = [("Create", "新增"),
                 ("Update", "更新"),
                 ("Delete", "删除")]


# Create your models here.
class CourseType(models.Model):
    type_id = models.AutoField(primary_key=True, help_text="id")
    name = models.CharField(verbose_name="类型名", max_length=100, unique=True, help_text="类型名")
    color = models.CharField(verbose_name="颜色", max_length=6, help_text="颜色，六位字符，例如：FFFFFF")

    class Meta:
        verbose_name = '课程类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseInfo(models.Model):
    info_id = models.AutoField(primary_key=True, help_text="id")
    type = models.ForeignKey(verbose_name="课程类型", to=CourseType, on_delete=models.CASCADE,
                             related_name="type_info", help_text="FK-CourseType")
    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期")
    semester = models.CharField(verbose_name="学期", max_length=8, choices=semester_choice,
                                help_text="从大一上算起的第?学期 ∈ [1,14]")
    code = models.CharField(max_length=100, default='', help_text='课程编号(如CS21,ES22)', blank=True, null=True)
    ch_name = models.CharField(verbose_name="中文名", max_length=100, unique=True, help_text="课程中文名")
    en_name = models.CharField(verbose_name="English", max_length=100, help_text="课程英语名", blank=True, null=True)
    fr_name = models.CharField(verbose_name="Français", max_length=100, help_text="课程法语名", blank=True, null=True)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ch_name


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, help_text="id")
    name = models.CharField(verbose_name="姓名", max_length=100, unique=True, help_text="授课教师姓名")
    slug = models.CharField(max_length=300, blank=True, null=True)
    validity = models.BooleanField(verbose_name="是否生效", default=True, help_text="是否参与当前教学计划")

    class Meta:
        verbose_name = '授课教师'
        verbose_name_plural = verbose_name

    def save(self, **kwargs):
        slug = slugify(self.name)
        self.slug = slug if slug else f"teacher{self.teacher_id}"
        super(Teacher, self).save(**kwargs)

    def __str__(self):
        return self.name + f" ({self.slug})"


class Group(models.Model):
    group_id = models.AutoField(primary_key=True, help_text="id")
    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期")
    semester = models.CharField(verbose_name="学期", max_length=8, choices=semester_choice,
                                help_text="从大一上算起的第?学期 ∈ [1,14]")
    name = models.CharField(verbose_name="分组名称", max_length=100, help_text="分组名称，例如：PA")

    class Meta:
        verbose_name = '分组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CoursePlan(models.Model):
    plan_id = models.AutoField(primary_key=True, help_text="id")
    teacher = models.ForeignKey(verbose_name="授课教师", to="Teacher", on_delete=models.CASCADE,
                                related_name="teacher_plan", help_text="FK-Teacher")
    info = models.ForeignKey(verbose_name="课程信息", to="CourseInfo", on_delete=models.CASCADE,
                             related_name="info_plan", help_text="FK-CourseInfo")
    groups = models.ManyToManyField(verbose_name="分组", to="Group", related_name="group_plan", help_text="M2M Plan&Group")
    method = models.CharField(verbose_name="授课方式", max_length=8, choices=method_choice, help_text="Course/TD/TP/DS")

    class Meta:
        verbose_name = '教学计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "_".join([self.info.ch_name, self.get_method_display(), self.teacher.name])


class Classroom(models.Model):
    room_id = models.AutoField(primary_key=True, help_text="id")
    name = models.CharField(verbose_name="教室名", max_length=100, unique=True, help_text="教室名")

    class Meta:
        verbose_name = '教室'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseChangeLog(models.Model):
    log_id = models.AutoField(primary_key=True, help_text="id")
    plan = models.ForeignKey(verbose_name="教学计划", to="CoursePlan", on_delete=models.CASCADE,
                             related_name="plan_log", help_text="FK-CoursePlan")
    action = models.CharField(verbose_name="动作", max_length=8, choices=action_choice, help_text="新增/更新/删除")
    description = models.CharField(verbose_name="描述", max_length=255, help_text="对本次变动的描述", blank=True, null=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now_add=True, help_text='该变动发生的时间')

    class Meta:
        verbose_name = '课程更新日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.action + "：" + self.plan.__str__()


class SemesterConfig(models.Model):
    config_id = models.AutoField(primary_key=True, help_text="id")
    current_period = models.IntegerField(verbose_name="当前时期", help_text="从2007.9算起的第?学期")
    week1_monday_date = models.DateTimeField(verbose_name="更新时间", help_text="本学期第一周星期一的日期")

    class Meta:
        verbose_name = '学期信息配置'
        verbose_name_plural = verbose_name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True, help_text="id")
    plan = models.ForeignKey(verbose_name="教学计划", to="CoursePlan", on_delete=models.CASCADE,
                             related_name="plan_course", help_text="FK-CoursePlan")
    room = models.ForeignKey(verbose_name="教室", to="Classroom", on_delete=models.CASCADE,
                             related_name="room_course", help_text="FK-Classroom")
    date = models.DateField(verbose_name="这节课的上课日期", help_text="这节课的上课日期")
    which_lesson = models.CharField(verbose_name="第?节课", max_length=8, choices=which_lesson_choice, help_text="第?节课，∈[1,5]")
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, help_text='该条记录的更新时间')

    class Meta:
        verbose_name = '排课记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "_".join([self.date.strftime("%Y-%m-%d "), self.get_which_lesson_display(), self.plan.__str__()])
