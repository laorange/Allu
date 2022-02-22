import os
from datetime import datetime

import django
from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProjectSettings.settings')

django.setup()

from course.models import *

teacher_list = [["1", "Adil", "adil"],
                ["2", "Caroline", "caroline"],
                ["3", "Eric", "eric"],
                ["4", "Joël", "joel"],
                ["5", "Julien", "julien"],
                ["6", "关静", "guan-jing"],
                ["7", "何永勃", "he-yong-bo"],
                ["8", "刘东亮", "liu-dong-liang"],
                ["9", "刘成盼", "liu-cheng-pan"],
                ["10", "刘文然", "liu-wen-ran"],
                ["11", "史磊", "shi-lei"],
                ["12", "周航", "zhou-hang"],
                ["13", "周隽", "zhou-jun"],
                ["14", "姚佳伟", "yao-jia-wei"],
                ["15", "孔庆国", "kong-qing-guo"],
                ["16", "孙凤鸣", "sun-feng-ming"],
                ["17", "宋肖肖", "song-xiao-xiao"],
                ["18", "庞勇", "pang-yong"],
                ["19", "张亚娟", "zhang-ya-juan"],
                ["20", "张鸿", "zhang-hong"],
                ["21", "李俊仙", "li-jun-xian"],
                ["22", "李双宝", "li-shuang-bao"],
                ["23", "李湘萍", "li-xiang-ping"],
                ["24", "李静", "li-jing"],
                ["25", "杜娟", "du-juan"],
                # ["26", "杨新湦", "yang-xin-sheng"],
                ["27", "武婧岚", "wu-jing-lan"],
                ["28", "牛一凡", "niu-yi-fan"],
                ["29", "王亚如", "wang-ya-ru"],
                ["30", "王付胜", "wang-fu-sheng"],
                ["31", "王剑", "wang-jian"],
                ["32", "王坤", "wang-kun"],
                ["33", "王彬", "wang-bin"],
                ["34", "王玥", "wang-yue"],
                ["35", "王瑞昕", "wang-rui-xin"],
                ["36", "王萱", "wang-xuan"],
                ["37", "田俊改", "tian-jun-gai"],
                ["38", "罗旭", "luo-xu"],
                ["39", "胡艳敏", "hu-yan-min"],
                ["40", "胡雪兰", "hu-xue-lan"],
                ["41", "苏志刚", "su-zhi-gang"],
                ["42", "裴昕", "pei-xin"],
                ["43", "贾惟", "jia-wei"],
                ["44", "邓甜", "deng-tian"],
                ["45", "陈亚军", "chen-ya-jun"],
                ["46", "陈嘉楠", "chen-jia-nan"],
                ["47", "马霁", "ma-ji"],
                ["48", "谷瑞娟", "gu-rui-juan"],
                ["49", "马锐", "ma-rui"],
                ["50", "Thomas", "thomas"],
                ["51", "张艳峰", "zhang-yan-feng"],
                ["52", "李文", "li-wen"],
                ["53", "陈佳音", "chen-jia-yin"],
                ["54", "陈慧军", "chen-hui-jun"],
                ["55", "高远", "gao-yuan"],
                ["56", "程海波", "cheng-hai-bo"],
                ["57", "---", "None"]]

classroom_ls = [(1, '107'), (2, '108'), (3, '120'), (4, '122'), (5, '201'), (6, '207'), (7, '208'), (8, '210'),
                (9, '212'), (10, '220'), (11, '309'), (12, '310'), (13, '312'), (14, '314'), (15, '323'),
                (16, '409'),
                (17, '410'), (18, '412'), (19, '414'), (20, '422')]

