# force-backup-automator

force-backup-automator is a library to automate the downloads of backups via the Salesforce Weekly Export Service

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install force-backup-automator
```

## Usage

```python
from force-backup-automator import BackupController

backup_instance = BackupController(driver_location='./chromedriver',org_link='ORG MAIN URL',is_headless=0)

backup_instance.download_backups(download_location='TARGET LOCATION',backup_url='ORG URL/lightning/setup/DataManagementExport/home',user_name='USERNAME',password='PASSWORD')
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)