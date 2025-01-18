# 🍰 Confectionary Shop Billing System 🍰

Welcome to the *Confectionary Shop Billing System*! This web application allows you to manage customer billing efficiently while generating beautiful PDF receipts. Perfect for any confectionery shop looking to streamline their billing process!

---

## 📜 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Use](#how-to-use)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Contributing](#contributing)

---

## 🕹 Introduction

This project is designed to help confectionery shops create and manage customer bills seamlessly. It utilizes a Flask backend with a MySQL database to store customer and product information, while also generating PDF receipts for each transaction.

---

## ✨ Features

- *User-Friendly Interface*: A simple web form for entering customer details and selecting products.
- *PDF Generation*: Automatically generates PDF bills using wkhtmltopdf.
- *Database Integration*: Stores customer and product data in a MySQL database.
- *Dynamic Product Selection*: Populate product options dynamically using JavaScript.

---

## 🤔 How to Use

1. *Run the Application*:
   - Start the Flask server by executing the Python script:
     
     python main.py
     
2. *Access the Web Interface*:
   - Open your browser and navigate to http://localhost:5000.

3. *Create a Bill*:
   - Fill in the customer name, select a product, and specify the quantity.
   - Click on "Create Bill" to generate the bill and download the receipt.

---

## ⚙ Technologies Used

- *Backend*: Python with Flask
- *Database*: MySQL
- *PDF Generation*: pdfkit (wkhtmltopdf)
- *Frontend*: HTML, CSS, JavaScript

---

## 📦 Installation

To set up this project locally, follow these steps:

1. Clone this repository:
   ```bash
   https://github.com/yourusername/confectionary-shop-billing.git

3. Navigate to the project directory:
    ```bash
   cd confectionary-shop-billing

4. Install the required packages:
     ```bash
   pip install flask mysql-connector-python pdfkit

5. Ensure you have MySQL installed and create a database named confectionary_shop.

6. Update the database configuration in app.py with your MySQL credentials.

7. Make sure wkhtmltopdf is installed and its path is correctly set in app.py.

---

## 🤝 Contributing

We welcome contributions! If you would like to enhance this project or add new features, feel free to fork the repository and submit a pull request.

---

## 🎉 Enjoy Billing!

Dive into an efficient billing experience with our Confectionary Shop Billing System! Happy selling! 🥳
   
