from flask import Blueprint, render_template, request, flash, redirect, url_for
import mysql.connector
from datetime import datetime
from PIL import Image
import json
import os
# import marketplace

mydb = mysql.connector.connect(
    user="owner", 
    password="4thstreet!",
    host="fourthstreet--warehouse.mysql.database.azure.com",
    port=3306,
    database="fourthstreetwarehouse", 
    ssl_ca="DigiCertGlobalRootCA.crt.pem", 
    ssl_disabled=False
    )

auth = Blueprint("auth", __name__)
currentEmail = ""
paymentNeeded = 0

@auth.route("/",  methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        emailAddress = request.form.get("email")
        password = request.form.get("password")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user where email_id ='" + str(emailAddress) + "'")
        myresult = mycursor.fetchall()

        if myresult == []:
            return render_template("loginDetails.html")
        if myresult[0][3] == password:
            global currentEmail
            currentEmail = emailAddress
            return redirect(url_for("auth.get_products"))
        else:
            return render_template("loginDetails.html")
    else:
        return render_template("loginDetails.html")
    

@auth.route("/registerCustomer",  methods = ["GET", "POST"])
def registerCustomer():
    if request.method == "POST":
        
        emailAddress = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        if password != confirmPassword or len(emailAddress) == 0:
            return render_template("registerDetails.html", text = "In register Customer")

        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        contact = request.form.get("contact")

        if len(firstName) == 0 or len(lastName) == 0 or len(contact) == 0:
            return render_template("registerDetails.html", text = "In register Customer")

        answerOne = request.form.get("answerOne")
        answerTwo = request.form.get("answerTwo")
        answerThree = request.form.get("answerThree")

        if len(answerOne) == 0 or len(answerTwo) == 0 or len(answerThree) == 0:
            return render_template("registerDetails.html", text = "In register Customer")
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO User (email_id, firstName, lastName, password, contact) VALUES (%s, %s, %s, %s, %s)"
        values = (emailAddress, firstName, lastName, password, contact)

        mycursor.execute(sql, values)
        mydb.commit()

        mycursor = mydb.cursor()
        sql = "INSERT INTO resetpassword (email_id, answer_one, answer_two, answer_three) VALUES (%s, %s, %s, %s)"
        values = (emailAddress, answerOne, answerTwo, answerThree)
        mycursor.execute(sql, values)
        mydb.commit()
        return render_template("loginDetails.html")
    return render_template("registerDetails.html", text = "In register Customer")

@auth.route("/forgetPassword",  methods = ["GET", "POST"])
def forgetPassword():
    if request.method == "POST":        
        emailAddress = request.form.get("email")
        password = request.form.get("password")
        confirmPassword = request.form.get("confirmPassword")
        answerOne = request.form.get("answerOne")
        answerTwo = request.form.get("answerTwo")
        answerThree = request.form.get("answerThree")

        if len(answerOne) == 0 or len(answerTwo) == 0 or len(answerThree) == 0 or len(emailAddress) == 0:
            return render_template("forgetPassword.html", text = "In forget Password")
        
        if password != confirmPassword:
            return render_template("forgetPassword.html", text = "In forget Password")
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM resetpassword where email_id ='" + str(emailAddress) + "'")
        myresult = mycursor.fetchall()

        if myresult == []:
            return render_template("loginDetails.html")

        if answerOne == myresult[0][1] and answerTwo == myresult[0][2] and answerThree == myresult[0][3]:
            mycursor = mydb.cursor()
            sql = "UPDATE user SET password = %s WHERE email_id = %s"
            val = (password, emailAddress)
            mycursor.execute(sql, val)
            mydb.commit()
        return render_template("csv.html", text = "In forget Password")

    return render_template("forgetPassword.html", text = "In forget Password")

@auth.route("/deleteUser",  methods = ["GET", "POST"])
def deleteUser():
    if request.method == "POST": 
        emailAddress = request.form.get("email")
        password = request.form.get("password")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM user where email_id ='" + emailAddress + "'")
        myresult = mycursor.fetchall()

        if myresult == []:
            return render_template("deleteUser.html", text = "In delete user")
        if myresult[0][3] != password:
            return render_template("deleteUser.html", text = "In delete user")
        else:
            mycursor = mydb.cursor()
            sql = "DELETE FROM user WHERE email_id = %s"
            val = (emailAddress,)
            mycursor.execute(sql, val)
            mydb.commit()

            return render_template("csv.html", text = "In forget user done")
    return render_template("deleteUser.html", text = "In delete user")

@auth.route("/message",  methods = ["GET", "POST"])
def message():
    if request.method == "GET":
        global currentEmail 
        emailAddress = currentEmail
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM negotiationmessage where seller_email ='" + emailAddress + "'")
        myresult = mycursor.fetchall()
        jsonMessage =[]
        for tuple in myresult:
            jsonMessage.append({'productId': tuple[0], 'from': tuple[2], 'message': tuple[3]})
        jsonMessage = json.dumps(jsonMessage)
        return render_template("message.html", text = jsonMessage)
    else:
        message = request.form.get("message")
        productId = request.form.get("productId")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT email_id FROM advertisement where product_id ='" + productId + "'")
        myresult = mycursor.fetchall()
        sql = "INSERT INTO NegotiationMessage (product_id, seller_email, buyer_email, note) VALUES (%s, %s, %s, %s)"
        values = (productId, myresult[0][0], currentEmail, message)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect(url_for("auth.get_products"))    

@auth.route("/payments",  methods = ["GET", "POST"])
def payments():
    if request.method == "POST":
        cardDetails = request.form.get("cardDetails")
        CVV = request.form.get("CVV")
        expiryDate = request.form.get("expiry")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        
        if len(cardDetails) == 0 or len(CVV) == 0 or len(expiryDate) == 0 or len(firstName) == 0 or len(lastName) == 0:
            return render_template("payments.html", text = currentPayment)
        return render_template("csv.html", text = "Thank you for Payment")       
    else:
        global currentEmail 
        emailAddress = currentEmail
        mycursor = mydb.cursor()
        mycursor.execute("SELECT amount_paid FROM payments where buyer_email ='" + emailAddress + "'")
        myresult = mycursor.fetchall()
        # jsonMessage =[]
        # for tuple in myresult:
        #     jsonMessage.append({'productId': tuple[0], 'from': tuple[2], 'message': tuple[3]})
        # jsonMessage = json.dumps(jsonMessage)

        global paymentNeeded
        paymentNeeded = myresult[0][0]
        currentPayment = paymentNeeded
        return render_template("payments.html", text = paymentNeeded)
        
        

@auth.route("/trial",  methods = ["GET", "POST"])
def trial():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM user")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

@auth.route("/marketplace",  methods = ["GET", "POST"])
def get_products():
    if request.method == "GET":
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Product")
        myresult = mycursor.fetchall()
        print(myresult)
        jsonMessage =[]
        for tuple in myresult:
            jsonMessage.append({'productId': tuple[0], 'description': tuple[3], 'productName': tuple[1], 'img': tuple[4], 'condition': tuple[5], 'date': tuple[6]})
        jsonMessage = json.dumps(jsonMessage)
        return render_template("showProducts.html", text=jsonMessage)
    
@auth.route("/add_product",  methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        productName = request.form.get("productName")
        # status = request.form.get("status")
        description = request.form.get("description")
        # xpicture_url = request.form.get("picture_url")
        product_condition = request.form.get("product_condition")
        date_of_listing = datetime.now().strftime('%d/%m/%Y')

        file = request.files['picture_url']
        image = Image.open(file)
        image_dir = 'fourthStreetWarehousebackend/static/img/'
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)
        
        image_path = os.path.join(image_dir, file.filename)
        image.save(image_path)

        pictureUrl = "static/img/" + str(file.filename)
        print(pictureUrl)
        mycursor = mydb.cursor()
        sql = "INSERT INTO Product (productName, status, description, picture_url, product_condition, date_of_listing) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (productName, 1, description, pictureUrl, product_condition, date_of_listing)

        global currentEmail
        mycursor.execute(sql, values)
        mydb.commit()

        sql = "SELECT product_id FROM Product WHERE productName = %s AND description = %s AND product_condition = %s AND date_of_listing = %s"
        values = (productName, description, product_condition, date_of_listing)

        mycursor.execute(sql, values)
        myresult = mycursor.fetchall()
        
        sql = "INSERT INTO advertisement(product_id, email_id) VALUES (%s, %s)"
        values = (myresult[0][0], currentEmail)
        mycursor.execute(sql, values)
        mydb.commit()

        return redirect(url_for("auth.get_products"))
    else:
        return render_template("addProduct.html")

@auth.route("/update_product",  methods = ["GET", "POST"])
def update_product():
    if request.method == "POST":
        productName = request.form.get("productName")
        # status = request.form.get("status")
        description = request.form.get("description")
        product_condition = request.form.get("product_condition")
        productId = request.form.get("productId")

        mycursor = mydb.cursor()
        sql = "UPDATE product SET productName = %s, description = %s, product_condition = %s WHERE product_id = %s"
        mycursor.execute(sql, (productName, description, product_condition, productId))
        mydb.commit()
        return redirect(url_for("auth.get_products"))
    else:
        productId = request.args.get("productId")
        print('r', productId)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Product WHERE product_id=%s", (productId,))
        myresult = mycursor.fetchall()
        jsonMessage =[]
        for tuple in myresult:
            jsonMessage.append({'productId': tuple[0], 'description': tuple[3], 'productName': tuple[1], 'condition': tuple[5]})
        jsonMessage = json.dumps(jsonMessage)
        print(jsonMessage)
        return render_template("updateProduct.html", text = jsonMessage)

@auth.route("/delete_product",  methods = ["GET", "POST"])
def delete_product():
    global currentEmail
    if request.method == "GET":
        emailAddress = currentEmail
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Product WHERE product_id IN (SELECT product_id FROM advertisement WHERE email_id = %s)", (emailAddress,))
        myresult = mycursor.fetchall()
        jsonMessage =[]
        for tuple in myresult:
            jsonMessage.append({'productId': tuple[0], 'productName': tuple[1], 'img': tuple[4], 'condition': tuple[3], 'date': tuple[6]})
        jsonMessage = json.dumps(jsonMessage)
        print(jsonMessage)
        return render_template("deleteProduct.html", text = jsonMessage)
    else:
        emailAddress = currentEmail
        mycursor = mydb.cursor()
        print("Here")
        print(request.form)
        print(request.form.get("productId"))
        mycursor.execute("DELETE FROM Product WHERE product_id=%s", (request.form.get("productId"),))
        mydb.commit()

        mycursor.execute("SELECT * FROM Product WHERE product_id IN (SELECT product_id FROM advertisement WHERE email_id = %s)", (emailAddress,))
        myresult = mycursor.fetchall()
        jsonMessage =[]
        for tuple in myresult:
            jsonMessage.append({'productId': tuple[0], 'productName': tuple[1], 'img': tuple[4], 'condition': tuple[3], 'date': tuple[6]})
        jsonMessage = json.dumps(jsonMessage)
        print(jsonMessage)
        return render_template("deleteProduct.html", text = jsonMessage)
