import express from 'express';
import bodyParser from "body-parser"

const data = {}

const app = express();


app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())


app.get('/', (request, response) => {
    response.send("Hello world!")
})

app.post("/register", (request, response) => {
    console.log(request.body)

    response.send(request.body)
})

app.listen(3000, () => {
    console.log("port listening on port 3000")
})