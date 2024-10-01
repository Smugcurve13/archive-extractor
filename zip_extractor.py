import zipfile
def extract_archive(archive_path,dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall()

if __name__ == '__main__':
    extract_archive("C:/Users/1000452/OneDrive - Compunnel/Desktop/udemy courses/python course/apps/bonus apps/archive extractor/test-for-archive.zip",
                    "C:/Users/1000452/Downloads/test-for-archive/dest")