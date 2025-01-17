## Confectionary Shop Billing System

This project is a web-based billing system designed for a confectionary shop. It allows users to create bills, generate PDF receipts, and maintain a database of customers, products, and transactions. The system is built using Flask for the backend, MySQL for the database, and HTML, CSS, and JavaScript for the frontend.

Features
Customer Management: Add customer details for each bill generated.
Product Management: Select products with pre-defined prices.
Bill Generation: Create detailed bills with product name, quantity, and total price.
PDF Export: Generate and download bills as PDF receipts.
Responsive Design: User-friendly interface for billing.

Project Structure
├── app.py                # Backend application (Flask)
├── templates
│   ├── index.html        # Frontend form for creating bills
│   ├── bill_template.html # PDF template for bill receipt
├── static                # Directory for static files (CSS, JS, etc.)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

Technologies Used
Backend: Flask (Python)
Database: MySQL
Frontend: HTML, CSS, JavaScript
PDF Generation: pdfkit and wkhtmltopdf
Setup Instructions

Prerequisites
Install Python (>= 3.7) and MySQL.
Install wkhtmltopdf from wkhtmltopdf.org.

Installation
Clone the repository:
git clone https://github.com/your-username/confectionary-shop-billing-system.git
cd confectionary-shop-billing-system

Install dependencies:
pip install -r requirements.txt

Configure MySQL:
Update the database credentials in app.py:
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YourPassword',
    'database': 'confectionary_shop'
}

Run the application once to create the necessary tables:
python app.py

Set up wkhtmltopdf:
Update the wkhtmltopdf binary path in app.py:
config = pdfkit.configuration(wkhtmltopdf=r'path\to\wkhtmltopdf.exe')

Running the Application
Start the Flask server:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000/
API Endpoints
Create Bill: POST /create_bill

Request Body:
{
  "customer_name": "Aditya Tanya",
  "product_id": 1,
  "quantity": 2
}
Response:

{
  "message": "Bill created successfully",
  "pdf_url": "/download_bill/bill_1.pdf"
}
Download Bill: GET /download_bill/<filename>h

Screenshots:-
1. Billing Form
  ![Billing form](https://github.com/user-attachments/assets/da290f93-ef6a-4b69-880d-31639b98e57b)

2. PDF Receipt
   ![bill_19 1 _page-0001](https://github.com/user-attachments/assets/3e157a33-73f6-4573-ba44-a6c8e9c8032a)
   ![bill_17 1 _page-0001](https://github.com/user-attachments/assets/cdd49fc1-24b8-45d2-8f26-0d2a2d1912bb)

Future Enhancements
Add user authentication for secure access.
Implement product inventory management.
Integrate real-time payment gateways.
