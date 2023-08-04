print('check charm..............////////////////...............')
from flask import Flask, request
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
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
        input_json = request.get_json(force=True) 
        group = PairingGroup('SS512')
        cpabe = CPabe_BSW07(group)
        return input_json
    except:
        pass
if __name__ == "__main__":
    app.run(host='172.29.0.16', port=5001)
