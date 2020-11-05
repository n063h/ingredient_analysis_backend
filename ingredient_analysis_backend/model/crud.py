from ingredient_analysis_backend.model.t_acquisition_info import T_acquisition_info
from ingredient_analysis_backend.model.t_component_info import T_component_info
from ingredient_analysis_backend.model import db
import uuid
import logging
logging.basicConfig(level=logging.INFO)

def insert_info(list):
        for i in list:
            id_ta = "".join(str(uuid.uuid1()).split('-'))
            i['creator']=""
            i['modified_time']=0
            i['modifier']=""
            i['desc']=""
            ta = T_acquisition_info(id=id_ta,fabric_id=i['fabrice_id'], device_id=i['device_id'], data_path=i['data_path'],
                                   main_component=i['main_component'], components=i['components'], weaving_type=i['weaving_type'],
                                   creator=i['creator'], modified_time=i['modified_time'],
                                   modifier=i['modifier'], desc=i['desc'])
            db.session.add(ta)
            for component in i['t_component']:
                id_tc = "".join(str(uuid.uuid1()).split('-'))
                tc=T_component_info(id=id_tc,acquisition_id=id_ta,component_name=component['component_name'],content=component['content'],creator=i['creator'], modified_time=i['modified_time'],
                                   modifier=i['modifier'], desc=i['desc'])
                db.session.add(tc)
        db.session.commit()
        db.session.close()
