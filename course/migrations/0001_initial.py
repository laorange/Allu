# Generated by Django 3.2.8 on 2022-01-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('room_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='教室名', max_length=100, unique=True)),
            ],
            options={
                'verbose_name': '教室',
                'verbose_name_plural': '教室',
            },
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('info_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('period', models.IntegerField(help_text='从2007.9算起的第?学期')),
                ('semester', models.CharField(choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', max_length=8)),
                ('code', models.CharField(blank=True, default='', help_text='课程编号(如CS21,ES22)', max_length=100, null=True)),
                ('ch_name', models.CharField(help_text='课程中文名', max_length=100, unique=True)),
                ('en_name', models.CharField(blank=True, help_text='课程英语名', max_length=100, null=True)),
                ('fr_name', models.CharField(blank=True, help_text='课程法语名', max_length=100, null=True)),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('type_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='类型名', max_length=100, unique=True)),
                ('color', models.CharField(help_text='颜色，六位字符，例如：FFFFFF', max_length=6)),
            ],
            options={
                'verbose_name': '课程类型',
                'verbose_name_plural': '课程类型',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('period', models.IntegerField(help_text='从2007.9算起的第?学期')),
                ('semester', models.CharField(choices=[(1, '大一上'), (2, '大一下'), (3, '大二上'), (4, '大二下'), (5, '大三上'), (6, '大三下'), (7, 'S1'), (8, 'S2'), (9, 'S3'), (10, 'S4'), (11, 'S5'), (12, 'S6'), (13, 'S7'), (14, 'S8')], help_text='从大一上算起的第?学期 ∈ [1,14]', max_length=8)),
                ('name', models.CharField(help_text='分组名称，例如：PA', max_length=100)),
            ],
            options={
                'verbose_name': '分组',
                'verbose_name_plural': '分组',
            },
        ),
        migrations.CreateModel(
            name='SemesterConfig',
            fields=[
                ('config_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('current_period', models.IntegerField(help_text='从2007.9算起的第?学期')),
                ('week1_monday_date', models.DateTimeField(help_text='本学期第一周星期一的日期')),
            ],
            options={
                'verbose_name': '学期信息配置',
                'verbose_name_plural': '学期信息配置',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='授课教师姓名', max_length=100, unique=True)),
                ('validity', models.BooleanField(default=True, help_text='是否参与当前教学计划')),
                ('slug', models.SlugField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': '授课教师',
                'verbose_name_plural': '授课教师',
            },
        ),
        migrations.CreateModel(
            name='CoursePlan',
            fields=[
                ('plan_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('method', models.CharField(choices=[('理论课', 'Course'), ('习题课', 'TD'), ('实验课', 'TP'), ('考试', 'DS')], help_text='授课方式', max_length=8)),
                ('groups', models.ManyToManyField(help_text='M2M Plan&Group', related_name='group_plan', to='course.Group')),
                ('info', models.ForeignKey(help_text='FK-CourseInfo', on_delete=django.db.models.deletion.CASCADE, related_name='info_plan', to='course.courseinfo')),
                ('teacher', models.ForeignKey(help_text='FK-Teacher', on_delete=django.db.models.deletion.CASCADE, related_name='teacher_plan', to='course.teacher')),
            ],
            options={
                'verbose_name': '教学计划',
                'verbose_name_plural': '教学计划',
            },
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='type',
            field=models.ForeignKey(help_text='FK-CourseType', on_delete=django.db.models.deletion.CASCADE, related_name='type_info', to='course.coursetype'),
        ),
        migrations.CreateModel(
            name='CourseChangeLog',
            fields=[
                ('log_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('action', models.CharField(choices=[('Create', '新增'), ('Update', '更新'), ('Delete', '删除')], help_text='新增/更新/删除', max_length=8)),
                ('description', models.CharField(blank=True, help_text='对本次变动的描述', max_length=255, null=True)),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='该变动发生的时间')),
                ('plan', models.ForeignKey(help_text='FK-CoursePlan', on_delete=django.db.models.deletion.CASCADE, related_name='plan_log', to='course.courseplan')),
            ],
            options={
                'verbose_name': '课程更新日志',
                'verbose_name_plural': '课程更新日志',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(help_text='id', primary_key=True, serialize=False)),
                ('date', models.DateField(help_text='这节课的上课日期')),
                ('which_lesson', models.CharField(choices=[('1', '第1,2节课'), ('2', '第3,4节课'), ('3', '第5,6节课'), ('4', '第7,8节课'), ('5', '第9,10节课')], help_text='第?节课，∈[1,5]', max_length=8)),
                ('plan', models.ForeignKey(help_text='FK-CoursePlan', on_delete=django.db.models.deletion.CASCADE, related_name='plan_course', to='course.courseplan')),
                ('room', models.ForeignKey(help_text='FK-Classroom', on_delete=django.db.models.deletion.CASCADE, related_name='room_course', to='course.classroom')),
            ],
            options={
                'verbose_name': '排课记录',
                'verbose_name_plural': '排课记录',
            },
        ),
    ]
