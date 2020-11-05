import os,re,time
def get_components(seg):
    pattern = re.compile(r'([a-zA-Z]+[0-9]+)')  # 查找数字
    components = pattern.findall(seg)
    dict={}
    for i in range(len(components)):
        j = 0
        key = ""
        while j < len(components[i]) and components[i][j].isdigit() == False:
            key = "".join((key, components[i][j]))
            j += 1
        dict[key]="".join((components[i][j:]))

    components=sorted(dict.items(),key=lambda k: int(k[1]),reverse=True)
    return components

def get_data(recv_file_dir):
    data=[]
    un7z_path=recv_file_dir
    for root0,un7z_root_dirs,files0 in os.walk(un7z_path):         #folder=  'D:\\7z\\10-27'
        for un7z_root_dir in un7z_root_dirs:
            un7z_root_path = os.path.join(un7z_path, un7z_root_dir)        #folder0='D:\\7z\\10-27\\10-27扫描'
            for root1, device_dirs, files1 in os.walk(un7z_root_path):
                for device_dir in device_dirs:
                    device_path = os.path.join(un7z_root_path, device_dir)  # folder1: 'D:\\7z\\10-27\\10-27扫描\\A设备10-27'
                    for root2, records, files2 in os.walk(device_path):
                        for record in records:  # dir3 :   D A SS040 A49C19R17N14SP1  K
                            seg = record.split(' ')
                            components_list = get_components(seg[3])
                            components = {} #以json 插入 T_acq
                            t_component = [] #分离 插入 T_com
                            for i in components_list:
                                components[i[0]] = i[1]
                                t_component.append({
                                    "component_name": i[0],
                                    "content": i[1]
                                })
                            tmp = {
                                "fabrice_id": seg[2],
                                "device_id": seg[0],
                                "data_path": os.path.join(device_dir, record),
                                "main_component": components_list[0][0],
                                "components": components,
                                "t_component": t_component,
                                "weaving_type":seg[-1],
                            }
                            data.append(tmp)
    print("data",data)
    print("data_length", len(data))
    return data


if __name__ == '__main__':
    data=get_data('./recv/12312');
    print(data)