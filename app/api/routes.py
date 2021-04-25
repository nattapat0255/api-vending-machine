from flask import Blueprint, request, jsonify, current_app
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message 
import sqlite3, datetime, traceback

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/vendors', methods=['GET'])
def getVendor():
  vendors = query('''SELECT * FROM vending_machine''')
  return jsonify(vendors)

@api.route('/vendors', methods=['POST'])
def addVendor():
  body = request.get_json()
  location_name = body['location_name']
  current_time = datetime.datetime.now()
  insert("INSERT INTO vending_machine (location_name, create_date, modified_date) VALUES ('{}', '{}', '{}')".format(location_name.encode('utf-8'), current_time, current_time))
  return {"message": "Add vendor success"}

@api.route('/sendmail', methods=['POST'])
def sendmail():
  body = request.get_json()
  location_name = body['location_name']
  product_name = body['product_name']
  product_remaining = body['product_remaining']
  with current_app.app_context():
    mail = Mail(current_app)
    msg = Message('Your Product are running out!', sender = current_app.config['MAIL_USERNAME'], recipients = [current_app.config['MAIL_RECEIVER']])
    msg.html = "Your Product are running out, Please refill your product.<br><b>Location</b> : {}<br><b>Product</b>: {}<br><b>Remaining</b>: {}<br><br>Thank you<br>Vending Machine".format(location_name, product_name, product_remaining)
    mail.send(msg)
  return {"message": "Mail has been sent!"}


def connection():
  con = sqlite3.connect('app/database.db')
  return con

def query(query_string):
  cur = connection().cursor()
  cur.execute(query_string)
  rows = cur.fetchall()
  return rows

def insert(query_string):
  con = connection()
  con.execute(query_string)
  con.commit()
  con.close()
  