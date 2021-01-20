# force-backup-automator

## What is it?

Do you use the Salesforce Weekly Data Export functionality to take your weekly backups?
force-backup-automator is a library to automate the download of backups via the Salesforce Weekly Export Service. This library uses Selenium to login into the Salesforce org and supports lightning or classic modes to download your back ups to your preferred location.

## Main Features
Here are a few great things of this package:
- Uses selenium to login and render the Weekly Export Service page
- Since it uses selenium to render the page, it supports both Salesforce Lightning or Classic Experience.
- Can run in headless mode for minimum overhead
- Uses the Chrome Driver for maximum compatibility
- Supports other login methods if you prefer to pass your login cookies to the package.

## Where to get it

The source code is hosted on Github at: https://github.com/stefanzepeda/force-backup-automator

Binary installers for the latest release version are available at the [Python
Package Index (PyPI)](https://pypi.org/project/force-backup-automator)

```bash
pip install force-backup-automator
```

## Dependencies
- [Selenium - Allows for login capabilities and support for lightning and classic experience](https://www.selenium.dev/projects/)
- [BeautifulSoup - Provides a robust framework to isolate the links from the page](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests - Allows for faster low overhead download of the files](https://requests.readthedocs.io/en/master/)

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Documentation

Import the BackupController class as the main helper to download files.

```python
from force-backup-automator import BackupController
```

Create an instance of the class and provide the Chrome Web Driver location, the link to your org and if you prefer headless mode:

```python
backup_instance = BackupController(driver_location='./chromedriver',org_link='ORG MAIN URL',is_headless=0)

```

### Constructor Parameters
- driver_location: The path to the Chrome Web Driver, make sure you download the proper version for your Operating System and Chrome binary [here](https://chromedriver.chromium.org/downloads)
- org_link: The main url for your Salesforce Org like: https://YOURDOMAIN.my.salesforce.com/
- login_url: Specify if the driver your login to a sandbox or production. By default production login: https://login.salesforce.com/
- is_headless: Configures Selenium to run on headless mode.

### download_backups

Main method to download back ups
```python
backup_instance.download_backups(download_location='TARGET LOCATION',backup_url='ORG URL/lightning/setup/DataManagementExport/home',user_name='USERNAME',password='PASSWORD')
```

#### Parameters

- download_location: The absolute path to the location where the download files will be saved
- backup_url: The lightning or classic URL of the Data Export Servive typically for classic: https://YOURDOMAIN.my.salesforce.com/ui/setup/export/DataExportPage/d?setupid=DataManagementExport
- cookies: Optional parameter if you prefer to handle authentication yourself. Pass the oid and sid cookies to the package in the selenium format as below:

- user_name: The username to login to the org if cookies are not passed
- password: The password to login to the org if cookies are not passed

### Optimal usage

Combine this package with a Python script and a task scheduler to run this package on a weekly basis. This will give you total control over storage locations and credential vaulting.

## Background
I created this package to make my life easier downloading data backups from the Weekly Export Service of Salesforce.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

