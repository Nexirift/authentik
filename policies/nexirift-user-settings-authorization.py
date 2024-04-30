

from humanize import naturalsize
from uuid import uuid4
from base64 import b64decode
from os import remove, makedirs
from os.path import isfile, isdir

AK_DOMAIN = "auth.nexirift.com"
FILE_PATH = "/media/user-media/"
URL_PATH = f"https://{AK_DOMAIN}{FILE_PATH}"
MAX_UPLOAD_SIZE = 5 * 1024 * 1024
ACCEPTED_FILE_TYPES = {
	"image/png": "png",
	"image/jpeg": "jpeg",
	"image/webp": "webp",
	"image/bmp": "bmp",
	"image/vnd.microsoft.icon": "ico"
}

EMPTY_FILE = "data:application/octet-stream;base64,"

def create_dir(type):
	dir_path = FILE_PATH + type
	if not isdir(dir_path):
		makedirs(dir_path)

def remove_old_file(type):
  file = request.user.attributes.get(type, None)
  if file:
    components = file.split(URL_PATH, 1)
    if len(components) == 2 and components[0] == "" and components[1]:
      old_filename = FILE_PATH + components[1]
      if isfile(old_filename):
        remove(old_filename)

def process_file(file_key, prompt_data):
	if file_key in prompt_data.get("attributes", {}):
		file_data = prompt_data["attributes"][file_key]
		if file_data == EMPTY_FILE:
			# No upload file specified, ignore
			del prompt_data["attributes"][file_key]
		else:
			file_mimetype = file_data.split("data:", 1)[1].split(";", 1)[0]
			if file_mimetype not in ACCEPTED_FILE_TYPES:
				ak_message(f"Invalid file type for {file_key}. Accepted types are: " + ", ".join(ACCEPTED_FILE_TYPES.values()))
				return False
			# Now we know it is one of the accepted file types
			file_base64 = file_data.split(",", 1)[1]
			file_binary = b64decode(file_base64)
			file_size = len(file_binary)
			if file_size > MAX_UPLOAD_SIZE:
				ak_message(f"{file_key} file size must not exceed " + naturalsize(MAX_UPLOAD_SIZE, binary=True, format="%.0f") + ".")
				return False
			# Set a random file name with extension reflecting mime type
			file_extension = ACCEPTED_FILE_TYPES[file_mimetype]
			file_filename = str(uuid4()) + "." + file_extension
			full_file_path = FILE_PATH + file_key + "/" + file_filename
			try:
				create_dir(file_key)
				with open(full_file_path, "wb") as f:
					f.write(file_binary)
			except:
				ak_message(f"Could not write {file_key} file.")
				return False
			remove_old_file(file_key)
			prompt_data["attributes"][file_key] = URL_PATH + file_key + "/" + file_filename
	
	return True

def process_files(prompt_data):
	if not process_file("avatar", prompt_data):
		return False
	if not process_file("banner", prompt_data):
		return False
	if not process_file("background", prompt_data):
		return False
	return True

prompt_data = request.context.get("prompt_data")

if not process_files(prompt_data):
	return False

return True