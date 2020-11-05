import time
from ingredient_analysis_backend.model import db,Base

def get_ms():
    return int(round(time.time() * 1000))


class T_acquisition_info(Base):
    # 表的名字:
    __tablename__ = 't_acquisition_info'

    # 表的结构:
    id = db.Column(db.String(32), primary_key=True)
    fabric_id = db.Column(db.String(32))
    device_id = db.Column(db.String(16))
    data_path = db.Column(db.String(255))
    main_component = db.Column(db.String(16))
    components = db.Column(db.JSON)
    weaving_type = db.Column(db.String(16))
    create_time = db.Column(db.BigInteger, default=get_ms)
    creator = db.Column(db.String(255))
    modified_time = db.Column(db.BigInteger, default=get_ms)
    modifier = db.Column(db.String(255))
    is_delete = db.Column(db.Integer, default=0)
    desc = db.Column(db.String(255))