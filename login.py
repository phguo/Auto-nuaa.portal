import sys
import requests
import json
import random

username = sys.argv[1]
password = sys.argv[2]

ip_url = "http://211.65.106.6/drcom/chkstatus?callback=dr1002&v={}".format(random.randint(1000, 9999))

ip_request = requests.get(ip_url)
ip_text_content = ip_request.text.replace('dr1002(', '').replace(')', '')
ip_json_content = json.loads(ip_text_content)
ip = ip_json_content["v46ip"]

login_url = "http://211.65.106.6:801/eportal/?c=Portal&a=login&callback=dr1003&login_method=1&user_account=%2C0%2C{}&user_password={}&wlan_user_ip={}&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=JiangNing_ME60&jsVersion=3.3.2&v=1060".format(username, password, ip)

login_request = requests.get(login_url)
login_text_content = login_request.text
try:
    login_text_content = login_text_content.replace("dr1003(", '').replace(')', '')
except:
    pass

login_json_content = json.loads(login_text_content)
result = login_json_content.get("result")
ret_code = login_json_content.get("ret_code")
msg = login_json_content.get("msg")

if result:
    result = int(result)
if ret_code:
    ret_code = int(ret_code)

if result == 1 and msg == "\u8ba4\u8bc1\u6210\u529f":  # 认证成功
    query = "✅ \"{}\" Logged in successfully!".format(username)
elif result == 0 and msg == "" and ret_code == 2:
    query = "😑 \"{}\" has already logged in.".format(username)
elif result == 0 and ret_code == 1:
    query = "🚫 Wrong password for \"{}\".".format(username)
else:
    query = "❓ Unknown error for \"{}\".".format(username)

sys.stdout.write(query)
