#backend

from flask import Flask, request, jsonify, render_template, send_file
import mysql.connector
import pdfkit
import os

app = Flask(_name_)

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',  # Update this with your MySQL username
    'password': 'hehe',  # Update this with your MySQL password
    'database': 'confectionary_shop'
}

# Specify wkhtmltopdf binary path 
config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')


# Create MySQL tables if they don't exist
def create_tables():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers
        (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), contact VARCHAR(15))
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products
        (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100), price FLOAT)
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bills
        (id INT PRIMARY KEY AUTO_INCREMENT, customer_id INT, date DATE, total FLOAT)
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bill_items
        (id INT PRIMARY KEY AUTO_INCREMENT, bill_id INT, product_id INT, quantity INT)
    ''')
    
    conn.commit()
    conn.close()

create_tables()

# API endpoint to create a new bill and generate PDF
@app.route('/create_bill', methods=['POST'])
def create_bill():
    data = request.json
    customer_name = data.get('customer_name')
    product_id = data.get('product_id')
    quantity = data.get('quantity')

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Insert customer
    cursor.execute("INSERT INTO customers (name, contact) VALUES (%s, %s)", (customer_name, ""))
    customer_id = cursor.lastrowid

    # Insert bill
    cursor.execute("INSERT INTO bills (customer_id, date, total) VALUES (%s, CURDATE(), %s)", (customer_id, 0))
    bill_id = cursor.lastrowid

    # Get product price and name
    cursor.execute("SELECT price, name FROM products WHERE id = %s", (product_id,))
    product_data = cursor.fetchone()
    price = product_data[0]
    product_name = product_data[1]

    # Calculate total price
    total_price = price * int(quantity)

    # Insert bill items
    cursor.execute("INSERT INTO bill_items (bill_id, product_id, quantity) VALUES (%s, %s, %s)", (bill_id, product_id, quantity))

    # Update total in bills table
    cursor.execute("UPDATE bills SET total = %s WHERE id = %s", (total_price, bill_id))

    conn.commit()
    conn.close()

    # Generate the PDF
    html = render_template('bill_template.html', customer_name=customer_name, product_name=product_name, quantity=quantity, total_price=total_price)
    pdf_filename = f'bill_{bill_id}.pdf'

    try:
        pdfkit.from_string(html, pdf_filename, configuration=config)
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return jsonify({'error': 'Failed to generate PDF'}), 500

    return jsonify({'message': 'Bill created successfully', 'pdf_url': f'/download_bill/{pdf_filename}'})

# Route to download the PDF bill
@app.route('/download_bill/<filename>')
def download_bill(filename):
    filepath = os.path.join(os.getcwd(), filename)
    return send_file(filepath, as_attachment=True)

# Route to render the index.html file
@app.route('/')
def index():
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
