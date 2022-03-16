from django.db import models
from uuslug import slugify

semester_choice = [(1, '大一上'), (2, '大一下'), (3, '大二上'),
                   (4, '大二下'), (5, '大三上'), (6, '大三下'),
                   (7, "S1"), (8, "S2"), (9, "S3"), (10, "S4"),
                   (11, "S5"), (12, "S6"), (13, "S7"), (14, "S8")]

method_choice = [("Course", "理论课"),
                 ("TD", "习题课"),
                 ("TP", "实验课"),
                 ("Exam", "考试")]

which_lesson_choice = [(1, "第1,2节课"),
                       (2, "第3,4节课"),
                       (3, "第5,6节课"),
                       (4, "第7,8节课"),
                       (5, "第9,10节课")]

action_choice = [("Create", "新增"),
                 ("Update", "更新"),
                 ("Delete", "删除")]


def get_period_display(period: int):
    n1 = n2 = period // 2 + 7
    if period % 2:
        m1, m2, n2 = 9, 1, n2 + 1
    else:
        m1, m2 = 2, 7
    return f"20{n1:0>2}.{m1:0>2}~20{n2:0>2}.{m2:0>2}"


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

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(CourseType, self).save(force_insert, force_update, using, update_fields)
        for info in self.type_info.all():
            info.save()


class CourseInfo(models.Model):
    info_id = models.AutoField(primary_key=True, help_text="id")
    type = models.ForeignKey(verbose_name="课程类型", to=CourseType, on_delete=models.CASCADE,
                             related_name="type_info", help_text="FK-CourseType")
    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期")
    semester = models.IntegerField(verbose_name="学期", choices=semester_choice,
                                   help_text="从大一上算起的第?学期 ∈ [1,14]")
    code = models.CharField(max_length=100, default='', help_text='课程编号(如CS21,ES22)', blank=True, null=True)
    ch_name = models.CharField(verbose_name="中文名", max_length=100, unique=True, help_text="课程中文名")
    en_name = models.CharField(verbose_name="English", max_length=100, help_text="课程英语名", blank=True, null=True)
    fr_name = models.CharField(verbose_name="Français", max_length=100, help_text="课程法语名", blank=True, null=True)

    # CourseType 存在这儿的
    color = models.CharField(verbose_name="颜色", max_length=6, help_text="颜色，六位字符，例如：FFFFFF", blank=True, null=True)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"({self.period}){self.get_semester_display()} {self.ch_name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.color = self.type.color

        super(CourseInfo, self).save(force_insert, force_update, using, update_fields)
        for plan in self.info_plan.all():
            plan.save()


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True, help_text="id")
    name = models.CharField(verbose_name="姓名", max_length=100, unique=True, help_text="授课教师姓名")
    slug = models.CharField(max_length=300, blank=True, null=True)
    validity = models.BooleanField(verbose_name="是否生效", default=True, help_text="是否参与当前教学计划")

    class Meta:
        verbose_name = '授课教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + f" ({self.slug})"

    def save(self, **kwargs):
        slug = slugify(self.name)
        self.slug = slug if slug else f"teacher{self.teacher_id}"
        super(Teacher, self).save(**kwargs)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True, help_text="id")
    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期")
    semester = models.IntegerField(verbose_name="学期", choices=semester_choice,
                                   help_text="从大一上算起的第?学期 ∈ [1,14]")
    name = models.CharField(verbose_name="分组名称", max_length=100, help_text="分组名称，例如：PA")

    class Meta:
        verbose_name = '分组'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"({self.period}){self.get_semester_display()} " + self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(Group, self).save(force_insert, force_update, using, update_fields)
        for plan in self.group_plan.all():
            plan.save()


