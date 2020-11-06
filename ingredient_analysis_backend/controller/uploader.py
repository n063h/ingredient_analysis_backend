from ingredient_analysis_backend import app,logger
import os, json
from flask import request
from ingredient_analysis_backend.service.get_data import get_data
from ingredient_analysis_backend.service.relocate import relocate
from ingredient_analysis_backend.service.un7z import un7z
from ingredient_analysis_backend.model.crud import insert_info
from werkzeug.utils import secure_filename
import ingredient_analysis_backend.setting as Config




@app.route('/up', methods=['POST'])
def recv7z():
    try:
        file = request.files['file']
        file.filename = secure_filename(file.filename)
        logger.info(file.filename + " in process")
        if not os.path.exists(Config.RECV_FILE_DEST):
            os.makedirs(Config.RECV_FILE_DEST)  # 路径不存在时创建路径
            logger.info("new dir {} made".format(Config.RECV_FILE_DEST))
        filepath = os.path.join(Config.RECV_FILE_DEST, file.filename)  # 压缩包保存路径filepath: 7z/xx.7z
        # 保存压缩包
        file.save(filepath)
        logger.info(file.filename + ".7z saved")
        un7z_dir = file.filename[:-3]  # un7z_dir: xx
        un7z_path = os.path.join(Config.RECV_FILE_DEST, un7z_dir)  # 压缩包解压路径 un7z_path: 7z/xx
        # 解压
        un7z(filepath, un7z_path)
        logger.info(file.filename + ".7z un7zed")
        # 遍历解压文件夹,得到数据和解压后根目录
        data= get_data(un7z_path)
        logger.info(file.filename + "get_data success")
        # 插入数据
        insert_info(data)
        logger.info(file.filename + "crud success")
        # 修改数据路径
        relocate(un7z_path, Config.UN7Z_FILE_DEST)
        logger.info(file.filename + "relocate finished")

    except Exception as e:
        logger.critical("file.filename recv error")
        #要加 ensure_ascii=False,否则error是Unicode编码
        return json.dumps({"res": 'error', "error":str(e)},ensure_ascii=False)
    else:
        logger.info(file.filename + "proc success")
    return json.dumps({"res": 'success'})


@app.route('/', methods=['get'])
def hello():
    print("index get request")
    return "hello world"
