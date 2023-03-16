import json
import file

def save_json(msg):
    msg = json.loads(msg)
    num_measurer = msg.get("id")

    data = file.read("./Database/DB_consumption.json")
    

    if(is_exit(num_measurer, data)):
        del msg["id"]
        meas_list = data.get(num_measurer)
        meas_list.append(msg)
        data[num_measurer] = meas_list
    
    file.write(data, "./Database/DB_consumption.json" )
          


def is_exit(num_meas, data):
    if num_meas in data:
        return True



'''
    larsidwireless
   Porteiner: 
   usu: tec502
   senha: eunaoseiasenha
'''