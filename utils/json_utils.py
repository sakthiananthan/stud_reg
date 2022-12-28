import json

def read_json(file):
    f=open(file)
    data=json.load(f)
    f.close()
    return data

def write_json(file, data):
    fw=open(file,"w")
    data_tw=json.dumps(data, indent=3)
    fw.write(data_tw)
    fw.close()