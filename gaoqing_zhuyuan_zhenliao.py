#-*- coding: utf-8 -*-

import random
import datetime
import time
# 住院
dataCount = 100000    #10M.
codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 370
theDay = datetime.date(2015, 1, 1)
hospital_dict = [['010101', '高青县中医院'],
                 ['010102', '高青县慈善医院'],
                 ['010201', '高青丽康医院'],
                 ['010202', '淄博市中心医院(高青院区)'],
                 ['010301', '高青县妇幼保健院'],
                 ['010302', '高青县花沟中心卫生院'],
                 ['010303', '高青县中医医院开发区卫生所'],
                 ['010304', '高青县城区办事处青苑社区卫生服务站'],
                 ['010401', '董家骨科'],
                 ['010402', '高苑社区卫生服务站'],
                 ['010403', '滨州沪滨爱尔眼科医院'],
                 ['010404', '淄博市高青县残疾人康复医院'],
                 ['010501', '高青东方老年医院'],
                 ['010502', '中医药针灸疑难病专科医院'],
                 ['010601', '滨州医学院附属医院协作医院'],
                 ['010602', '高青瑞佳口腔医院'],
                 ['010603', '济南明水眼科医院接送点'],
                 ['010604', '高青瑞佳口腔医院']]

region_dict = [['0101', '高青县'],
               ['0102', '淄博市'],
               ['0103', '高青县城区'],
               ['0104', '滨州'],
               ['0105', '高青东方区'],
               ['0106', '济南']]

item_dict = [['1', '西药'],
             ['2', '中成药'],
             ['3', '中草药'],
             ['4', '床位'],
             ['5', '诊察'],
             ['6', '检查'],
             ['7', '化验'],
             ['8', '治疗'],
             ['9', '手术'],
             ['10', '护理'],
             ['11', '卫生材料'],
             ['12', '一般诊疗费'],
             ['13', '药事服务费'],
             ['14', '挂号'],
             ['15', '国家基本药物'],
             ['16', '省级基本药物'],
             ['17', '抗菌药物'],
             ['18', '自制剂']]

group_dict = [['1', '普通收费'],
              ['2', '国家基本药物、省级基本药物'],
              ['3', '抗菌药物'],
              ['4', '自制剂']]


