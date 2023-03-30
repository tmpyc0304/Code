import csv
from itertools import groupby

s_to_i1 = {  # subject_to_int1
    "國": 0,
    "英": 1,
    "數A": 2,
    "數B": 3,
    "自": 4,
    "社": 5,
    "數甲": 6,
    "歷": 7,
    "地": 8,
    "公": 9,
    "物": 10,
    "化": 11,
    "生": 12,
}
s_to_i2 = {  # subject_to_int2
    "國文": 0,
    "英文": 1,
    "數學A": 2,
    "數學B": 3,
    "自然": 4,
    "社會": 5,
    "數學甲": 6,
    "歷史": 7,
    "地理": 8,
    "公民": 9,
    "物理": 10,
    "化學": 11,
    "生物": 12,
}

dic = []  # {系組代碼, 校名, 系組名, 採計及加權, 錄取人數, 普通生錄取分數, 普通生同分參酌, 原住民錄取分數}


def create_dic():
    csvfile = open("2021 Admission Scores.csv")

    for i in csv.reader(csvfile):
        dic.append(
            {
                "系組代碼": i[0],
                "校名": i[1],
                "系組名": i[2],
                "採計及加權": i[3],
                "錄取人數": i[4],
                "錄取分數": i[5],
                "同分參酌": i[6],
            }
        )


def calculate_weight(score, select):
    admit = []
    for key, value in groupby(dic, lambda d: d["校名"]):
        if key in select:
            for i in list(value):
                weight = [0 for j in range(13)]

                major = False
                for j in i["採計及加權"].split():
                    tmp = j.split("x")

                    if tmp[0] == "術科":
                        major = True

                        break

                    weight[s_to_i1[tmp[0]]] = float(tmp[1])

                if int(i["錄取人數"]) != 0 and major is False:
                    i["加權分數"] = sum([a * b for a, b in zip(score, weight)])
                    i["滿分率"] = float(i["錄取分數"]) / sum([60 * a for a in weight]) * 100

                    if i["加權分數"] > float(i["錄取分數"]):
                        admit.append(i)
                    elif i["加權分數"] == float(i["錄取分數"]):
                        same_score = i["同分參酌"].split()

                        conform = True
                        for j in range(0, len(same_score), 2):
                            if score[s_to_i2[same_score[j]]] < int(same_score[j + 1]):
                                conform = False

                                break

                        if conform is True:
                            admit.append(i)

    return admit


subject_list = [
    "",
    "國文",
    "英文",
    "數Ａ",
    "數Ｂ",
    "自然",
    "社會",
    "數甲",
    "歷史",
    "地理",
    "公民",
    "物理",
    "化學",
    "生物",
]
college_list = [
    "",
    "國立臺灣大學",
    "國立臺灣師範大學",
    "國立中興大學",
    "國立成功大學",
    "國立政治大學",
    "國立清華大學",
    "國立陽明交通大學",
    "國立中央大學",
    "國立臺灣海洋大學",
    "國立高雄師範大學",
    "國立彰化師範大學",
    "國立中山大學",
    "國立臺中教育大學",
    "國立臺北教育大學",
    "國立臺南大學",
    "國立東華大學",
    "臺北市立大學",
    "國立屏東大學",
    "國立臺東大學",
    "國立體育大學",
    "國立中正大學",
    "國立臺灣藝術大學",
    "國立暨南國際大學",
    "國立臺灣體育運動大學",
    "國立臺南藝術大學",
    "國立臺北大學",
    "國立嘉義大學",
    "國立高雄大學",
    "國立宜蘭大學",
    "國立聯合大學",
    "國立金門大學",
    "東吳大學",
    "高雄醫學大學",
    "中原大學",
    "東海大學",
    "中國醫藥大學",
    "淡江大學",
    "逢甲大學",
    "中國文化大學",
    "靜宜大學",
    "大同大學",
    "輔仁大學",
    "中山醫學大學",
    "長庚大學",
    "元智大學",
    "大葉大學",
    "中華大學",
    "義守大學",
    "銘傳大學",
    "世新大學",
    "實踐大學",
    "長榮大學",
    "南華大學",
    "玄奘大學",
    "真理大學",
    "慈濟大學",
    "臺北醫學大學",
    "康寧大學",
    "佛光大學",
    "明道大學",
    "亞洲大學",
    "馬偕醫學院",
]
