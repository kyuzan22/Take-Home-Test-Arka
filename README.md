# Inventory API and Python Function

This repository contains an Inventory API and a Python function for removing duplicate elements from a list. 🚀

## Inventory API

### Overview

The Inventory API provides endpoints to manage products, users, and client collaborations for an oil and gas company. It includes the following features:

1. **Database Design:**
   - Three tables: `users`, `products`, and `clients`.
   - Columns for user information (pk_user_id, userid, name, email, password), product details (pk_product_id, product_id,product_name, product_description, price), and client (pk_client_id, service_id, user_id, colaboration_startdate, contract_value).

2. **API Endpoints:**
   - `api/noAuthProducts`: Get a list of all available products without authorization.
   - `api/noAuthProducts`: Get a list of all available products with user authorization.
   - `api/users`: Retrieve user information.
   - `api/clients`: Access client collaboration details.
   - `/login`: Access user token for log in.

3. **Integration Testing:**
   - Integration test to verify the correctness of API endpoints.
   - Use tools like postman for better experience.

### How to Run

1. Restore `arkadata_test.bak` file provided in Database folder to you SQL server

2. Clone this repository:
   ```
   git clone https://github.com/kyuzan22/Take-Home-Test-Arka.git
   ```

3. Open Backend folder on your command prompt, gitbash, or visual studio code terminal :
   ```
   cd Backend
   ```

4. Install dependencies for backend:
   ```
   npm install
   ```

5. Setting the Server connection to your SQL server on dBConfig inside app.js:
   ```
   const dbConfig = {
     user: 'sa', // Replace with your Server authentication user , delete this if you're using windows auth
     password: 'Test123!', // Replace with your Server password, delete this if you're using windows auth
     server: 'DESKTOP-AIJNSUU\\DZIKRISQLSERVER', // Replace with your Server password
     database: 'arkadata_techtest',
     options: {
       trustServerCertificate: true,
     },
   };
   ```

6. Run the API:
   ```
   npm start
   ```

7. Access the API at `http://localhost:3000/api/test`.

8. Open Postman app or other api test tool and run your testing. example:
   - Login (POST) = http://localhost:3000/login
     ```
     {
       "username": "dzikriqomar",
       "password": "testPassword"
     }
     ```
   - Product list without Authorization (GET) = http://localhost:3000/api/authProducts
     ```
     Headers :
        Authorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7InBrX3VzZXJfaWQiOjEsInVzZXJpZCI6ImR6aWtyaXFvbWFyIiwibmFtZSI6ImR6aWtyaSIsImVtYWlsIjoiZHVtbXlAbWFpbC5jb20iLCJwYXNzd29yZCI6IiQyYiQxMCRlajE3V29Ca2xLa2dZWVRwMW9OZzIuYnpqZG95d09iVnJCR1BQRkM1ODBlbHo1THZTeUQuQyJ9LCJpYXQiOjE3MTk0MTU4NTcsImV4cCI6MTcxOTQxOTQ1N30.iNZvw2yngr7uurK9cjtFFt77ONqWK_rY9GGTTMiU-Qg
     ```
   - Product list without Authorization (GET) = http://localhost:3000/api/noAuthProducts
     Can run directly on the link

### Password Hash
You can create your own password hasher by :
1. Open file PasswordHasher.js

2. Put your password that want to be hashed on plainPassword const. i.e :
   ```
   const plainPassword = 'testPassword';
   ```
3. Run the code by run :
   ```
   node PasswordHasher.js
   ```

4. Your hashed password display on log

## Python Function

### Remove Duplicates from a List

The Python function `remove_duplicates(lst)` removes duplicate elements from a list while preserving the order.

### How to Run Unit Tests

1. Ensure you have Python installed.

2. Open file Python_Technical_Test.py in vs code

3. Or Use the cd command to navigate to the directory where Python_Technical_Test.py file is located:
   ```
   cd Python
   ```

4. Run the unit tests:
   ```
   python -m Python_Technical_Test.py
   ```

5. You can also modified the input by open the file. And un-comment the code inside main


## Questions or Issues?

If you have any questions or encounter issues, feel free to open an issue through this repository or my personal contact.