dept_dict = [
['A01', '预防保健科'],
['A02', '全科医疗科'],
['A03', '内科'],
['A03.01', '呼吸内科专业'],
['A03.02', '消化内科专业'],
['A03.03', '神经内科专业'],
['A03.04', '心血管内科专业'],
['A03.05', '血液内科专业'],
['A03.06', '肾病学专业'],
['A03.07', '内分泌专业'],
['A03.08', '免疫学专业'],
['A03.09', '变态反应专业'],
['A03.10', '老年病专业'],
['A03.99', '其他'],
['A04', '外科'],
['A04.01', '普通外科专业'],
['A04.01.01', '肝脏移植项目'],
['A04.01.02', '胰腺移植项目'],
['A04.01.03', '小肠移植项目'],
['A04.02', '神经外科专业'],
['A04.03', '骨科专业'],
['A04.04', '泌尿外科专业'],
['A04.04.01', '肾脏移植项目'],
['A04.05', '胸外科专业'],
['A04.05.01', '肺脏移植项目'],
['A04.06', '心脏大血管外科专业'],
['A04.06.01', '心脏移植项目'],
['A04.07', '烧伤科专业'],
['A04.08', '整形外科专业'],
['A04.99', '其他'],
['A05', '妇产科'],
['A05.01', '妇科专业'],
['A05.02', '产科专业'],
['A05.03', '计划生育专业'],
['A05.04', '优生学专业'],
['A05.05', '生殖健康与不孕症专业'],
['A05.99', '其他'],
['A06', '妇女保健科'],
['A06.01', '青春期保健专业'],
['A06.02', '围产期保健专业'],
['A06.03', '更年期保健专业'],
['A06.04', '妇女心理卫生专业'],
['A06.05', '妇女营养专业'],
['A06.99', '其他'],
['A07', '儿科'],
['A07.01', '新生儿专业'],
['A07.02', '小儿传染病专业'],
['A07.03', '小儿消化专业'],
['A07.04', '小儿呼吸专业'],
['A07.05', '小儿心脏病专业'],
['A07.06', '小儿肾病专业'],
['A07.07', '小儿血液病专业'],
['A07.08', '小儿神经病学专业'],
['A07.09', '小儿内分泌专业'],
['A07.10', '小儿遗传病专业'],
['A07.11', '小儿免疫专业'],
['A07.99', '其他'],
['A08', '小儿外科'],
['A08.01', '小儿普通外科专业'],
['A08.02', '小儿骨科专业'],
['A08.03', '小儿泌尿外科专业'],
['A08.04', '小儿胸心外科专业'],
['A08.05', '小儿神经外科专业'],
['A08.99', '其他'],
['A09', '儿童保健科'],
['A09.01', '儿童生长发育专业'],
['A09.02', '儿童营养专业'],
['A09.03', '儿童心理卫生专业'],
['A09.04', '儿童五官保健专业'],
['A09.05', '儿童康复专业'],
['A09.99', '其他'],
['A10', '眼科'],
['A11', '耳鼻咽喉科'],
['A11.01', '耳科专业'],
['A11.02', '鼻科专业'],
['A11.03', '咽喉科专业'],
['A11.99', '其他'],
['A12', '口腔科'],
['A12.01', '口腔内科专业'],
['A12.02', '口腔颌面外科专业'],
['A12.03', '正畸专业'],
['A12.04', '口腔修复专业'],
['A12.05', '口腔预防保健专业'],
['A12.99', '其他'],
['A13', '皮肤科'],
['A13.01', '皮肤病专业'],
['A13.02', '性传播疾病专业'],
['A13.99', '其他'],
['A14', '医疗美容科'],
['A15', '精神科'],
['A15.01', '精神病专业'],
['A15.02', '精神卫生专业'],
['A15.03', '药物依赖专业'],
['A15.04', '精神康复专业'],
['A15.05', '社区防治专业'],
['A15.06', '临床心理专业'],
['A15.07', '司法精神专业'],
['A15.99', '其他'],
['A16', '传染科'],
['A16.01', '肠道传染病专业'],
['A16.02', '呼吸道传染病专业'],
['A16.03', '肝炎专业'],
['A16.04', '虫媒传染病专业'],
['A16.05', '动物源性传染病专业'],
['A16.06', '蠕虫病专业'],
['A16.99', '其它'],
['A17', '结核病科'],
['A18', '地方病科'],
['A19', '肿瘤科'],
['A20', '急诊医学科'],
['A21', '康复医学科'],
['A22', '运动医学科'],
['A23', '职业病科'],
['A23.01', '职业中毒专业'],
['A23.02', '尘肺专业'],
['A23.03', '放射病专业'],
['A23.04', '物理因素损伤专业'],
['A23.05', '职业健康监护专业'],
['A23.99', '其他'],
['A24', '临终关怀科'],
['A25', '特种医学与军事医学科'],
['A26', '麻醉科'],
['A27', '疼痛科'],
['A28', '重症医学科'],
['A30', '医学检验科'],
['A30.01', '临床体液、血液专业'],
['A30.02', '临床微生物学专业'],
['A30.03', '临床生化检验专业'],
['A30.04', '临床免疫、血清学专业'],
['A30.05', '临床细胞分子遗传学专业'],
['A30.99', '其他'],
['A31', '病理科'],
['A32', '医学影像科'],
['A32.01', 'X线诊断专业'],
['A32.02', 'CT诊断专业'],
['A32.03', '磁共振成像诊断专业'],
['A32.04', '核医学专业'],
['A32.05', '超声诊断专业'],
['A32.06', '心电诊断专业'],
['A32.07', '脑电及脑血流图诊断专业'],
['A32.08', '神经肌肉电图专业'],
['A32.09', '介入放射学专业'],
['A32.10', '放射治疗专业'],
['A32.99', '其他'],
['A50', '中医科'],
['A50.01', '内科专业'],
['A50.02', '外科专业'],
['A50.03', '妇产科专业'],
['A50.04', '儿科专业'],
['A50.05', '皮肤科专业'],
['A50.06', '眼科专业'],
['A50.07', '耳鼻咽喉科专业'],
['A50.08', '口腔科专业'],
['A50.09', '肿瘤科专业'],
['A50.10', '骨伤科专业'],
['A50.11', '肛肠科专业'],
['A50.12', '老年病科专业'],
['A50.13', '针灸科专业'],
['A50.14', '推拿科专业'],
['A50.15', '康复医学专业'],
['A50.16', '急诊科专业'],
['A50.17', '预防保健科专业'],
['A50.99', '其他'],
['A51', '民族医学科'],
['A51.01', '维吾尔医学'],
['A51.02', '藏医学'],
['A51.03', '蒙医学'],
['A51.04', '彝医学'],
['A51.05', '傣医学'],
['A51.99', '其他'],
['A52', '中西医结合科'],
['A69', '其他业务科室'],
['B01', '传染病预防控制科(中心)'],
['B02', '性病艾滋病预防控制科(中心)'],
['B03', '结核病预防控制科(中心)'],
['B04', '血吸虫预防控制科(中心)'],
['B05', '慢性非传染性疾病预防控制科(中心)'],
['B06', '寄生虫病预防控制科(中心)'],
['B07', '地方病控制科(中心)'],
['B08', '精神卫生科(中心)'],
['B09', '妇幼保健科'],
['B10', '免疫规划科(中心)'],
['B11', '农村改水技术指导科(中心)'],
['B12', '疾病控制与应急处理办公室'],
['B13', '食品卫生科'],
['B14', '环境卫生所'],
['B15', '职业卫生科'],
['B16', '放射卫生科'],
['B17', '学校卫生科'],
['B18', '健康教育科(中心)'],
['B19', '预防医学门诊'],
['B69', '其他业务科室'],
['C01', '综合卫生监督科'],
['C02', '产品卫生监督科'],
['C03', '职业卫生监督科'],
['C04', '环境卫生监督科'],
['C05', '传染病执法监督科'],
['C06', '医疗服务监督科'],
['C07', '稽查科(大队)'],
['C08', '许可受理科'],
['C09', '放射卫生监督科'],
['C10', '学校卫生监督科'],
['C11', '食品安全监督科'],
['C69', '其他'],
['D71', '护理部'],
['D72', '药剂科(药房)'],
['D73', '感染科'],
['D74', '输血科(血库)'],
['D81', '办公室'],
['D82', '人事科'],
['D83', '财务科'],
['D84', '设备科'],
['D85', '信息科(中心)'],
['D86', '医政科'],
['D87', '教育培训科'],
['D88', '总务科'],
['D89', '新农合管理办公室'],
['D99', '其他科室']]