class_descriptions = [(5, 0, 1, 'A', 'AB班'), (6, 1, 1, 'A', 'A班'), (7, 1, 1, 'B', 'B班'), (8, 2, 1, 'A', 'PA'),
                      (9, 2, 1, 'B', 'PB'), (10, 2, 1, 'C', 'PC'), (11, 2, 1, 'D', 'PD'), (12, 3, 1, 'A', 'FA'),
                      (13, 3, 1, 'B', 'FB'), (14, 3, 1, 'C', 'FC'), (15, 3, 1, 'D', 'FD'), (16, 3, 1, 'E', 'FE'),
                      (17, 0, 2, 'A', 'AB班'), (18, 1, 2, 'A', 'A班'), (19, 1, 2, 'B', 'B班'), (20, 2, 2, 'A', 'PA'),
                      (21, 2, 2, 'B', 'PB'), (22, 2, 2, 'C', 'PC'), (23, 2, 2, 'D', 'PD'), (24, 3, 2, 'A', 'FA'),
                      (25, 3, 2, 'B', 'FB'), (26, 3, 2, 'C', 'FC'), (27, 3, 2, 'D', 'FD'), (28, 3, 2, 'E', 'FE'),
                      (29, 0, 3, 'A', 'AB班'), (30, 1, 3, 'A', 'A班'), (31, 1, 3, 'B', 'B班'), (32, 2, 3, 'A', 'PA'),
                      (33, 2, 3, 'B', 'PB'), (34, 2, 3, 'C', 'PC'), (35, 2, 3, 'D', 'PD'), (36, 3, 3, 'A', 'FA'),
                      (37, 3, 3, 'B', 'FB'), (38, 3, 3, 'C', 'FC'), (39, 3, 3, 'D', 'FD'), (40, 3, 3, 'E', 'FE'),
                      (41, 0, 4, 'A', 'AB班'), (42, 1, 4, 'A', 'A班'), (43, 1, 4, 'B', 'B班'), (44, 2, 4, 'A', 'PA'),
                      (45, 2, 4, 'B', 'PB'), (46, 2, 4, 'C', 'PC'), (47, 2, 4, 'D', 'PD'), (48, 3, 4, 'A', 'FA'),
                      (49, 3, 4, 'B', 'FB'), (50, 3, 4, 'C', 'FC'), (51, 3, 4, 'D', 'FD'), (52, 3, 4, 'E', 'FE'),
                      (53, 0, 5, 'A', 'AB班'), (54, 1, 5, 'A', 'A班'), (55, 1, 5, 'B', 'B班'), (56, 2, 5, 'A', 'PA'),
                      (57, 2, 5, 'B', 'PB'), (58, 2, 5, 'C', 'PC'), (59, 2, 5, 'D', 'PD'), (60, 3, 5, 'A', 'FA'),
                      (61, 3, 5, 'B', 'FB'), (62, 3, 5, 'C', 'FC'), (63, 3, 5, 'D', 'FD'), (64, 3, 5, 'E', 'FE'),
                      (65, 0, 6, 'A', 'AB班'), (66, 1, 6, 'A', 'A班'), (67, 1, 6, 'B', 'B班'), (68, 2, 6, 'A', 'PA'),
                      (69, 2, 6, 'B', 'PB'), (70, 2, 6, 'C', 'PC'), (71, 2, 6, 'D', 'PD'), (72, 3, 6, 'A', 'FA'),
                      (73, 3, 6, 'B', 'FB'), (74, 3, 6, 'C', 'FC'), (75, 3, 6, 'D', 'FD'), (76, 3, 6, 'E', 'FE'),
                      (77, 0, 7, 'A', 'All'), (80, 3, 7, 'A', 'GR.A'), (81, 3, 7, 'B', 'GR.B'),
                      (82, 3, 7, 'C', 'GR.C'),
                      (83, 3, 7, 'D', 'GR.D'), (84, 0, 8, 'A', 'All'), (87, 3, 8, 'A', 'GR.A'),
                      (88, 3, 8, 'B', 'GR.B'),
                      (89, 3, 8, 'C', 'GR.C'), (90, 3, 8, 'D', 'GR.D'), (91, 0, 9, 'A', 'All'),
                      (94, 3, 9, 'A', 'GR.A'),
                      (95, 3, 9, 'B', 'GR.B'), (96, 3, 9, 'C', 'GR.C'), (97, 3, 9, 'D', 'GR.D'),
                      (98, 0, 10, 'A', 'All'),
                      (101, 3, 10, 'A', 'GR.A'), (102, 3, 10, 'B', 'GR.B'), (103, 3, 10, 'C', 'GR.C'),
                      (104, 3, 10, 'D', 'GR.D'), (105, 4, 10, 'A', 'AG'), (106, 4, 10, 'B', 'SM'),
                      (107, 4, 10, 'C', 'PS'), (108, 0, 11, 'A', 'All'), (111, 3, 11, 'A', 'GR.A'),
                      (112, 3, 11, 'B', 'GR.B'), (113, 3, 11, 'C', 'GR.C'), (114, 3, 11, 'D', 'GR.D'),
                      (115, 4, 11, 'A', 'AG'), (116, 4, 11, 'B', 'SM'), (117, 4, 11, 'C', 'PS'),
                      (118, 0, 12, 'A', 'All'), (121, 3, 12, 'A', 'GR.A'), (122, 3, 12, 'B', 'GR.B'),
                      (123, 3, 12, 'C', 'GR.C'), (124, 3, 12, 'D', 'GR.D'), (125, 4, 12, 'A', 'AG'),
                      (126, 4, 12, 'B', 'SM'), (127, 4, 12, 'C', 'PS')]

