const express = require('express');
const packageJSON = require('./package.json');
const appVersion = packageJSON.version; // get app version
const jwt = require('jsonwebtoken'); // Import jwt package
const bcrypt = require('bcrypt'); // Import bcrypt package
const sql = require('mssql'); // Import the mssql package
const app = express();
const PORT = process.env.PORT || 3000;

// Secret key for signing JWTs (replace with your actual secret)
const secretKey = 'arkadataTechnicalTest9988';

// Create a pool to manage connections (SQL Server)
const dbConfig = {
  user: 'sa', // Replace with your Server authentication user , delete this if you're using windows auth
  password: 'Test123!', // Replace with your Server password, delete this if you're using windows auth
  server: 'DESKTOP-AIJNSUU\\DZIKRISQLSERVER', // Replace with your Server password
  database: 'arkadata_techtest',
  options: {
    trustServerCertificate: true,
  },
};

sql.connect(dbConfig, (err) => {
  if (err) {
    console.error('Error connecting to SQL Server:', err.message);
    process.exit(1);
  } else {
    console.log('Connected to SQL Server successfully! http://localhost:3000/api/test');
  }
});

const pool = new sql.ConnectionPool(dbConfig);
const poolConnect = pool.connect();


// Generate a JWT token
function generateToken(user) {
  return jwt.sign({ user }, secretKey, { expiresIn: '1h' });
}

// Middleware to verify token
function verifyToken(req, res, next) {
  const bearerHeader = req.headers['authorization'];
  if (typeof bearerHeader !== 'undefined') {
    const bearerToken = bearerHeader.split(' ')[1];
    req.token = bearerToken;
    next();
  } else {
    res.sendStatus(403);
  }
}

// Parser for getting request data body
const bodyParser = require('body-parser');
app.use(bodyParser.json()); // Parse JSON-encoded bodies
app.use(bodyParser.urlencoded({ extended: true })); // Parse URL-encoded bodies


//Test Connection on api
app.get('/api/test', (req, res) => {
  res.send(`backend app version ${appVersion}`);
});

// Login route
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    await poolConnect; // Wait for the pool to connect

    // Query the database for user data
    const result = await pool
      .request()
      .input('username', sql.VarChar(50), username)
      .query('SELECT * FROM Users WHERE userid = @username');

    const user = result.recordset[0]; // Assuming username is unique

    if (!user || !bcrypt.compareSync(password, user.password)) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    // Generate a JWT token
    const token = generateToken(user);

    res.json({ token });
  } catch (error) {
    console.error('Error fetching user data:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Protected route (requires authentication)
app.get('/api/authProducts', verifyToken, async (req, res) => {
  try {
    await poolConnect; // Wait for the pool to connect

    // Query the database for products
    const result = await pool.request().query('SELECT * FROM Products');

    // Send the products as JSON response
    res.json(result.recordset);
  } catch (error) {
    console.error('Error fetching products:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// UnProtected route (not requires authentication)
app.get('/api/noAuthUsers', async (req, res) => {
  try {
    await poolConnect; // Wait for the pool to connect

    // Query the database for products
    const result = await pool.request().query('SELECT * FROM Users');

    // Send the products as JSON response
    res.json(result.recordset);
  } catch (error) {
    console.error('Error fetching products:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

app.get('/api/noAuthProducts', async (req, res) => {
  try {
    await poolConnect; // Wait for the pool to connect

    // Query the database for products
    const result = await pool.request().query('SELECT * FROM Products');

    // Send the products as JSON response
    res.json(result.recordset);
  } catch (error) {
    console.error('Error fetching products:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

app.get('/api/noAuthClients', async (req, res) => {
  try {
    await poolConnect; // Wait for the pool to connect

    // Query the database for products
    const result = await pool.request().query('SELECT * FROM Clients');

    // Send the products as JSON response
    res.json(result.recordset);
  } catch (error) {
    console.error('Error fetching products:', error.message);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Error handling middleware
app.use((err, req, res, next) => {
  console.error('Error:', err.message);
  res.status(500).json({ message: 'Internal server error' });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