def genRandomString(nameLength):
    global alphaRange, alphaMax
    length = random.randint(1, nameLength)
    name = ''
    for i in range(length):
        name += alphaRange[random.randint(0, alphaMax-1)]
    return name


def genRandomDay():
    global daysMax, theDay
    mDays = random.randint(0, daysMax)
    mDate = theDay + datetime.timedelta(days=mDays)
    # return mDate.isoformat()
    return mDate


def genRandomTime():
    return str(time.strftime(" %H:%M:%S", time.localtime()))
    # hour = random.randint(0, 24)
    # minite = random.randint(0, 60)
    # second = random.randint(0,60)
    # return str(hour) + ":" + str(minite) + ":" + str(second)


def genRandomNum(maxNum):
    return random.randint(1, maxNum)


def genRandomTypes(types):
    return random.choice(types)


def genDataBase1(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        ADMISSION_NUM = genRandomNum(100)
        BED_NUM = genRandomNum(100)
        BETTER_NUM = genRandomNum(100)
        CONSULT_REG_DIAG = genRandomNum(100)
        CONSULT_TOTAL = genRandomNum(100)
        date = genRandomDay()
        CREATE_AT = date.strftime("%Y-%m-%d")
        CRITICAL_NUM = genRandomNum(100)
        DEATH_NUM = genRandomNum(100)
        DELIVERY_NORMAL_NUM = genRandomNum(100)
        dept = genRandomTypes(dept_dict)
        DEPT_CODE = dept[0]
        DEPT_NAME = dept[1]
        DIED_NUM = genRandomNum(100)
        DISCHARGE_NUM = genRandomNum(100)
        DISTRICT_CODE = genRandomTypes(region_dict)[0]
        DOCTORDAY_NUM = genRandomNum(100)
        EXCHANGE_TYPE = genRandomString(10)
        HEAL_NUM = genRandomNum(100)
        HOSPITAL_CHECK = genRandomNum(100)
        HOSPITAL_CHECK_EXCEPTION = genRandomNum(100)
        HOSPITAL_EXTRA_CARE = genRandomNum(100)
        HOSPITAL_FIRST_CARE = genRandomNum(100)
        HOSPITAL_INSPECT = genRandomNum(100)
        HOSPITAL_INSPECT_EXCEPTION = genRandomNum(100)
        HOSPITAL_NURSE_NUM = genRandomNum(100)
        HOSPITAL_SECOND_CARE = genRandomNum(100)
        HOSPITAL_THREE_CARE = genRandomNum(100)
        ID = genRandomString(20)
        IN_HOSPITAL_NUM = genRandomNum(100)
        IN_HOSPITALDAY_TOTAL = genRandomNum(100)
        MOVE_IN_NUM = genRandomNum(100)
        NOT_HEAL_NUM = genRandomNum(100)
        OPERATION = genRandomNum(100)
        hospital = genRandomTypes(hospital_dict)
        ORG_CODE = hospital[0]
        ORG_NAME = hospital[1]
        OTHER_NUM = genRandomNum(100)
        PAT_ANTIBACTERIAL_NUM = genRandomNum(100)
        PAT_BASIC_DRUG_NUM = genRandomNum(100)
        REFER_OUT_NUM = genRandomNum(100)
        REPORT_PERIOD = date.strftime("%Y%m%d")
        RESCUE_NUM = genRandomNum(100)
        RESCUE_SUCCESS_NUM = genRandomNum(100)
        SERVICE_BED = genRandomNum(100)
        SEVERE_BETTER_TOTAL = genRandomNum(100)
        SEVERE_DEATH_TOTAL = genRandomNum(100)
        SEVERE_OUT_TOTAL = genRandomNum(100)
        STD_DEPT_CODE = dept[0]
        SYSTEM_TIME = date.strftime("%Y-%m-%d") + genRandomTime()

        # mLine = "%d\x01%d\x01%d\x01%d\x01%d\x01%s\x01%d\x01%d\x01%d\x01%s\x01%s\x01%d\x01%d\x01%s\x01%d\x01%s\x01" \
        #         "%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%s\x01%d\x01%d\x01%d\x01%d\x01%d\x01" \
        #         "%s\x01%s\x01%d\x01%d\x01%d\x01%d\x01%s\x01%d\x01%d\x01%d\x01%d\x01%d\x01%d\x01%s\x01%s\n" % (
        mLine = "%s,%s,%s,%s,%s,%s,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d," \
                "%d,%d,%d,%d,%d,%s,%s,%s,%d,%d,%d,%d,%s,%d,%d,%d," \
                "%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%s\n" % (
            REPORT_PERIOD,
        ORG_CODE,
        ORG_NAME,
            STD_DEPT_CODE,
        DEPT_CODE,
        DEPT_NAME,
            ADMISSION_NUM,
        MOVE_IN_NUM,
        REFER_OUT_NUM,
        DISCHARGE_NUM,
        DIED_NUM,
        CRITICAL_NUM,
        RESCUE_NUM,
        RESCUE_SUCCESS_NUM,
        OPERATION,
        CONSULT_TOTAL,
        CONSULT_REG_DIAG,
        SEVERE_OUT_TOTAL,
        SEVERE_BETTER_TOTAL,
        SEVERE_DEATH_TOTAL,
        SERVICE_BED,
        CREATE_AT,
        EXCHANGE_TYPE,
        DISTRICT_CODE,
        IN_HOSPITAL_NUM,
        PAT_ANTIBACTERIAL_NUM,
        PAT_BASIC_DRUG_NUM,
        BED_NUM,
        ID,
        IN_HOSPITALDAY_TOTAL,
        DOCTORDAY_NUM,
        HEAL_NUM,
        BETTER_NUM,
        NOT_HEAL_NUM,
        DELIVERY_NORMAL_NUM,
        DEATH_NUM,
        OTHER_NUM,
        HOSPITAL_EXTRA_CARE,
        HOSPITAL_FIRST_CARE,
        HOSPITAL_SECOND_CARE,
        HOSPITAL_THREE_CARE,
        HOSPITAL_CHECK,
        HOSPITAL_CHECK_EXCEPTION,
        HOSPITAL_INSPECT,
        HOSPITAL_INSPECT_EXCEPTION,
        HOSPITAL_NURSE_NUM,
        SYSTEM_TIME)
        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase1('.\zhuyuan_zhenliao_new.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end-start))
    print('Ok')
