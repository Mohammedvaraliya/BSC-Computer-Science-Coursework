MongoDB data models can be implemented using the MongoDB shell or a driver for your preferred programming language. Here's an example of how to create a data model in MongoDB using the shell:

Start the MongoDB shell by running the command mongo in your terminal.

Create a new database by running the command use 
    
    <database name> 

For example,

    use mydb.

Create a new collection by running the command 
    
    db.createCollection("<collection name>") 

For example, 

    db.createCollection("customers").

Insert documents into the collection using the command 
    db.<collection name>.insert(<document>) 

For example, 

    db.customers.insert({"name": "John Doe", "age": 30})

You can also insert multiple documents at a time by passing an array of documents to the insert command.

Verify the documents have been inserted by running the command 

    db.<collection name>.find().

    db.customers.find().