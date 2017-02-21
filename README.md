# postgres-dump
**creates dump file with pg_dump.exe and uploads it to Dropbox**
SETUP
---
**Once you have cloned the directory to your local machine:**

1. `cd` into `postgres-dump` directory.
2. Create virtual environment *(recommended)*.
2. Install requirements:
  `pip install -r requirements.txt`
3. Replace value of `ACCESS_TOKEN` in `DBdump.py` file with your dropbox token.

USAGE
---
*Administrative Privileges may be required*
```
python DBbump.py databaseName -p password -c
```
With this command we've set the password (`-p`) and clean-up (`-c`) properties.  
The result of this command:
```
(venv) path\to\project\postgres-dump>python DBdump.py postgres -p admin -c
[11:09:42] Creating dump file
[11:09:42] Uploading on Dropbox
[11:09:43] Cleaning up
[11:09:43] Done
```
Database name is positional argument.  
If password is not set - default ('admin') will be used.  
If not clean-up - dump file will be saved in project direcotry.  

The result of `help` command
```
(venv) path\to\project\postgres-dump>python DBdump.py -h
usage: DBdump.py [-h] [-p DB_PASS] [-c] db_name

Creates dump file with pg_dump.exe and uploads it to Dropbox

positional arguments:
  db_name               Name of a database.

optional arguments:
  -h, --help            show this help message and exit
  -p DB_PASS, --password DB_PASS
                        Password to a database.
  -c, --clean           Remove dump file from local storage.
```
