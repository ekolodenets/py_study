import os
import shutil
import uuid

# source directory
source_dir = "c:/Users/ULSE/Downloads/"
dest_dir_archives = source_dir + "archives/"
dest_dir_documents = source_dir + "documents/"
dest_dir_images = source_dir + "images/"
dest_dir_videos = source_dir + "videos/"
dest_dir_else = source_dir + "else/"

# extensions
archive_ext = ('rar', 'zip')
document_ext = ('doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx')
image_ext = ('jpg', 'jpeg', 'png', 'gif', 'bmp')
video_ext = ('mp4', 'avi', 'mkv', 'mov')



def move(source, target):
    file_exist = os.path.exists(target + source.name)       # Check if file already exists
    if file_exist:
        stamp = str(uuid.uuid4())[0:5]                      # generate random string
        new = source_dir + stamp + '_' + source.name        # create new file name
        os.rename(source.path, new)                         # rename file
        shutil.move(new, target)
    else:
        shutil.move(source.path, target)


with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.is_file():                                 # check if file
            if entry.name.endswith(archive_ext):
                move(entry, dest_dir_archives)
            elif entry.name.endswith(document_ext):
                move(entry, dest_dir_documents)
            elif entry.name.endswith(image_ext):
                move(entry, dest_dir_images)
            elif entry.name.endswith(video_ext):
                move(entry, dest_dir_videos)
            else:
                move(entry, dest_dir_else)
