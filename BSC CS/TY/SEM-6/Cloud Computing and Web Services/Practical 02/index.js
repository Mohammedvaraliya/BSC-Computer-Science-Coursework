const express = require('express')
const cors = require('cors')
const app = express()
const port = 3000

app.use(cors())

app.get('/Uppercase', (req, res) => {
  // Accessing query parameters
  const queryTerm = req.query.query;

  res.send(`Result of Uppercase: ${queryTerm.toUpperCase()}`);
})

app.get('/Lowercase', (req, res) => {
  // Accessing query parameters
  const queryTerm = req.query.query;

  res.send(`Result of Lowercase: ${queryTerm.toLowerCase()}`);
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})