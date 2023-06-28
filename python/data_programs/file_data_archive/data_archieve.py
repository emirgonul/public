import os
import shutil
import datetime

def archive_data(source_dir, destination_dir):
    # Create a timestamp for the archive filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = f'data_archive_{timestamp}.zip'

    # Create the full path of the archive file
    archive_path = os.path.join(destination_dir, archive_name)

    try:
        # Create a ZIP archive of the source directory
        shutil.make_archive(archive_path[:-4], 'zip', source_dir)

        print(f'Data archived successfully: {archive_name}')
    except Exception as e:
        print(f'Failed to archive data: {str(e)}')

# Example usage
source_directory = '/path/to/source'
destination_directory = '/path/to/destination'

archive_data(source_directory, destination_directory)
