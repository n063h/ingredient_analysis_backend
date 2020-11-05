import py7zr

def un7z(filepath,un7z_path):
    f = py7zr.SevenZipFile(filepath, mode='r')
    f.extractall(path=un7z_path)
    f.close()
    return 1

if __name__ == '__main__':
    un7z("","")