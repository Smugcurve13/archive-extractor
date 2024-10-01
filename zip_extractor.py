import zipfile
def extract_archive(archive_path,dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(path=dest_dir)

if __name__ == '__main__':
    extract_archive("C:/Users/1000490/archive-extractor/test-for-archive.zip",
                    "C:/Users/1000490/archive-extractor/destination")