class CoursePlan(models.Model):
    plan_id = models.AutoField(primary_key=True, help_text="id")
    info = models.ForeignKey(verbose_name="课程信息", to="CourseInfo", on_delete=models.CASCADE,
                             related_name="info_plan", help_text="FK-CourseInfo")
    method = models.CharField(verbose_name="授课方式", max_length=8, choices=method_choice, help_text="Course/TD/TP/Exam")
    groups = models.ManyToManyField(verbose_name="分组", to="Group", related_name="group_plan", help_text="M2M Plan&Group")
    teacher = models.ForeignKey(verbose_name="授课教师", to="Teacher", on_delete=models.CASCADE,
                                related_name="teacher_plan", help_text="FK-Teacher", blank=True, null=True)

    # Teacher表 存这儿的
    teacher_name = models.CharField(verbose_name="授课教师姓名", max_length=100, help_text="授课教师姓名", blank=True, null=True)

    color = models.CharField(verbose_name="颜色", max_length=6, help_text="颜色，六位字符，例如：FFFFFF", blank=True, null=True)

    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期", blank=True, null=True)
    semester = models.IntegerField(verbose_name="学期", choices=semester_choice, blank=True, null=True,
                                   help_text="从大一上算起的第?学期 ∈ [1,14]")
    code = models.CharField(max_length=100, default='', help_text='课程编号(如CS21,ES22)', blank=True, null=True)
    ch_name = models.CharField(verbose_name="中文名", max_length=100, help_text="课程中文名", blank=True, null=True)
    en_name = models.CharField(verbose_name="English", max_length=100, help_text="课程英语名", blank=True, null=True)
    fr_name = models.CharField(verbose_name="Français", max_length=100, help_text="课程法语名", blank=True, null=True)

    class Meta:
        verbose_name = '教学计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        info_ls = [self.info.ch_name, self.get_method_display()]
        if self.teacher:
            info_ls.append(self.teacher.name)
        return "-".join(info_ls)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.teacher_name = self.teacher.name if self.teacher else None

        self.color = self.info.type.color
        self.period = self.info.period
        self.semester = self.info.semester
        self.code = self.info.code
        self.ch_name = self.info.ch_name
        self.en_name = self.info.en_name
        self.fr_name = self.info.fr_name

        super(CoursePlan, self).save(force_insert, force_update, using, update_fields)
        for course in self.plan_course.all():
            course.save()


class Classroom(models.Model):
    room_id = models.AutoField(primary_key=True, help_text="id")
    name = models.CharField(verbose_name="教室名", max_length=100, unique=True, help_text="教室名")
    is_common = models.BooleanField(verbose_name="是否自习室", default=True, help_text="是否可作为自习室")

    class Meta:
        verbose_name = '教室'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Classroom, self).save(force_insert, force_update, using, update_fields)
        for course in self.room_course.all():
            course.save()


class CoursePlanChildModel(models.Model):
    plan = models.ForeignKey(verbose_name="教学计划", to="CoursePlan", on_delete=models.CASCADE,
                             related_name="toBeOverwritten", help_text="FK-toBeOverwritten")

    # region 别的表储存在此处的信息
    color = models.CharField(verbose_name="颜色", max_length=6, help_text="颜色，六位字符，例如：FFFFFF", blank=True, null=True)

    period = models.IntegerField(verbose_name="时期", help_text="从2007.9算起的第?学期", blank=True, null=True)
    semester = models.IntegerField(verbose_name="学期", choices=semester_choice, blank=True, null=True,
                                   help_text="从大一上算起的第?学期 ∈ [1,14]")
    code = models.CharField(max_length=100, default='', help_text='课程编号(如CS21,ES22)', blank=True, null=True)
    ch_name = models.CharField(verbose_name="中文名", max_length=100, help_text="课程中文名", blank=True, null=True)
    en_name = models.CharField(verbose_name="English", max_length=100, help_text="课程英语名", blank=True, null=True)
    fr_name = models.CharField(verbose_name="Français", max_length=100, help_text="课程法语名", blank=True, null=True)

    method = models.CharField(verbose_name="授课方式", max_length=8, choices=method_choice, help_text="Course/TD/TP/Exam", default="Course")
    group_ids = models.CharField(verbose_name="分组", max_length=100, help_text="group_id(s),以字符串储存列表", blank=True, null=True)
    teacher_name = models.CharField(verbose_name="教师名", max_length=200, help_text="授课教师姓名", blank=True, null=True)

    # endregion

    def activate_trigger_of_save(self):
        self.color = self.plan.info.type.color
        self.period = self.plan.info.period
        self.semester = self.plan.info.semester
        self.code = self.plan.info.code
        self.ch_name = self.plan.info.ch_name
        self.en_name = self.plan.info.en_name
        self.fr_name = self.plan.info.fr_name
        self.method = self.plan.method
        self.group_ids = str([group.group_id for group in self.plan.groups.all()])
        self.teacher_name = self.plan.teacher.name if self.plan.teacher else None

    class Meta:
        abstract = True


