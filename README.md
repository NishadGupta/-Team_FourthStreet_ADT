Final Project - Technical Report
Team: Aditya Ramachandra, Ganesh Arkanath, Nishad Gupta
Application URL:
NOTE: We were unable to host the project as our database is hosted on Azure and requires HTTPS access from hosting platforms. We tried pythonanywhere but unfortunately, it does not support HTTPS requests. URL: http://localhost:5000
Full GitHub URL:
We have uploaded the application source code with github.iu.edu at following URL
URL: https://github.iu.edu/napoom/Team_FourthStreet_ADT
Purpose
Project Summary
FourthStreet warehouse is a second hand marketplace that is located on W 4th St Bloomington. FourthStreet warehouse is a platform where people can purchase and sell used goods like clothing, electronics, furniture, cars, and other items. It's a platform that links buyers and sellers who want to buy or sell pre-owned goods with prospective buyers who are searching for inexpensive or distinctive goods. Typically, the procedure entails setting up an account, uploading images and descriptions of the object for sale, and deciding on a price. Buyers can peruse the available listings and get in touch with the vendor and arrange for shipping or pick-up.
Project Objective
To create a platform where people can purchase and sell used goods like clothing, electronics, furniture, cars, and other items. It's a platform that links buyers and sellers who want to buy or sell pre-owned goods with prospective buyers who are searching for inexpensive or distinctive goods. It solves the following problems.
●	Markets for used products promote recycling and reuse, which helps to cut waste and promotes sustainable consumption.
●	Used products are frequently considerably less expensive than their brand-new counterparts, making them a viable alternative for those on a tight budget.
●	Secondhand markets can support local communities and lessen the environmental effect of producing new products by facilitating the reuse of goods.
●	The ability to sell unwanted things for cash on second-hand marketplaces can be a wonderful source of income for both individuals and small business owners.
Project Usefulness
FourthStreet marketplace as a database would be helpful for a second-hand market for a number of reasons. First of all, it would make it possible to store and retrieve information about the goods being sold on the site, including specifics like descriptions, costs, and seller details. Customers will have an easier time finding what they're looking for thanks to the use of this data to simplify searching and filtering for particular goods. 
The database would be more useful if it had an interactive interface, for both buyers and vendors. It will make it simple to browse and search for products, view seller profiles, and navigate the site. An interactive interface might give sellers tools for controlling inventory and pricing. 
There are similar other marketplaces like eBay, Facebook marketplace etc. FourthStreet Marketplace is a single source database, mainly focused on selling and buying second hand products. The absence of any social user profile and overhead information results in shorter querying time and faster querying speed.
The target audience for our platform is anyone who wants to buy/sell second hand products.
How did we build our application
Data Storage:
We are using the MySQL database to store all the warehouse data. This database has been hosted on Azure cloud database, which provides easy management and maintenance of our database.
Backend:
For this project, we have employed Flask for backend development. Flask is a micro web framework using Python language and provides RESTful request dispatching.
Database Access, Connection and Operations:
We have used the following code snippet to connect the database with the Flask app. The database has already been hosted on Azure, and we connect using the proper parameters. This a very secure way of connecting as we provide username, password and SSL certificate of the database on Azure. The same will be used in our products as Well.
Below is our production database url
URL: fourthstreet--warehouse.mysql.database.azure.com
Frontend Languages: We use HTML and CSS to display our frontend web pages. We also use JavaScript for all the communication between the client and server. CSS provides styling for UI.
App Interactivity:
Users will be able to register and login on to our web app. Then, any user can either view and buy the products listed on our site or create a new listing and sell their product. We also allow the buyers to make the payment and order the product or negotiate the price with the seller by contacting them. The pages will include buttons and forms which will be used for getting the data from the users.
Architecture:
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/66e9dd28-f25e-4d14-84ad-5b0131488bdb)

 
Web App Layout
-	Login is the first page that will be displayed to the user once they open our app.
-	The product listing page is the menu panel of our web app.
-	We will be needing five pages for our webpage
-	We will be using a warehouse image as a background and sand brown black and whitecolor schema.
Tools:
We have implemented an entire application with lightweight Python web framework, Flask and Python language for server-side programming. We use MySQL for databases.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/8eb67744-4d3b-461e-aa81-b1ccd8d7c12e)

Model:
The model is developed using Flask RESTful APIs and MySQL database. View:
The views are developed using Flask render_template with HTML, JS Controller:
The controllers are developed using Flask Web Application routers
Tools Used:
Front End: Flask/HTML/JS
Back End: Python
Database: MySQL
Tools: Visual Studio Code, Python, Postman
Data
Dataset and Database
The initial data is self collected. Some of the columns that we have included are: productID, UserID, product name, product description, password, photo_url, price, category, user contact, note to seller, condition of product, date of listing
We are using the MySQL database to store all the warehouse data. This database has been hosted on Azure cloud database, which provides easy management and maintenance of our database.
 
Database Access, Connection and Operations
We have used the following code snippet to connect the database with the Flask app. The database has already been hosted on Azure, and we connect using the proper parameters. This a very secure way of connecting as we provide username, password and SSL certificate of the database on Azure. The same will be used in our products as well.
Below is our production database url
URL: fourthstreet--warehouse.mysql.database.azure.com
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/6d637596-aa79-4582-843c-31eda9c14093)

 
Here is a sample of MySQL database usage
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/6256cb35-a28f-4be5-ab69-784a12bbb6ba)

 
User Functionalities
Application supports the following functionalities
●	Register/Login
●	Buy product 
●	Sell Product
●	Update Product
●	Delete Product
●	Contact Seller
Register Page:
On this page, new users can register on our application by providing the necessary details.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/e289965a-be49-4403-aaa8-5a88c6d91451)

 
Login Page:
Once registered, users can log in via email and password. The user can also reset their password using security questions, and answers fetched during registration. All these details will be displayed in a form which will have to be filled by the users.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/dd51a292-735c-4c8a-ac10-3b0220ce163a)

 
Delete User page:
Here the user will be able to delete his profile. The necessary information will be fetched using form.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/d86a428b-7357-4b7a-9705-a36a73806de2)

 
Forgot Password:
Users can reset their passwords if forgotten by answering the security questions which were provided by the user during registration.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/c013b652-a3af-4bbb-a06f-ff7d3d4bd060)

 
Product Listing Page:
Here, the users can view all the products listed by the sellers on our application and select any of their choice. All the product listings will be shown in the form of a table.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/ffebd49b-9401-48e1-b64b-b89c8f38873b)

 
Sell Product:
Here the users can sell the product by adding a new listing. They will have to provide the necessary details about the product and add an image. All these required values will be displayed in a form which will have to be filled by the users.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/2e55c47a-8663-4987-a995-b521dec054e0)

Delete Product:
Here, the seller can delete the product that was listed by them. 
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/f233e21f-2e7c-4a6f-95ca-4195f36e4d54)

 
Update Product:
Here, the seller can delete the product that was listed by them.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/ad43596a-14ea-40e9-b87b-bed40c697d40)

 
Messaging:
Here, the user can negotiate the price by having a conversation with the seller. All the dialogue exchanged between the users will be stored on our database and displayed in the form of a table.
![image](https://github.com/NishadGupta/Team_FourthStreet_ADT/assets/29921061/d7e6e3f8-c564-4f05-bd16-228b7f0fc166)

 
●	The integration of frontend and backend on Flask was seamless. 
What could have been improved	●	Deployment could have been done better.
●	Could have stored images in a better way.
●	Could have used a NoSQL database instead of MySQL.
 

