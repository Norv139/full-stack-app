const { Client } = require('pg')

const client = new Client({
    user: 'postgres',
    password: 'postgres',
    database: 'shop',
    host: 'localhost',
    port: 5001,
})
client.connect()
client.query('SELECT name FROM customer', (err, res) => {
    console.log('customer', res.rows)
})