class CourseChangeLog(CoursePlanChildModel):
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

    def save(self, *args, **kwargs):
        self.activate_trigger_of_save()
        super(CourseChangeLog, self).save(*args, **kwargs)


class Course(CoursePlanChildModel):
    course_id = models.AutoField(primary_key=True, help_text="id")
    plan = models.ForeignKey(verbose_name="教学计划", to="CoursePlan", on_delete=models.CASCADE,
                             related_name="plan_course", help_text="FK-CoursePlan")
    room = models.ForeignKey(verbose_name="教室", to="Classroom", on_delete=models.CASCADE,
                             related_name="room_course", help_text="FK-Classroom", blank=True, null=True)
    date = models.DateField(verbose_name="这节课的上课日期", help_text="这节课的上课日期")
    which_lesson = models.IntegerField(verbose_name="第?节课", choices=which_lesson_choice, help_text="第?节课，∈[1,5]")
    note = models.CharField(verbose_name="备注", max_length=255, blank=True, null=True, default=None, help_text="补充说明")
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, help_text='这条记录的更新时间')

    # 别的表储存在此处的信息
    room_name = models.CharField(verbose_name="教室名", max_length=100, help_text="教室名", blank=True, null=True)

    # endregion

    class Meta:
        verbose_name = '排课记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "_".join([self.date.strftime("%Y-%m-%d "), self.get_which_lesson_display(), self.plan.__str__()])

    def delete(self, *args, **kwargs):
        description = f"删除：{self.date}{self.get_which_lesson_display()}的{self.plan}"
        CourseChangeLog.objects.create(plan_id=self.plan_id, action="Delete", description=description)
        return super(Course, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if old := Course.objects.filter(course_id=self.course_id):
            old = old[0]
            description = ""
            if self.plan_id != old.plan_id:
                description = f"变更：{self.date}{self.get_which_lesson_display()}的{old.plan}变更为{self.plan}"
            elif (self.date != old.date or self.which_lesson != old.which_lesson) and self.plan_id == old.plan_id:
                description = f"调课：原{old.date}{old.get_which_lesson_display()}的{self.plan}，调到{self.date}{self.get_which_lesson_display()}"
            elif self.room_id != old.room_id and self.plan_id == old.plan_id:
                description = f"换教室：{self.date}{self.get_which_lesson_display()}的{self.plan}，从{old.room}换到{self.room}"
            if description:
                CourseChangeLog.objects.create(plan_id=old.plan_id, action="Update", description=description)
        else:
            description = f"新增：{self.date}{self.get_which_lesson_display()}的{self.plan}"
            CourseChangeLog.objects.create(plan_id=self.plan_id, action="Create", description=description)

        self.activate_trigger_of_save()
        self.room_name = self.room.name if self.room else None

        return super(Course, self).save(*args, **kwargs)


class SemesterConfig(models.Model):
    config_id = models.AutoField(primary_key=True, help_text="id")
    current_period = models.IntegerField(verbose_name="当前时期", help_text="从2007.9算起的第?学期")
    week1_monday_date = models.DateTimeField(verbose_name="学期开始日期", help_text="本学期第一周星期一的日期")
    max_week = models.IntegerField(verbose_name="最大周数", default=20, help_text="本学期共计多少周")

    class Meta:
        verbose_name = '学期信息配置'
        verbose_name_plural = verbose_name


class Notice(models.Model):
    notice_id = models.AutoField(primary_key=True, help_text="id")
    content = models.CharField(verbose_name="描述", max_length=255, help_text="对本次变动的描述")
    link = models.TextField(verbose_name="链接", help_text="点击通知时跳转链接", blank=True, null=True)
    priority = models.IntegerField(verbose_name="优先级", help_text="数字越大优先级越高", default=1)
    validity = models.BooleanField(verbose_name="是否生效", default=True, help_text="是否生效")
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True, help_text='这条记录的更新时间')

    class Meta:
        verbose_name = '系统通知'
        verbose_name_plural = verbose_name
