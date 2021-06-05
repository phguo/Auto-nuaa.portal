import sys
import requests
import json
import random
import socket

import requests


def get_ip(login_ip='211.65.106.6'):
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # try:
    #     s.connect(("202.119.64.123", 1))
    #     ip = s.getsockname()[0]
    # except:
    #     ip = "127.0.0.1"
    # finally:
    #     s.close()

    # if ip == "127.0.0.1":
    
    ip_parameters = {
        "callback": "dr1002",
        "v": str(random.randint(1000, 9999))
    }
    ip_url = "http://{}/drcom/chkstatus".format(login_ip)
    ip_request = requests.get(ip_url, params=ip_parameters)
    ip_text_content = ip_request.text.replace('dr1002(', '').replace(')', '')
    ip_json_content = json.loads(ip_text_content)
    ip = ip_json_content["v46ip"]

    return ip


def login(username, password, login_ip='211.65.106.6'):
    ip = get_ip()

    login_parameters = {
        "c": "Portal",
        "a": "login",
        "callback": "dr1003",
        "login_method": "1",
        "user_account": ",0," + username,
        "user_password": str(password),
        "wlan_user_ip": ip,
        "wlan_user_ipv6": "",
        "wlan_user_mac": "000000000000",
        "wlan_ac_ip": "",
        # "wlan_ac_name": "JiangNing_ME60",
        "wlan_ac_name": "nuaa_jjl_me60_2",
        # "wlan_ac_name": "nuaa_jjl_me60",
        "jsVersion": "3.3.2",
        # "v": "5780",
        "v": "1724"
    }

    login_url = "http://{}:801/eportal/".format(login_ip)
    login_request = requests.get(login_url, params=login_parameters, verify=False)
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

    return query


if __name__ == '__main__':
    try:
        from config import U, P, LOGIN_IP
        query = login(U, P, LOGIN_IP)
    except:
        try:
            query = login(sys.argv[1], sys.argv[2], sys.argv[3])
        except:
            try:
                query = login(sys.argv[1], sys.argv[2])
            except:
                query = "Unknown Error for Login!"
    finally:
        sys.stdout.write(query)
