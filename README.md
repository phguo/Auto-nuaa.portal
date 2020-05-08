# Alfred Workflow "Auto nuaa.portal"
"Auto nuaa.portal" is a Alfred workflow to automatically login to nuaa.portal on MacOS.


# Getting Started
0. Install Python with "Requests" library.
    - Install [Miniconda Python](https://docs.conda.io/en/latest/miniconda.html#macosx-installers).
    - Install [Requests](https://requests.readthedocs.io/en/master/).
1. Install [Alfred 4](https://www.alfredapp.com/) (this workflow may also compatible with Alfred 3 and Alfred 2, not tested) with a [Powerpack](https://www.alfredapp.com/shop/) licence.
2. Download workflow source file from [release page](https://github.com/phguo/Auto-nuaa.portal/releases) and double-click.
3. Set the "Workflow Environment Variables" in which
    - __PASSWORD__ is your password, like `BX1909999`.
    - __PYTHON_ENV__ is a python environment with "Requests" library installed, it would be like `/Users/{your mac user name}/miniconda3/bin/python` if you follow step 0 to install Python and "Requests".
    - __UNAME__ is your ID for login to nuaa.portal, like `123456`.
4. Click on "import" to import "Auto nuaa.portal" into your Alfred workflows.


# Usage
- Connect to "nuaa.portal".
- Using with Alfred keyword "nuaa login" to login to "nuaa.portal".
- Using with Alfred keyword "nuaa logout" to log out.


# Changelog
For the versions available, see [releases on this repository](https://github.com/phguo/Auto-nuaa.portal/releases).

- [__v0.9__](https://github.com/phguo/Auto-nuaa.portal/releases/tag/v0.9) - May 8, 2020
    - *Added:* Using keyword "nuaa login" to login to "nuaa.portal".
    - *Added:* Using keyword "nuaa logout" to log out.


# TODO
- ❎Get SSID of current WiFi connection.


# License
This project is licensed under the MIT License, see the [LICENSE](https://github.com/phguo/Auto-nuaa.portal/blob/master/LICENSE) file for details.


# Acknowledgments
This project referred to [nuaa_portal_login_cli](https://github.com/RyanSu98/nuaa_portal_login_cli).
