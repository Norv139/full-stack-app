
const { Pool } = require('pg')
const express = require('express')

const app = express()
//const host = '0.0.0.0'
const port = 8000

const {
    POSTGRES_HOST,
    POSTGRES_PORT
  } = process.env;

client = new Pool({
    host: POSTGRES_HOST || '0.0.0.0',
    port: POSTGRES_PORT || 5001,
    user: 'postgres',
    password: 'postgres',
    database: 'shop',
});

client.query("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'", (error, results) => {
    if (error) {
      console.log(error)
    }
    console.log(results.rows)
  })

const getAllTables = (request, response) => {
    client.query("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE'", (error, results) => {
      if (error) {
        console.log(error)
      }
      console.log('get tables')

      var rows =  results.rows.map(x=>x.table_name)
      
      response.status(200).json({"tables":rows})
    })
}
  
const getTable = (request, response) => {
    
    const { table } = request.params;

    client.query(`SELECT * FROM ${table}`, (error, results) => {
        if (error) {
            console.log(error)
        }
        console.log('get table')
        
        response.status(200).json({"table":results.rows})
    })
}

// -

app.get('/', (req, res)=>{
    res.send('/redoc')
})

app.get('/tables', getAllTables)

app.get('/tables/:table', getTable)


app.get('/redoc', (req, res)=>{
    res.send(
        [
            {
                url: '/tables',
                response: {tables: ['TableName', 'TableName', 'TableName', 'TableName']}
            },
            {
                url: '/tables/:TableName',
                response: {
                    table: [
                        {
                            any: 'any'
                        },
                        {
                            any: 'any'
                        },
                    ]
                }
            },
        ]
    )
})

app.listen(port, () =>
  console.log(`Server listens http://localhost:${port}`)
)
