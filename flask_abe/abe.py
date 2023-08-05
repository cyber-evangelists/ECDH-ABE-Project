from flask import Flask, request, jsonify
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
import logging
import base64
import json

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
app = Flask(__name__)

@app.route("/check")
def hello():
    try:
        print('test api.............')
        group = PairingGroup('SS512')
        cpabe = CPabe_BSW07(group)

        msg = 'Patient: John Doe, Condition: Heart Disease, Medication: ABC'
        patient_attributes = ['DOCTOR:DrSmith', 'CONDITION:HeartDisease']
        doctor_attributes = ['DOCTOR:DrSmith']

        access_policy = '((DOCTOR:DrSmith and CONDITION:HeartDisease) or DOCTOR:DrBrown)'

        (master_public_key, master_key) = cpabe.setup()

        patient_secret_key = cpabe.keygen(master_public_key, master_key, patient_attributes)

        cipher_text = cpabe.encrypt(master_public_key, msg, access_policy)

        doctor_secret_key = cpabe.keygen(master_public_key, master_key, doctor_attributes)
        decrypted_msg = cpabe.decrypt(master_public_key, doctor_secret_key, cipher_text)

        print("Decrypted Message by Doctor:", decrypted_msg)

        return 'sdfghj14526k'
    except Exception as error:
        print('error is:',error)

@app.route("/encryption", methods=['POST'])
def encryption():
    try:
        patient_encrypted = {}
        input_json = request.get_json(force=True)
        p_dict = json.loads(input_json['patient'])
        logger.info('check recevied data'+input_json['patient'])
        logger.info('check dict')
        logger.info(p_dict)
        patient_attributes = ['DOCTOR:'+input_json['doctor']['username'], 'CONDITION:'+input_json['patient']['treatment_type']]
        doctor_attributes = ['DOCTOR:'+input_json['doctor']['username']]
        access_policy = '(DOCTOR:'+input_json['doctor']['username']+' and CONDITION:'+input_json['patient']['treatment_type']+')'
        group = PairingGroup('SS512')
        cpabe = CPabe_BSW07(group)
        c1 = ''
        c2 = None
        (master_public_key, master_key) = cpabe.setup()
        patient_secret_key = cpabe.keygen(master_public_key, master_key, patient_attributes)
        for key,value in p_dict.items():
            cipher_text = cpabe.encrypt(master_public_key, value, access_policy)
            logger.info('check cipher')
            logger.info(cipher_text)
            patient_encrypted[key] = base64.b64encode(cipher_text).decode('utf-8')
            c1 = base64.b64encode(cipher_text).decode('utf-8')
            c2 = cipher_text
        # if type(b'4') is bytes:
        #     return 'type is byte',200
        # if isinstance('',str):
        #     return 'string type',201
        return jsonify({'encryption':patient_encrypted})
    except Exception as error:
        logger.error(error) 

if __name__ == "__main__":
    app.run(host='172.29.0.16', port=5001)