lesson_type = [(1, '未分类', '#ffffff'), (2, '预科数学', '#CCFFFF'), (3, '预科物理化学', '#FFFF99'), (4, '预科法语', '#ffffff'),
               (5, '预科英语', '#FF99CC'),
               (6, "Engineering Mathematics  工程数学", "#FF99FF"),
               (7, "Electronics Engineering  电子工程", "#FFFF00"),
               (8, "Aircraft Structure  飞机结构", "#00B0F0"),
               (9, "Aeronautical Materials 航空材料", "#00B0F0"),
               (10, "Fluid Mechanics  流体力学", "#F79646"),
               (11, "Heat Transfer  传热学", "#FF5B5B"),
               (12, "Engineering Sciences  工程科学", "#00B050"),
               (13, "Human Sciences  人文科学", "#EBF1DE"),
               (14, "English & French  外语", "#CECECE"),
               (15, "Internship & Experiment 实习实验", "#ffffff"),
               (16, "Computer Sciences  计算机科学", "#9934CD"),
               (17, "Propulsion Systems  推进系统", "#F79646"),
               (18, "Air Traffic Management   空中交通管理", "#ffffff"),
               (19, "Air Ground Systems  地空系统", "#ffffff")]

lesson_list = [['09402001', '', '体育（1）', '1', '1'],
               ['15401004', '', '走进民航', '1', '1'],
               ['16402001', '', '中国近现代史纲要及实践', '1', '1'],
               ['52409001', '', '军训', '1', '1'],
               ['60411120', 'Advanced Mathematics I', '高等数学（1）', '1', '2'],
               ['60411220', 'Fundamental Physics （1）', '基础物理（1）', '1', '3'],
               ['60411321', 'Basic French 1', '基础法语（1）', '1', '4'],
               ['60411322', 'College English 1', '大学英语（1）', '1', '5'],
               ['09402002', '', '体育（2）', '2', '1'],
               ['16402004', '', '思想道德修养与法律基础及实践', '2', '1'],
               ['52401002', '', '军事理论', '2', '1'],
               ['60411121', 'Advanced Mathematics II', '高等数学（2）', '2', '2'],
               ['60411221', 'Fundamental Physics （2）', '基础物理（2）', '2', '3'],
               ['60411323', 'Basic French 2', '基础法语（2）', '2', '4'],
               ['60411324', 'College English 2', '大学英语（2）', '2', '5'],
               ['60411325', 'Scientific French', '科技法语', '2', '4'],
               ['60411501', '', '大学美育', '2', '1'],
               ['', '', '形势与政策（1）', '2', '1'],
               ['09402003', '', '体育（3）', '3', '1'],
               ['16401001', '', '毛泽东思想和中国特色社会主义理论体系概论（1）', '3', '1'],
               ['60411122', 'Advanced Mathematics III', '高等数学（3）', '3', '2'],
               ['60411222', 'General physics (1)', '普通物理（上）', '3', '3'],
               ['60411226', 'Chemistry (1)', '化学（1）', '3', '3'],
               ['60411326', 'Intermediate French 1', '中级法语（1）', '3', '4'],
               ['60411327', 'College English 3', '大学英语（3）', '3', '5'],
               ['60413220', 'Physics Experiments I', '物理实验 I（1）', '3', '3'],
               ['60416001', 'Cognitive Internship', '认知实习', '3', '1'],
               ['09402004', '', '体育（4）', '4', '1'],
               ['16402002', '', '马克思主义基本原理概论及实践', '4', '1'],
               ['16402003', '', '毛泽东思想和中国特色社会主义理论体系概论（2）', '4', '1'],
               ['60411123', 'Advanced Mathematics IV', '高等数学（4）', '4', '2'],
               ['60411223', 'General physics (2)', '普通物理（下）', '4', '3'],
               ['60411227', 'Chemistry (2)', '化学（2）', '4', '3'],
               ['60411328', 'Intermediate French 2', '中级法语（2）', '4', '4'],
               ['60411329', 'College English 4', '大学英语（4）', '4', '5'],
               ['60413216', 'Electric and Electronic Experiments', '电子电工实验', '4', '1'],
               ['', '', '形势与政策（2）', '4', '1'],
               ['16401002', '', '习近平新时代中国特色社会主义思想概论', '5', '1'],
               ['60411124', 'Advanced Mathematics V', '高等数学（5）', '5', '2'],
               ['60411224', 'Classical physics (1)', '经典物理（上）', '5', '3'],
               ['60411228', 'Chemistry (3)', '化学（3）', '5', '3'],
               ['60411331', 'Comprehensive English 1', '综合英语（1）', '5', '5'],
               ['60411335', 'Intermediate French 3', '中级法语（3）', '5', '4'],
               ['60411336', 'French expression methodology 1', '法语写作与表达（1）', '5', '4'],
               ['60412407', 'Computer programming', '计算机编程', '5', '1'],
               ['60412408', 'Engineering Drawing', '工程制图', '5', '1'],
               ['60413222', 'Characterized physics Experiment', '特色物理实验', '5', '3'],
               ['60411125', 'Advanced Mathematics VI', '高等数学（6）', '6', '2'],
               ['60411225', 'Classical physics (2)', '经典物理（下）', '6', '3'],
               ['60411229', 'Chemistry (4)', '化学（4）', '6', '3'],
               ['60411333', 'Comprehensive English 2', '综合英语（2）', '6', '5'],
               ['60411337', 'Intermediate French 4', '中级法语（4）', '6', '4'],
               ['60411338', 'French expression methodology 2', '法语写作与表达（2）', '6', '4'],
               ['60412409', 'Complex Analysis', '复变函数', '6', '1'],
               # ['60412825', 'Applied Thermodynamics', '工程热力学', '6', '1'],
               ['60413206', 'Experiment of Chemistry', '化学实验', '6', '1'],
               ['60413221', 'Physics Experiments II', '物理实验 I（2）', '6', '3'],
               ['', '', '形势与政策（3）', '6', '1'],
               ['', '', '工程师遴选考试', '7', '1'],
               ['EM11', 'Functional analysis', '泛函分析', '7', '6'],
               ['EM12', 'Optimisation', '最优化', '7', '6'],
               ['EM13', 'Probabilities and statistics', '概率论与数理统计', '7', '6'],
               ['EE11', 'Electrical engineering', '电气工程', '7', '7'],
               ['EE12', 'Deterministic signal processing', '确定性信号处理', '7', '7'],
               ['AS11', 'Linear statics (flexible solids and beams)', '线性静力学', '7', '8'],
               ['AM11', 'Structural metallic materials', '金属结构材料', '7', '9'],
               ['FM11', 'Basic fluid mechanics and aerodynamics', '基础流体力学和空气动力学', '7', '10'],
               ['HT11', 'Engineering Thermodynamics', '工程热力学', '7', '11'],
               ['ES11', 'Introduction to options', '学科导论', '7', '12'],
               ['ES12', 'Project Management 1', '项目管理1', '7', '12'],
               ['HS11', 'Economics', '经济学', '7', '13'],
               ['EF11', 'French Language', '法语', '7', '14'],
               ['EF12', 'Engineering English 1', '工程英语1', '7', '14'],
               ['', 'Professional Experiment', '综合实验（学术小假期）', '7', '15'],
               ['EE21', 'Random Signal Processing', '随机信号处理', '8', '7'],
               ['AS21', 'Linear theory of beams', '梁的线性理论', '8', '8'],
               ['AS22', 'Finite element methods', '有限元方法', '8', '8'],
               ['HT21', 'Heat Transfer', '传热学', '8', '11'],
               ['CS21', 'Database Design ', '数据库设计', '8', '16'],
               ['ES21', 'System Modeling & Simulation', '建模与仿真', '8', '12'],
               ['ES22', 'Flight mechanics', '飞行力学', '8', '12'],
               ['ES23', 'Aircraft System', '飞机系统', '8', '12'],
               ['ES24', 'Multidisciplinary Project Bachelor thesis', '多学科项目（本科毕业设计）', '8', '12'],
               ['EF21', 'French language, cultural conferences and workshops', '外国语言文化与艺术', '8', '14'],
               ['EF22', 'Engineering English 2', '工程英语2', '8', '14'],
               ['', 'Worker Internship', '蓝领实习（金工实习）', '8', '15'],
               ['', 'Week of science, technology and academics', '科技学术周', '8', '15'],
               ['', 'Situation and Policy 3', '形式与政策（3）', '8', '15'],
               ['EM31', 'Numerical Analysis of PDE', '偏微分方程数值分析', '9', '6'],
               ['EE31', 'Digital Electronics', '数字电路', '9', '7'],
               ['EE32', 'Representation and Analysis of dynamical systems ', '动态系统建模与分析', '9', '7'],
               ['EE33', 'Control design and servo-loop systems', '控制设计与伺服回路系统', '9', '7'],
               ['AS31', 'Discrete structure dynamics', '离散结构动力学', '9', '8'],
               ['AM31', 'Composite and special materials', '复合材料与特种材料', '9', '9'],
               ['FM31', 'Advanced fluid mechanics', '高级流体力学', '9', '10'],
               ['HT31', 'Convective transfers', '对流换热', '9', '11'],
               ['AT31', 'Air Traffic Management', '空中交通管理', '9', '18'],
               ['ES31', 'Flying qualities', '飞行品质', '9', '12'],
               ['ES32', 'Airplane conceptual design', '飞机概念设计', '9', '12'],
               ['ES33', 'Production and maintenance techniques', '航空生产及维修技术', '9', '12'],
               ['HS31', 'Introduction to air law', '航空法导论', '9', '13'],
               ['EF31', 'Basic Aviation English', '初级民航英语', '9', '14'],
               ['AS41', 'Theory of Plates and Shells', '板壳理论', '10', '8'],
               ['AS42', 'Fatigue of structure', '结构疲劳', '10', '8'],
               ['AM41', 'Properties of Metallic materials', '金属材料性能', '10', '9'],
               ['AM42', 'Properties of Composite Materials', '复合材料性能', '10', '9'],
               ['CS41', 'Validation and verification', '确认与验证', '10', '16'],
               ['ES41', 'Sustainable development & enviroment', '可持续发展与环境', '10', '12'],
               ['ES42', 'Airworthiness', '适航', '10', '12'],
               ['ES43', 'Project Management 2', '项目管理2', '10', '12'],
               ['HS41', 'Air transport economics', '航空运输经济', '10', '13'],
               ['EF41', 'Advanced Aviation English', '高级民航英语', '10', '14'],
               ['', 'Technician Internship', '技术实习', '10', '15'],
               ['FM41', 'Compressible aerodynamics', '可压缩空气动力学', '10', '10'],
               ['HT41', 'Fundamentals of combustion & Heterogeneous combustion', '燃烧理论基础与多相燃烧', '10', '11'],
               ['HT42', 'Basics of heat transfer in turbomachinery', '涡轮机械换热基础', '10', '11'],
               ['PS41', 'Propulsion', '推进系统', '10', '17'],
               ['EE41', 'Filtering and navigation', '滤波与导航', '10', '7'],
               ['EE42', 'Automatic piloting and flight control', '自动驾驶与飞行控制', '10', '7'],
               ['EE43', 'Sensors', '传感器', '10', '7'],
               ['EE44', 'Networks', '计算机网络', '10', '7'],
               ['EE45', 'Communication Principle', '通信原理', '10', '7'],
               ['AS51', 'Advanced Dynamics of Structures', '高级结构动力学', '11', '8'],
               ['AS52', 'Applications Structurales des Element Finis', '有限元应用', '11', '8'],
               ['AS53', 'Aircraft and Spacecraft  Loads & Structure', '航空航天器载荷与结构分析', '11', '8'],
               ['FM51', 'Turbulence : Physical basis and modelling ', '湍流', '11', '10'],
               ['FM52', 'Aerodynamics of turbomachinery', '涡轮机械空气动力学', '11', '10'],
               ['HT51', 'Turbulent combustion and modelling', '湍流燃烧与模拟', '11', '11'],
               ['HT52', 'Combustion chamber modelling', '燃烧室模拟', '11', '11'],
               ['HT53', 'Thermal radtion in participating media', '参与介质热辐射', '11', '11'],
               ['PS51', 'Advanced thermodynamics of propulsive airbreathing systems ，Elements of rocket propulsion',
                '燃气轮机高等热力学和火箭推进系统', '11', '17'],
               ['PS52', 'Aerothermochemistry and Explosions', '气动热化学及爆炸', '11', '17'],
               ['AG51', 'Navigation Systems', '导航系统', '11', '19'],
               ['AG52', 'Flight Management and Guidance Systems', '飞行管理与引导系统', '11', '19'],
               ['AG53', 'Avionics Technology', '航空电子技术', '11', '19'],
               ['AG54', 'Avionics Systems Regulations', '航空电子系统规章', '11', '19'],
               ['AG55', 'Hydraulic and Electrical Actuators', '液压与电动装置', '11', '19'],
               ['AG56', 'Aeronautical Communication Systems', '航空通信系统', '11', '19'],
               ['AG57', 'Aircraft Operations', '航空器运行', '11', '19'],
               ['AG58', 'Surveillance Systems', '监视系统', '11', '19'],
               ['AG59', 'Air-Ground Collaborative Applications', '地空协作应用', '11', '19'],
               ['ES51', 'Multi-Disciplinary Project', '多学科项目（研究生开题）', '11', '12'],
               ['ES52', 'Aeronautical Engineering sciences', '航空工程科学', '11', '12'],
               ['HS51', 'Corporate management', '企业管理', '11', '13'],
               ['HS52', 'Business game and team organization', '商务运作与团队组织', '11', '13'],
               ['HS53', 'Natural Dialectic', '自然辩证法', '11', '13'],
               ['HS54/S9901001', 'Politics', '中国特色社会主义理论与实践', '11', '13']]


