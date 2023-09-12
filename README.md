# hndx stagetwo

## How to run the application 
The application is built using django and django restframework(drf)
 
 To get the apllication up and running, you will need to install the requirments.txt file by using the command

```pip install requirments.txt```

This process will install the necessary libries to run the application.

## Testing the endpoints 
Below are the end points to perform the basic crud operations: 

```create: localhost:8000/api/create/```

This is to create a person. This endpoint will request for the name and save it to the database.

```get: localhost:8000/api/get/```

This will get all the data in the database

```getById: localhost:8000/api/byId/<id>```

This will get the data with the provided id 

```updateById: localhost:8000/api/byId/<id>```

This will update the data using the provided id 

```deleteById: localhost:8000/api/byId/<id>```

This endpoint will delete the data using the provided id


