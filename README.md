# Auto nuaa.portal
"Auto nuaa.portal" is a project for automatically login to "nuaa.portal" (南京航空航天大学校园无线网) without input username and password manually.

## iOS "Shortcuts"
The Shortcuts for iOS can be downloaded from [here](https://www.icloud.com/shortcuts/a034bd37f093425d962a6baff717d1d0).

## Android "Tasker"

## macOS "Alfred"
The Alfred workflow for macOS can be deployed by following steps.

### Getting Started
0. Install Python with "Requests" library.
    - Install [Miniconda Python](https://docs.conda.io/en/latest/miniconda.html#macosx-installers).
    - Install [Requests](https://requests.readthedocs.io/en/master/).
1. Install [Alfred 4](https://www.alfredapp.com/) (this workflow may also compatible with Alfred 3 and Alfred 2, not tested) with a [Powerpack](https://www.alfredapp.com/shop/) licence.
2. Download workflow source file from [release page](https://github.com/phguo/Auto-nuaa.portal/releases) and double-click.
3. Set the "Workflow Environment Variables" in which
    - __UNAME__ is your ID for login to nuaa.portal, like `BX9999999`.
    - __PASSWORD__ is your password, like `123456`.
    - __PYTHON_ENV__ is a python environment with "Requests" library installed, it would be like `/Users/{your mac user name}/miniconda3/bin/python` if you follow step 0 to install Python and "Requests".
4. Click on "import" to import "Auto nuaa.portal" into your Alfred workflows.
5. Disable the "Captive Network Support" in macOS using 
```
sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.captive.control Active -boolean false
```
This step is required due to terminal can not access to the network when there is a captive network popup for inputting username and password, see [this discussion](https://apple.stackexchange.com/questions/45418/how-to-automatically-login-to-captive-portals-on-os-x) for detail. In case you want to remove this setting use
```
sudo defaults delete /Library/Preferences/SystemConfiguration/com.apple.captive.control Active
```


### Usage
- Connect to "nuaa.portal".
- Using with Alfred keyword "nuaa login" to login to "nuaa.portal".
- Using with Alfred keyword "nuaa logout" to log out.


### Changelog
For the versions available, see [releases on this repository](https://github.com/phguo/Auto-nuaa.portal/releases).

- [__v1.0__](https://github.com/phguo/Auto-nuaa.portal/releases/tag/v1.0) - May 21, 2020
    - *Update:* This workflow will not work till the WebView popup for captive portal is closed, fixed this by disable the "Captive Network Support" in macOS.
    - *Add:* Added an optional `config.py` file to store username and password.
    - *Update:* Modified the request URL.

- [__v0.9__](https://github.com/phguo/Auto-nuaa.portal/releases/tag/v0.9) - May 8, 2020
    - *Add:* Using keyword "nuaa login" to login to "nuaa.portal".
    - *Add:* Using keyword "nuaa logout" to log out.


### TODO
- [ ] Get SSID of current WiFi connection.


## License
This project is licensed under the MIT License, see the [LICENSE](https://github.com/phguo/Auto-nuaa.portal/blob/master/LICENSE) file for details.


## Acknowledgments
This project referred to 

1. [nuaa_portal_login_cli](https://github.com/RyanSu98/nuaa_portal_login_cli)
2. [需要captive portal方式认证WiFi的自动登录方法](https://zhuanlan.zhihu.com/p/21412687)
3. [How to automatically login to captive portals on OS X?](https://apple.stackexchange.com/questions/45418/how-to-automatically-login-to-captive-portals-on-os-x)
4. [nuistconnect](https://github.com/RRRRRm/nuistconnect/)
