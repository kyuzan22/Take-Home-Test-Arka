const bcrypt = require('bcrypt');
const saltRounds = 10;

const plainPassword = 'testPassword';

// Generate a salt and hash the password
bcrypt.genSalt(saltRounds)
    .then((salt) => bcrypt.hash(plainPassword, salt))
    .then((hashed) => {
        console.log('Hashed password:', hashed);

        // Simulate user input (you'd get this from the login form)
        const userInputPassword = 'testPassword';

        // Compare the hashed password with the user input
        const result = bcrypt.compareSync(userInputPassword, hashed);

        if (result) {
            console.log('Password correct');
            // Proceed with authentication logic (e.g., grant access)
        } else {
            console.log('Password wrong');
        }
    })
    .catch((error) => {
        console.error('Error:', error);
    });
