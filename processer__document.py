# -*- coding: utf-8 -*-

import random
import datetime
import time
# 住院
dataCount = 10000000    #10M.
codeRange = range(ord('a'), ord('z'))
alphaRange = [chr(x) for x in codeRange]
alphaMax = len(alphaRange)
daysMax = 370
theDay = datetime.date(2017, 1, 1)
hospital_dict = [['01', '顶级医院'],
                 ['0101', '二级医院A'],
                 ['010101', '高青县中医院'],
                 ['010102', '高青县慈善医院'],
                 ['0102', '二级医院B'],
                 ['010201', '高青丽康医院'],
                 ['010202', '淄博市中心医院(高青院区)'],
                 ['0103', '二级医院C'],
                 ['010301', '高青县妇幼保健院'],
                 ['010302', '高青县花沟中心卫生院'],
                 ['010303', '高青县中医医院开发区卫生所'],
                 ['010304', '高青县城区办事处青苑社区卫生服务站'],
                 ['0104', '二级医院D'],
                 ['010401', '董家骨科'],
                 ['010402', '高苑社区卫生服务站'],
                 ['010403', '滨州沪滨爱尔眼科医院'],
                 ['010404', '淄博市高青县残疾人康复医院'],
                 ['0105', '二级医院E'],
                 ['010501', '高青东方老年医院'],
                 ['010502', '中医药针灸疑难病专科医院'],
                 ['0106', '二级医院F'],
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
             ['18', '自制剂'],
             ['19', '其他']]

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
['A04.06.01', '心脏移植项目']]


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
    return random.randint(1, maxNum)/float(100)


def genRandomTypes(types):
    return random.choice(types)


def genDataBase1(fileName, dataCount):
    outp = open(fileName, 'w')
    i = 0
    while i < dataCount:
        account_item = genRandomTypes(item_dict)
        ACCOUNT_ITEM_CODE = account_item[0]
        ACCOUNT_ITEM_NAME = account_item[1]
        AMOUNT = genRandomNum(10000)
        dept = genRandomTypes(dept_dict)
        DEPT_CODE = dept[0]
        DEPT_NAME = dept[1]
        GROUP_ID = genRandomTypes(group_dict)[0]
        hospital = genRandomTypes(hospital_dict)
        HOSPITAL_CODE = hospital[0]
        HOSPITAL_NAME = hospital[1]
        date = genRandomDay()
        REPORT_PERIOD = date.strftime("%Y%m%d")
        DISTRICT_CODE = genRandomTypes(region_dict)[0]
        SYSTEM_TIME = date.strftime("%Y-%m-%d") + genRandomTime()

        # mLine = "%s\x01%s\x01%d\x01%s\x01%s\x01%s\x01%s\x01%s\x01%s\x01%s\x01%s\n" % (ACCOUNT_ITEM_CODE, ACCOUNT_ITEM_NAME, AMOUNT, DEPT_CODE,
        #                                              DEPT_NAME, GROUP_ID, HOSPITAL_CODE, HOSPITAL_NAME, REPORT_PERIOD,
        #                                              DISTRICT_CODE, SYSTEM_TIME)
        mLine = "%s,%s,%s,%d,%s,%s,%s,%s,%s\n" % (HOSPITAL_CODE, DEPT_CODE,
                                                        ACCOUNT_ITEM_CODE, AMOUNT, ACCOUNT_ITEM_NAME, REPORT_PERIOD,
                                                        GROUP_ID, DISTRICT_CODE, SYSTEM_TIME)
        outp.write(mLine)
        i += 1
    outp.close()


if __name__ == "__main__":
    random.seed()
    start = time.time()
    genDataBase1('.\processer_document.txt', dataCount)
    end = time.time()
    print('use time:%d' % (end-start))
    print('Ok')
