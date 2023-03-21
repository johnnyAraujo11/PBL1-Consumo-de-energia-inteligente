import json
import file
import variables as var

'''
Salva os dados que chegam do medido em um arquivo json
'''
def save_json(msg):
    msg = json.loads(msg)
    num_measurer = msg.get("id")

    data = file.read(var.PATH_DATA_MEASURE)
    
    if(is_exit(num_measurer, data)):
        del msg["id"]
        meas_list = data.get(num_measurer)
        meas_list.append(msg)
        data[num_measurer] = meas_list
    
    file.write(data, var.PATH_DATA_MEASURE)
          
'''
Verifica se o medido existe
'''
def is_exit(num_meas, data):
    if num_meas in data:
        return True


