# https://reqbin.com/req/python/yemanjjt/make-soap-request
# https://www.inven.co.kr/board/maple/2304/16942
# 108285093

import requests
from requests.structures import CaseInsensitiveDict
import xmltodict, json
def GetCharInfo(id):
  url = "http://api.maplestory.nexon.com/soap/maplestory.asmx?wsdl"

  headers = CaseInsensitiveDict()
  headers["Content-Type"] = "application/soap+xml"

  data = """
  <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
      <GetCharacterInfoByAccountID xmlns="https://api.maplestory.nexon.com/soap/">
        <AccountID>%d</AccountID>
      </GetCharacterInfoByAccountID>
    </soap12:Body>
  </soap12:Envelope>
  """% id


  resp = requests.post(url, headers=headers, data=data)
  obj = xmltodict.parse(resp.content)

  UserInfo = json.loads(json.dumps(obj["soap:Envelope"]["soap:Body"]["GetCharacterInfoByAccountIDResponse"]["GetCharacterInfoByAccountIDResult"]["diffgr:diffgram"]["NewDataSet"]["UserInfo"]))


  """
  print("="*50)
  print("(대표)캐릭터 월드 : %s"%UserInfo['WorldName'])
  print("(대표)캐릭터 이름 : %s"%UserInfo['CharacterName'])
  print("(대표)캐릭터 레벨 : %s"%UserInfo['Lev'])
  print("(대표)캐릭터 Exp : %s"%UserInfo['Exp'])
  print("="*50)
  """
  return UserInfo

if __name__ == '__main__' :
  print(GetCharInfo(int(input())))