# api-vending-machine

## Project setup
```
pip install -r requirements.txt
```

### Compiles
```
export FLASK_APP=app
```
```
flask run 
```
### Email Configuration for sending & email
```
export MAIL_USERNAME={{email_sender(Gmail Only)}}
```
```
export MAIL_PASSWORD={{email_sender_password}}
```
```
export MAIL_RECEIVER={{email_receiver}}
```

### API Documentation
1. Get Vendors
```
GET http://localhost:5000/api/v1/vendors
```
2. Add Vendors
```
POST http://localhost:5000/api/v1/vendors (with JSON Body)
{
  "location_name" : "Kasetsart University  Ngamwongwan Rd., Chatuchak District, Bangkok"
}
```
3. Send Notification From Email
```
POST http://localhost:5000/api/v1/sendmail (with JSON Body)
{
  "location_name": "Kasetsart University  Ngamwongwan Rd., Chatuchak District, Bangkok",
  "product_name": "Soju",
  "product_remaining": "10 
}
```
Example : Receive message from email
![Image from iOS (1)](https://user-images.githubusercontent.com/81974292/116009077-bd109e00-a641-11eb-8ece-4c2852f7aff4.jpg)

