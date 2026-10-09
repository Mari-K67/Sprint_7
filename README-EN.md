# Sprint_7
API testing.

Task: test the API of the educational service [Яндекс Самокат](https://qa-scooter.education-services.ru) ([documentation](qa-scooter.education-services.ru/docs/)).
Before writing tests, test the API manually in Postman. This will help you understand how requests work.

## What you need to do
Test the endpoints. Check that they work correctly and return the necessary errors.

### Courier creation
Check:
* a courier can be created;
* you cannot create two identical couriers;
* to create a courier, you need to pass all required fields to the endpoint;
* the request returns the correct response code;
* a successful request returns {"ok":true};
* if one of the fields is missing, the request returns an error;
* if you create a user with a login that already exists, an error is returned.

### Courier login
Check:
* a courier can log in;
* to authorize, you need to pass all required fields;
* the system will return an error if you specify the login or password incorrectly;
* if any field is missing, the request returns an error;
* if you try to log in as a non-existent user, the request returns an error;
* a successful request returns id.

### Order creation
Check that when you create an order:
* you can specify one of the colors — BLACK or GREY;
* you can specify both colors;
* you can not specify any color;
* the response body contains track.

To test order creation, you need to use parametrization.

### Order list
* Check that the response body returns a list of orders.
