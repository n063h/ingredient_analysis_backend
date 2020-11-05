import os
import ingredient_analysis_backend.setting as Config
import logging

logging.basicConfig(level=logging.INFO)
def relocate(root,dest):
    try:
        if not os.path.exists(Config.UN7Z_FILE_DEST):
            os.makedirs(Config.UN7Z_FILE_DEST)  # 路径不存在时创建路径
        for root1, dirs1, files1 in os.walk(root): # dirs1: ['A设备10-27','B设备10-27']
            for dir in dirs1:   # dir: 'A设备10-27'
                frm=os.path.join(root1,dir) #root1:'D:\\7z\\10-27\\10-27扫描'
                dst=os.path.join(dest,dir)
                os.rename(frm,dst)
        os.rmdir(root)
    except Exception as e:
        logging.ERROR("relocate error",e)
        return e
    return 1

if __name__ == '__main__':
    relocate("","")