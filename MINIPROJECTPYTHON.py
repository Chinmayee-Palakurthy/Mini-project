from flask import Flask, render_template, request
import pymysql
mydb=pymysql.connect(host="localhost",user="root",password="gate2022",database="expert_spm")
cursor=mydb.cursor()
app = Flask(__name__)
@app.route('/')
@app.route('/mini')
def mainpage():
    return render_template('miniprojecthtml.html')
@app.route('/ph')
def pharm():
    return render_template('pharmacy.html')
@app.route('/spec')
def speci():
    return render_template('specialists.html')
@app.route('/doc')
def doct():
    return render_template('severe.html')
@app.route('/med')
def  medi():
    return render_template('general.html')
@app.route('/get_stores',methods=['POST','GET'])
def get_stores():
    if request.method == 'POST':
        cursor.execute("select  name,address,mobile from pharmacy where pincode=%s",(request.form['pic'],))
        result=cursor.fetchall()
        return render_template('addressoutput.html',data=result)
@app.route('/get_specialist',methods=['POST','GET'])
def get_specialist():
    if request.method == 'POST':
       cursor.execute(" select  name,hospital_name,degree,phno,address,exp,rating,about from doctor_details where specialist=%s",(request.form['spec'],))
       result=cursor.fetchall()
       return render_template('specialistoutput.html',data=result)
@app.route('/get_doc',methods=['POST','GET'])
def get_doc():
    if request.method == 'POST':
       cursor.execute(" select * from doctor_details inner join severe on doctor_details.specialist=severe.specialist where severe.symptom =%s",(request.form['sesm'],))
       result=cursor.fetchall()
       return render_template('severeoutput.html',data=result)
@app.route('/get_med',methods=['POST','GET'])
def get_med():
    if request.method == 'POST':
       if int(request.form['age'])<=15:
           cursor.execute("select * from general_symptoms inner join medicines on general_symptoms.disease=medicines.disease where age<=15 and general_symptoms.symptoms =%s",request.form['gsesm'],)
       if int(request.form['age'])>15:
           cursor.execute("select * from general_symptoms inner join medicines on general_symptoms.disease=medicines.disease where age>15 and general_symptoms.symptoms =%s",request.form['gsesm'],)
       result=cursor.fetchall()
       return render_template('generaloutput.html',data=result)
app.run()
