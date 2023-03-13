import json


def save_json(msg):
    #msg = json.loads('{"id":"001","pontecy":"800", "date": "08/03/2023", "time_on":"500", "hour":"10:00"}')
    msg = json.loads(msg)
    num_measurer = msg.get("id")

    data = ''
    with open("./Controller/DB_consumption.json", encoding='utf-8') as r_json:
        data = json.load(r_json)

        if(is_exit(num_measurer, data)):
            del msg["id"]
            meas_list = data.get(num_measurer)
            meas_list.append(msg)
            data[num_measurer] = meas_list

    with open("./Controller/DB_consumption.json", 'w') as json_file:
          json.dump(data, json_file, indent=5)


def is_exit(num_meas, data):
    if num_meas in data:
        return True



'''
    larsidwireless
   Porteiner: 
   usu: tec502
   senha: eunaoseiasenha
'''