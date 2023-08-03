print('check charm..............////////////////...............')
from flask import Flask
from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
app = Flask(__name__)

@app.route("/check")
def hello():
    try:
        print('test api.............')
        group = PairingGroup('SS512')
        cpabe = CPabe_BSW07(group)
        msg = 'hello from flask'
        attributes = ['ONE', 'TWO', 'THREE']
        access_policy = '((four or three) and (three or one))'
        (master_public_key, master_key) = cpabe.setup()
        secret_key = cpabe.keygen(master_public_key, master_key, attributes)
        cipher_text = cpabe.encrypt(master_public_key, msg, access_policy)
        decrypted_msg = cpabe.decrypt(master_public_key, secret_key, cipher_text)
        print('decrypted_msg is:',decrypted_msg)
        return 'sdfghjk'
    except Exception as error:
        print('error is:',error)

@app.route("/encryption")
def encryption():
    try:
        pass
    except:
        pass
if __name__ == "__main__":
    print('main flask.............')
    app.run(host='172.29.0.16', port=5001)
