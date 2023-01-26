import express from "express";
import bodyParser from "body-parser";

const data = {};

const app = express();

app.use(bodyParser.urlencoded({ extended: false }));

// parse application/json
app.use(bodyParser.json());

// 
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get("/", (request, response) => {
  response.send("Welcome to Student Registration Portal.");
});

// CREATE
app.post("/student", (request, response) => {
  const student = request.body;

  // Check if the roll no exists
  if (Object.keys(data).includes(student.rollNo.toString())) {
    response.statusCode = 409;
    return response.json({ message: "Student already exist" });
  }

  // Add record to memory
  data[request.body.rollNo] = request.body;

  response.statusCode = 200;
  response.json({ message: "Data added successfully" });
});

// READ
app.get("/student", (request, response) => {
  const rollNo = request.query.rollNo;
  // Check if record exists
  if (data[rollNo]) {
    response.statusCode = 200;
    return response.send(data[rollNo]);
  }

  response.statusCode = 404;
  response.send("Data not found");
});

// UPDATE
app.patch("/student", (request, response) => {
  const rollNo = request.query.rollNo;
  const password = request.body.password;

  // If the record exists and the password matches
  if (data[rollNo] && data[rollNo].password === password) {
    //Update data
    data[rollNo] = request.body;

    //Send confirmation message
    response.statusCode = 200;
    return response.send("Updated user.");
  }

  response.statusCode = 403;
  response.send("Invalid roll number or password.");
});

// DELETE
app.delete("/student", (request, response) => {
  const rollNo = request.query.rollNo;
  const password = request.body.password;

  // If the record exists and the password matches
  if (data[rollNo] && data[rollNo].password === password) {
    //Delete the record
    delete data[rollNo];

    //Send confirmation message
    response.statusCode = 200;
    return response.send("Deleted user.");
  }

  response.statusCode = 403;
  response.send("Invalid roll number or password.");
});

app.listen(3000, () => {
  console.log("port listening on port 3000");
});
