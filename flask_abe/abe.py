from flask import Flask, request, jsonify
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.abenc.abenc_yct14 import EKPabe
from charm.core.engine.util import objectToBytes, bytesToObject
import logging
import base64
import json
import os
os.environ['PYTHONUTF8'] = '1'

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
app = Flask(__name__)


group = PairingGroup('MNT224')
kpabe = EKPabe(group)

def convert_to_bytes_if_element(value):
    if isinstance(value, ):
        return value.export()
    return value

def print_nested_dict(data, indent=0):
    for key, value in data.items():
        if isinstance(value, dict):
            print('{}{}: (dict)'.format(' ' * indent, key))
            print_nested_dict(value, indent + 4)
        else:
            # value = convert_to_bytes_if_element(value)
            print('{}{}: {} ({})'.format(' ' * indent, key, value, type(value).__name__))

@app.route("/check")
def hello():
    try:
        print('test api')
        group = PairingGroup('MNT224')
        kpabe = EKPabe(group)
        attributes = [ 'ONE1', 'two', 'THREE']
        (master_public_key, master_key) = kpabe.setup(attributes)
        policy = '(ONE1 or THREE) and (THREE or two)'
        secret_key = kpabe.keygen(master_public_key, master_key, policy)
        print(policy,attributes)
        print('secrat type',type(secret_key))
        msg = "Some Random Message"
        cipher_text = kpabe.encrypt(master_public_key, msg.encode("utf-8"), attributes)
        print('cipher type',type(cipher_text))
        decrypted_msg = kpabe.decrypt(cipher_text, secret_key)
        if(msg==decrypted_msg):
            print('msg is same',decrypted_msg)
        else:
            print('not same msg')

        return jsonify({'decrypty':str(decrypted_msg)})
    except Exception as error:
        print('error is:',error)

@app.route("/encryption", methods=['POST'])
def encryption():
    try:
        patient_encrypted = {}
        input_json = request.get_json(force=True)
        p_dict = input_json['patient']
        p_dict['user'] = str(p_dict['user'])
        p_dict['status'] = str(p_dict['user'])
        patient_attributes = [input_json['doctor']['username'].upper(),input_json['patient']['treatment_type'].upper(),input_json['doctor']['department'].upper()]
        policy = '('+input_json['doctor']['username'].upper()+' or '+input_json['doctor']['department'].upper()+') and ('+input_json['doctor']['department'].upper()+' or '+input_json['patient']['treatment_type'].upper()+')'
        print('check policy and attributes')
        # group = PairingGroup('MNT224')
        # kpabe = EKPabe(group)
        print('making master keys.....',policy,patient_attributes)
        (master_public_key, master_key) = kpabe.setup(patient_attributes)
        print('master key done and secret key making')
        secret_key = kpabe.keygen(master_public_key, master_key, policy)
        print('sectar key generated',type(secret_key))
        for key,value in p_dict.items():
            print('check value',key,value,type(value))
            if value:
                cipher_text = kpabe.encrypt(master_public_key, value.encode("utf-8"), patient_attributes)
                patient_encrypted[key] = str(objectToBytes(cipher_text,group))
        patient_encrypted['secret_key'] = str(objectToBytes(secret_key,group))
        print_nested_dict(patient_encrypted)
        return jsonify(patient_encrypted)
    except Exception as error:
        logger.error(error)


@app.route("/decryption", methods=['POST'])
def decryption():
    try:
        input_json = request.get_json(force=True)
        print('check decryption',input_json)
        return 'ok'
    except Exception as error:
        logger.error(error)


if __name__ == "__main__":
    app.run(host='172.29.0.16', port=5003,debug=True, use_reloader=False)
