


import logging,os
logging.basicConfig(level=logging.INFO)
def recv7z_handle(file):
    try:

        un7z_dir = file.filename[:-3]  # un7z_dir: xx
        un7z_path = os.path.join(Config.RECV_FILE_DEST, un7z_dir)  # 压缩包解压路径 un7z_path: 7z/xx
        # 解压
        un7z(filepath, un7z_path)
        # 遍历解压文件夹,得到数据和解压后根目录
        data, root = get_data(un7z_path)
        # 插入数据
        insert_info(data)
        # 修改数据路径
        relocate(root, Config.UN7Z_FILE_DEST)
    except Exception as e:
        print("recv7z error" + str(file.filename))
        logging.ERROR("recv7z error" + str(file.filename))
        return 0
    return 1