import requests
import json


lua_script = '''
function main(splash)
  splash:go("http://example.com")              --打开页面
  splash:wait(0.5)                             --等待加载
  local title = splash:evaljs("document.title") --执行js代码获取结果
  return {title=title}                         --返回json 形式的结果
end
'''
splash_url = 'http://localhost:8050/execute'
headers = {'content-type': 'application/json'}
data = json.dumps({'lua_source': lua_script})
response = requests.post(splash_url, headers=headers, data=data)
print(response.content)



