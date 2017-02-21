from subprocess import Popen
from datetime import datetime
import argparse
import os
import dropbox


# Dump file settings
PATH_TO_DUMPER 		= r'C:\Program Files\PostgreSQL\9.5\bin\pg_dump.exe'
TIME 				= datetime.now().strftime("%d-%m-%Y_%H%M%S")
DUMP_FILE_NAME 		= 'dump' + TIME + '.txt'
PATH_TO_DUMP_FILE 	= os.path.join(os.getcwd(), DUMP_FILE_NAME)

# Dropbox settings
ACCESS_TOKEN 		= '***'  # replace with your access token from Dropbox
DROPBOX_PATH 		= '/postgres-dumps/' + DUMP_FILE_NAME

def main():
	parser = init_args_parser()
	args = parser.parse_args()
	
	create_dump(args.db_name[0],args.db_pass)
	upload_dump()
	
	if args.clean:
		delete_dump()
	
	log('Done')
	
def init_args_parser():
	parser = argparse.ArgumentParser(
		description='Creates dump file with pg_dump.exe and uploads it to Dropbox'
	)
	
	parser.add_argument(
		'db_name', 
		metavar='db_name', 
		type=str, 
		nargs=1,
		help='Name of a database.'
	)
	
	parser.add_argument(
		'-p','--password',
		dest='db_pass',
		default='admin',
		help='Password to a database.'
	)
	
	parser.add_argument(
		'-c', '--clean',
		default=False,
		action='store_true',
		help='Remove dump file from local storage.'
	)
	
	return parser

def log(msg):
	print('[' + datetime.now().strftime('%H:%M:%S') + '] ' + msg)


def create_dump(db_name, db_pass):	
	log('Creating dump file')
	
	os.putenv('PGPASSWORD', db_pass)
	command = '"{}" {} > "{}"'.format(PATH_TO_DUMPER, db_name, PATH_TO_DUMP_FILE)
	proc = Popen(command, shell=True)
	proc.wait()

	
def upload_dump():
	log('Uploading on Dropbox')
	
	client = dropbox.client.DropboxClient(ACCESS_TOKEN)
	with open(PATH_TO_DUMP_FILE, 'rb') as f:
		response = client.put_file(DROPBOX_PATH, f)

		
def delete_dump():
	log('Cleaning up')
	os.remove(PATH_TO_DUMP_FILE)	# clean-up

	
if __name__ == '__main__':
	main()