import os
import ingredient_analysis_backend.setting as Config
from ingredient_analysis_backend import logger


def relocate(un7z_root,dest):#root : 10-27
    try:
        if not os.path.exists(Config.UN7Z_FILE_DEST):
            os.makedirs(Config.UN7Z_FILE_DEST)  # 路径不存在时创建路径

        for root1, un7z_date_dirs, files1 in os.walk(un7z_root): # un7z_date_dirs: ['10-27扫描']
            for un7z_date_dir in un7z_date_dirs:   # un7z_date_dir: '10-27扫描'
                un7z_date_path=os.path.join(un7z_root,un7z_date_dir)
                for root2, un7z_device_dirs, files2 in os.walk(un7z_date_path):  #un7z_date_dirs: ['10-27扫描']
                    for un7z_device_dir in un7z_device_dirs:
                        frm=os.path.join(un7z_date_path,un7z_device_dir)  #un7z_date_path:'D:\\7z\\10-27\\10-27扫描'
                        dst=os.path.join(dest,un7z_device_dir)
                        os.rename(frm,dst)
                os.rmdir(un7z_date_path)
        os.rmdir(un7z_root)
    except Exception as e:
        logger.error("relocate error")
        raise Exception("无权限或文件已存在")
        return e
    return 1

if __name__ == '__main__':
    relocate("","")