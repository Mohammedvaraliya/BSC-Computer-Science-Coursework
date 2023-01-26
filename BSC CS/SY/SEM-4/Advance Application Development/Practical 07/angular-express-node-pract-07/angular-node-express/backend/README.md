# Advanced Application Development Practical (6 & 7)

## Initializing a Express project.

1. Initialize a `node` project using `npm`.

   ```bash
    npm init -y
   ```

1. Install all the dependencies (i.e. Express, BodyParse)

   ```bash
   npm i express body-parser
   ```

1. Install `nodemon` as a dev dependency.

   ```bash
   npm i -D nodemon
   ```

## Configuring the scripts in `package.json`

1.  Add the following scripts to your `package.json` file.
    ```json
    {
      "name": "backend",
      "version": "1.0.0",
      "description": "",
      "main": "index.js",
      "type": "module", // In order to use import/export syntax. Not defining this would require you to use require() function.
      "scripts": {
        "dev": "nodemon index.js", // Starting the app in development mode
        "start": "node index.js" // Starting the app in production mode
      },
      "author": "Subhashish Nabajja",
      "license": "ISC",
      "dependencies": {
        "body-parser": "^1.20.1",
        "express": "^4.18.2",
        "mongodb": "^4.13.0",
        "mongoose": "^6.8.4"
      },
      "devDependencies": {
        "nodemon": "^2.0.20"
      }
    }
    ```

## Coding the `Express` server.

1. Create `index.js` file in your root directory.

   ```bash
   touch index.js
   ```

1. Initialize `express` server.

   ```javascript
   import express from "express";

   const app = express();

   app.listen(3000, () => {
     console.log("port listening on port 3000");
   });
   ```

1. Now to store the data we would generally use a database, but for now we are going to use a simple Javasript object to store the data. Declare a object at the top of the file.

   ```javascript
   import express from "express";

   const data = {}; // Store all the data here
   const app = express();

   app.listen(3000, () => {
     console.log("port listening on port 3000");
   });
   ```

## Configuring routes and `http` methods

1. First we define our general endpoint.

   ```Javascript
   //index.js
   import express from "express";

   const data = {}; // Store all the data here
   const app = express();

   app.get("/", (request, response) => {
        response.send("Welcome to Student Registration Portal.");
   });

   app.listen(3000, () => {
    console.log("port listening on port 3000");
   });
   ```

1. Now we need the endpoints for CRUD operations.

   ```Javascript
   // CREATE
   app.post("/student", (request, response) => {
    const student = request.body;
    // Check if the roll no exists
    if (Object.keys(data).includes(student.rollNo.toString())) {
        response.statusCode = 409;
        return response.send("Student already exists.");
    }
    // Add record to memory
    data[request.body.rollNo] = request.body;response.statusCode = 200;
    response.send("Data added successfully");
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
   ```

## Starting the application

To start the application run `npm run start` (or `npm run dev` to start in development mode. )
