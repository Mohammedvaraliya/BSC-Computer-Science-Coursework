MongoDB documents are modified by connecting to a server, querying the proper documents, and then changing the setting properties before sending the data back to the database to be updated. CRUD is data-oriented, and it’s standardized according to HTTP action verbs.

When it comes to the individual CRUD operations:

* The Create operation is used to insert new documents in the MongoDB database.
* The Read operation is used to query a document in the database.
* The Update operation is used to modify existing documents in the database.
* The Delete operation is used to remove documents in the database.

### Create Operations

First we have to create database in mongodb shell
to display all the databases use command:

    show dbs

Now if you run next command, mongodb will create one database automatically for you 
which should be your active database

    use pract-02-mongodb

MongoDB provides two different create operations that you can use to insert documents into a collection:
1. insertOne()
2. insertMany()

insertOne()

now insert the data to the mongodb like this.

    db.testdata.insertOne({
        name: "John Doe",
        age: 20,
        citizen: "India"
    })

insertMany()

now insert more than one data to the mongodb like this.

    db.testdata.insertMany([{
        name:"Kailash", 
        age:20, 
        citizen:"India"
        }, 
        {
            name:"Scheffer", 
            age:22, 
            citizen:"US"
    }])


### Read Operations

MongoDB has two methods of reading documents from a collection:

* find()
* findOne()

find()

In order to get all the documents from a collection, we can simply use the find() method on our chosen collection. Executing just the find() method with no arguments will return all records currently in the collection.

    db.testdata.find()

If you want to get more specific with a read operation and find a desired subsection of the records, you can use the previously mentioned filtering criteria to choose what results should be returned.

    db.testdata.find({name: "John Doe"})

findOne()

In order to get one document that satisfies the search criteria, we can simply use the findOne() method on our chosen collection. If multiple documents satisfy the query, this method returns the first document according to the natural order which reflects the order of documents on the disk. If no documents satisfy the search criteria, the function returns null.

    db.testdata.findOne({name: "John Doe"}, {name: 0})



### Update Operations


For MongoDB CRUD, there are three different methods of updating documents:

* updateOne()
* updateMany()
* replaceOne()

updateOne()

We can update a currently existing record and change a single document with an update operation. To do this, we use the updateOne() method on a chosen collection, which here is “RecordsDB.” To update a document, we provide the method with two arguments: an update filter and an update action.

    db.testdata.updateOne({name: "John Doe"}, {$set: {age: 30}})


updateMany()

updateMany() allows us to update multiple items by passing in a list of items, just as we did when inserting multiple items. This update operation uses the same syntax for updating a single document.

    db.testdata.updateMany({name: "John Doe"}, {$set: {age: 30}})


replaceOne()

The replaceOne() method is used to replace a single document in the specified collection. replaceOne() replaces the entire document, meaning fields in the old document not contained in the new will be lost.

    db.testdata.replaceOne({name: "John Doe"}, {name: "Maki"}})


### Delete Operations


MongoDB has two different methods of deleting records from a collection:

* deleteOne()
* deleteMany()

deleteOne()

deleteOne() is used to remove a document from a specified collection on the MongoDB server. A filter criteria is used to specify the item to delete. It deletes the first record that matches the provided filter.

    db.testdata.deleteOne({age: 20})

deleteMany()

deleteMany() is a method used to delete multiple documents from a desired collection with a single delete operation. A list is passed into the method and the individual items are defined with filter criteria as in deleteOne().

    db.testdata.deleteMany({age: 20})