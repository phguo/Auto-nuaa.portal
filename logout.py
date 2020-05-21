import sys
import requests
import json
from login import get_ip


def logout():
    parameters = {
        "c": "Portal",
        "a": "logout",
        "callback": "dr1006",
        "login_method": "1",
        "user_account": "drcom",
        "user_password": "123",
        "ac_logout": "1",
        "register_mode": "1",
        "wlan_user_ip": get_ip(),
        "wlan_user_ipv6": "",
        "wlan_vlan_id": "",
        "wlan_user_mac": "",
        "wlan_ac_ip": "",
        "wlan_ac_name": "",
        "jsVersion": "3.3.2",
        "v": "8914"
    }
    logout_url = "http://211.65.106.6:801/eportal/"

    logout_request = requests.get(logout_url, params=parameters)
    logout_text_content = logout_request.text
    try:
        logout_text_content = logout_text_content.replace("dr1006(", '').replace(')', '')
    except:
        pass

    logout_json_content = json.loads(logout_text_content)
    result = logout_json_content.get("result")
    msg = logout_json_content.get("msg")

    if result:
        result = int(result)

    if result == 1 and msg == "\u6ce8\u9500\u6210\u529f":  # 注销成功
        query = "Logged out successfully!"
    elif result == 0 and msg == "\u6ce8\u9500\u5931\u8d25":  # 注销失败
        query = "Log out failed (Not logged in yet)."
    else:
        query = "Unknown error."

    return query


if __name__ == "__main__":
    try:
        query = logout()
    except:
        query = "Unknown Error for Log out!"
    sys.stdout.write(query)
