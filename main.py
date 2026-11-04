#Hospital Management System API

import psycopg2
from fastapi import FastAPI

def connection():
    return psycopg2.connect(host='localhost',database='Hospital_project',user='postgres',password='postgres123',port=5432)

app = FastAPI()

@app.post('/addpatients')
def add_patients_details(pid,name,phone,gender,disease,address):
    conn=connection()
    cur=conn.cursor()
    cur.execute("""insert into patients(pid,name,phone,gender,disease,address)values(%s,%s,%s,%s,%s,%s)""",(pid,name,phone,gender,disease,address))
    conn.commit()
    cur.close()
    conn.close()

    return {'message':'Patient details added successfully'}


@app.put('/update')
def update(pid,name):
    conn=connection()
    cur=conn.cursor()
    cur.execute('update patients set pid=%s where name=%s',(pid,name))
    conn.commit()
    cur.close()
    conn.close()
    return {'message':'Patient details updated successfully'}


@app.get('/readdata')
def patients_record():
    conn=connection()
    cur=conn.cursor()
    cur.execute('select * from patients')
    res=cur.fetchall()
    cur.close()
    conn.close()
    return {'message':'See your patients details','data':res}


@app.delete('/delete')
def delete_record(name):
    conn=connection()
    cur=conn.cursor()
    cur.execute('delete from patients where name=%s',(name,))
    conn.commit()
    cur.close()
    conn.close()
    return {'message':'Patient record deleted successfully'}