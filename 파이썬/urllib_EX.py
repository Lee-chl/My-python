import re
import urllib.request

url="https://bit.ly/3rxQFS4"
html = urllib.request.urlopen(url)
html_contents = str(html.read()) 
id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)" ,html_contents) #findall 전체 찾기 패턴대로 데이터 찾기

for result in id_results:
    print(result) #결과 출력
    