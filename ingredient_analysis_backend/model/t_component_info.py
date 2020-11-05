import time
from ingredient_analysis_backend.model import db,Base

def get_ms():
    return int(round(time.time() * 1000))

class T_component_info(Base):
    # 表的名字:
    __tablename__ = 't_component_info'

    # 表的结构:
    id = db.Column(db.String(32), primary_key=True)
    acquisition_id = db.Column(db.String(32))
    component_name = db.Column(db.String(16))
    content = db.Column(db.Integer)
    create_time = db.Column(db.BigInteger, default=get_ms)
    creator = db.Column(db.String(255),)
    modified_time = db.Column(db.BigInteger, default=get_ms)
    modifier = db.Column(db.String(255),)
    is_delete = db.Column(db.Integer, default=0)
    desc = db.Column(db.String(255))