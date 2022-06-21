# 기본데이터 : https://github.com/icepeng/maple-calc/blob/master/src/app/grinding/models/map.ts
# 계산데이터 : https://github.com/icepeng/maple-calc/blob/e633b80e62fcb67c0d40baf70792e85bac1600f6/src/app/grinding/containers/grinding.component.ts
# 추가 로직 : https://github.com/icepeng/maple-calc/blob/e633b80e62fcb67c0d40baf70792e85bac1600f6/src/app/grinding/services/grinding.service.ts

"""
메인 로직 : 타입스크립트

ngOnInit(): void {
    const mapViews = maps.map(mapData => {
      const countPerHour = (mapData.count * 60 * 60) / 7.5; 
      const expPerHour =
        (countPerHour * mapData.mobs.reduce((acc, mob) => acc + mob.exp, 0)) /
        mapData.mobs.length;
      const mesoPerHour =
        ((countPerHour *
          mapData.mobs.reduce((acc, mob) => acc + mob.level, 0)) /  # mobs 전체 값 더하기
          mapData.mobs.length) *
        7.5;
      const backgroundColor = backgroundColors[mapData.group];

      return {
        ...mapData,
        countPerHour,
        expPerHour,
        mesoPerHour,
        backgroundColor,
        burning: 0,
      };
    });
"""
"""
옵션 로직
기본 100 두배 100 추경 50 경축 10 혈반 10 쓸심 35 메르 15 유뇬 20 하이퍼 10 정펜 30 룬 100 룬의경험 50 쑥쑥새싹 10 PC 30 로디드 30
"""

def buff(option) :
 # optionslist = {'Coupon':'없음', 'MVP':0, 'Potion':0, 'ExGold':0, 'Merlink':'없음', 'HolyS' :0, 'Ring':0,'Zero':'없음','Union':0,'Hyper':0,'Pendant':'없음','Dice':0,'PC':0,'Bud':0}
  sum = 1
  if option['Coupon'] == '3배' :
    sum = sum + 2
  elif option['Coupon'] == '2배' :
    sum = sum + 1
  elif option['Coupon'] == '1.5배' :
    sum = sum + 0.5
  else :
    pass

  if option['MVP'] == 1 :
    sum = sum + 0.5

  if option['Potion'] == 1 :
    sum = sum + 0.1
    
  if option['ExGold'] == 1 :
    sum = sum + 0.1

  if option['Merlink'] == '2레벨' :
    sum = sum + 0.15
  elif option['Merlink'] == '1레벨' :
    sum = sum + 0.1
  else :
    pass

  sum = sum + (0.01 * int(option['HolyS']))

  if option['Ring'] == 1 :
    sum = sum + 0.1
  
  if option['Zero'] == 'SSS' :
    sum = sum + 0.12
  elif option['Zero'] == 'SS' :
    sum = sum + 0.1
  elif option['Zero'] == 'S' :
    sum = sum + 0.08
  elif option['Zero'] == 'A' :
    sum = sum + 0.06
  elif option['Zero'] == 'B' :
    sum = sum + 0.04
  else :
    pass
  
  sum = sum + (0.01 * int(option['Union']))
  sum = sum + (0.01 * int(option['Hyper']))

  if option['Pendant'] == '30%' :
    sum = sum + 0.3
  elif option['Pendant'] == '20%' :
    sum = sum + 0.2
  elif option['Pendant'] == '10%' :
    sum = sum + 0.1
  else :
    pass
  
  if option['Dice'] == 1 :
    sum = sum + 0.3
  
  if option['PC'] == 1:
    sum = sum + 0.3
  
  if option['Bud'] == 1 :
    sum = sum + 0.1

  sum = sum + (0.01 * int(option['etc']))
  #print(sum)
  return sum

def mob_bojeong(origexp, plylev, moblev) :
  origexp_int = int(origexp)
  if plylev >= 284 :
    plylev = 284
  diff = int(plylev) - int(moblev)
  if diff >= 40 :
    return origexp_int * 0.7
  elif diff >= 21 :
    return origexp_int * (0.9 - (diff - 20) / 100)
  elif diff >= 19 :
    return origexp_int * 0.95
  elif diff >= 17 :
    return origexp_int * 0.96
  elif diff >= 15 :
    return origexp_int * 0.97
  elif diff >= 13 :
    return origexp_int * 0.98
  elif diff >= 11 :
    return origexp_int * 0.99
  elif diff >= 10 :
    return origexp_int
  elif diff >= 5 :
    return origexp_int * 1.05
  elif diff >= 2 :
    return origexp_int * 1.1
  elif diff >= -1 :
    return origexp_int * 1.2
  elif diff >= -4 :
    return origexp_int * 1.1
  elif diff >= -9 :
    return origexp_int * 1.05
  elif diff >= -20 :
    return origexp_int * (1+(diff+10)/100)
  elif diff >= -35 :
    return origexp_int * (0.7 + ((diff+21)/100) * 4)
  elif diff >= -39 :
    return origexp_int * 0.1
  else :
    return 0

def calculate(level, data, option) :
  mapgroup = ['리버스시티','츄츄아일랜드','얌얌아일랜드','레헬른','아르카나','모라스','에스페라','셀라스','문브릿지','고통의미궁','리멘','세르니움','불타는세르니','아르크스'] #,'오디움']
  i = (level-200) // 5
  appgroup = ['소멸의여로'] + mapgroup[0:i]
  usedata = list()
  tpdata = list()
  for i in range (1, len(data), 1) :
    if data[i][0] in appgroup :
      usedata.append(data[i])
  for i in range(0, len(usedata), 1) :
    HourCount = (int(usedata[i][2]) * 60 * 60) / 7.5
    if usedata[i][5] == '' :
      HourExp = HourCount * mob_bojeong(usedata[i][3], level, usedata[i][4]) * buff(option)
    else :
      HourExp = HourCount * ((mob_bojeong(usedata[i][3], level, usedata[i][4]) + mob_bojeong(usedata[i][5], level, usedata[i][6])) / 2) * buff(option)
    tpdata.append(['200','300',usedata[i][0], usedata[i][1], str(round(float(HourExp))),'0'])
  tpdata.sort(key=lambda x: int(x[4]))
  tpdata.reverse()
  return tpdata

if __name__ == '__main__' :
  import csv
  tmpfile = open('./assets/data/200to300.csv', encoding='utf-8')
  DataList = csv.reader(tmpfile, delimiter=",", doublequote=False, lineterminator="\r\n", quotechar="'", skipinitialspace=True)
  Data2 = list(DataList)
  tmpfile.close()
  level = int(input())
  optionslist = {'Coupon':'없음', 'MVP':0, 'Potion':0, 'ExGold':0, 'Merlink':'없음', 'HolyS' :0, 'Ring':0,'Zero':'없음','Union':0,'Hyper':0,'Pendant':'없음','Dice':0,'PC':0,'Bud':0}
  print(calculate(level, Data2, optionslist))