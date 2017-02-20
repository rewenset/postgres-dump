from subprocess import Popen
from datetime import datetime
import os
import dropbox

# setting to create dump file
PATH_TO_DUMPER 		= r'C:\Program Files\PostgreSQL\9.5\bin\pg_dump.exe'
PATH_TO_DUMP_FILE 	= r'C:\temp_dump_file.txt'
DATABASE_NAME 		= 'postgres'
PASSWORD 			= 'admin'

# settings to upload dump file to Dropbox
ACCESS_TOKEN 		= '************'
TIME 				= datetime.now().strftime("%d-%m-%Y_%H%M")
DROPBOX_FOLDER 		= '/postgres-dumps/'
DROPBOX_FILE_NAME 	= 'dump' + TIME + ".txt"
DROPBOX_FULL 		= DROPBOX_FOLDER + DROPBOX_FILE_NAME


command = '"{}" {} > "{}"'.format(PATH_TO_DUMPER, DATABASE_NAME, PATH_TO_DUMP_FILE)
os.putenv('PGPASSWORD', PASSWORD)
output = Popen(command, shell=True)


client = dropbox.client.DropboxClient(ACCESS_TOKEN)
with open(PATH_TO_DUMP_FILE, 'rb') as f:
	response = client.put_file(DROPBOX_FULL, f)
	
os.remove(PATH_TO_DUMP_FILE)	# clean-up