def prepare_teacher():
    for t in tqdm(teacher_list):
        Teacher.objects.get_or_create(name=t[1].strip())


def prepare_classroom():
    for c in tqdm(classroom_ls):
        Classroom.objects.get_or_create(name=c[1].strip())


def prepare_group():
    for g in tqdm(class_descriptions):
        Group.objects.get_or_create(semester=int(str(g[2]).strip()), name=str(g[4]).strip(), period=30)
        Group.objects.get_or_create(semester=int(str(g[2]).strip()), name=str(g[4]).strip(), period=29)


def prepare_type():
    for ct in tqdm(lesson_type):
        CourseType.objects.get_or_create(name=ct[1], defaults=dict(color=ct[2].strip().strip("#")))


def prepare_lesson_info():
    for li in tqdm(lesson_list):
        semester = int(li[3])
        if semester % 2 == 0:
            CourseInfo.objects.get_or_create(ch_name=li[2], defaults=dict(period=30, code=li[0], en_name=li[1], type_id=li[4], semester=semester))
        else:
            CourseInfo.objects.get_or_create(ch_name=li[2], defaults=dict(period=29, code=li[0], en_name=li[1], type_id=li[4], semester=semester))


def prepare_semester_config():
    SemesterConfig.objects.get_or_create(config_id=1, defaults=dict(current_period=30, week1_monday_date=datetime(2022, 2, 28)))


if __name__ == '__main__':
    prepare_teacher()
    prepare_classroom()
    prepare_group()
    prepare_type()
    prepare_lesson_info()
    prepare_semester_config()

    # for course in Course.objects.all():
    #     course.save()

    # for log in tqdm(CourseChangeLog.objects.all()):
    #     log.save()
