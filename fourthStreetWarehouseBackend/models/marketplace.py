# from flask import Blueprint, render_template, request, flash, redirect, url_for
# import mysql.connector

# import json
# from datetime import datetime

# mydb = mysql.connector.connect(
#     user="owner", 
#     password="4thstreet!",
#     host="fourthstreet--warehouse.mysql.database.azure.com",
#     port=3306,
#     database="fourthstreetwarehouse", 
#     ssl_ca="DigiCertGlobalRootCA.crt.pem", 
#     ssl_disabled=False
#     )

# marketplace = Blueprint("marketplace", __name__)

# @marketplace.route("/marketplace",  methods = ["GET", "POST"])
# def get_products():
#     if request.method == "GET":
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM Product")
#         myresult = mycursor.fetchall()
#         print(myresult)
#         jsonMessage =[]
#         for tuple in myresult:
#             jsonMessage.append({'productId': tuple[0], 'productName': tuple[1], 'img': tuple[4], 'condition': tuple[3], 'date': tuple[6]})
#         jsonMessage = json.dumps(jsonMessage)
#         return render_template("showProducts.html", text=jsonMessage)
    
# @marketplace.route("/add_product",  methods = ["GET", "POST"])
# def add():
#     if request.method == "POST":
#         productName = request.form.get("productName")
#         # status = request.form.get("status")
#         description = request.form.get("description")
#         picture_url = request.form.get("picture_url")
#         product_condition = request.form.get("product_condition")
#         date_of_listing = datetime.now().strftime('%d/%m/%Y')

#         mycursor = mydb.cursor()
#         sql = "INSERT INTO Product (productName, status, description, picture_url, product_condition, date_of_listing) VALUES (%s, %s, %s, %s, %s, %s)"
#         values = (productName, 1, description, picture_url, product_condition, date_of_listing)

#         print(auth.currentEmail)
#         mycursor.execute(sql, values)
#         mydb.commit()
#         return redirect(url_for("marketplace.get_products"))
#     else:
#         return render_template("addProduct.html")
