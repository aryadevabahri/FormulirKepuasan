import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import certifi
from datetime import datetime

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

ca = certifi.where()
client = MongoClient(MONGODB_URI,tlsCAFile=ca)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('qusioner_kepuasan.html')
@app.route('/datafull')
def data_display():
    return render_template('datafull.html')

@app.route('/databiasa')
def data_display_biasa():
    return render_template('data.html')

@app.route('/⬧︎♋︎❖︎♏︎♎︎♋︎⧫︎♋︎', methods=['GET','POST'])
def simpan_data():
    today = datetime.now()
    mytime = today.strftime('%y-%m-%d-%H-%M-%S')
    nama_receive = request.form["nama_give"]
    jeniskelamin_receive = request.form["jeniskelamin_give"]
    usia_receive = request.form["usia_give"]
    pendidikan_receive = request.form["pendidikan_give"]
    jenislayanan_receive = request.form["jenislayanan_give"]
    jawaban1_receive = request.form["jawaban1_give"]
    jawaban2_receive = request.form["jawaban2_give"]
    jawaban3_receive = request.form["jawaban3_give"]
    jawaban4_receive = request.form["jawaban4_give"]
    jawaban5_receive = request.form["jawaban5_give"]
    jawaban6_receive = request.form["jawaban6_give"]
    jawaban7_receive = request.form["jawaban7_give"]
    jawaban8_receive = request.form["jawaban8_give"]
    jawaban9_receive = request.form["jawaban9_give"]
    pekerjaan_receive = request.form["pekerjaan_give"]
    date = mytime
    id =f'{nama_receive}-{date}'
    doc = {
        'nama':nama_receive,
        'jeniskelamin':jeniskelamin_receive,
        'usia':usia_receive,
        'pendidikan':pendidikan_receive,
        'jenislayanan':jenislayanan_receive,
        'pekerjaan':pekerjaan_receive,
        'jawaban1':jawaban1_receive,
        'jawaban2':jawaban2_receive,
        'jawaban3':jawaban3_receive,
        'jawaban4':jawaban4_receive,
        'jawaban5':jawaban5_receive,
        'jawaban6':jawaban6_receive,
        'jawaban7':jawaban7_receive,
        'jawaban8':jawaban8_receive,
        'jawaban9':jawaban9_receive,
        'date':date,
        'id':id
    }
    db.data_kepuasan.insert_one(doc)
    return jsonify({
        'msg':'success',
        'url':'/sukses'
    })

@app.route('/♎︎♏︎●︎♏︎⧫︎♏︎♎︎♋︎⧫︎♋︎',methods=['POST','GET'])
def delete():
    id = request.form['id_give']
    db.data_kepuasan.delete_one({'id':id})
    return jsonify({'msg':'data berhasil di hapus'})


@app.route('/sukses')
def sukses():
    return render_template('sukses.html')

@app.route('/♎︎♋︎⧫︎♋︎',methods=['POST','GET'])
def data():
    massage_list = list(db.data_kepuasan.find({},{'_id':False}))
    return jsonify({'data': massage_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)