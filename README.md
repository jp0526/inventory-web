# Flask Inventory Management API

## Features
- View All Items – Retrieve a list of all items and their stock quantities.

- Search Item – Find a specific item using its ID.

- Add Item – Add a new product with its stock quantity.

- Update Item – Update the stock quantity of an existing product.

- Delete Item – Remove an item from the database.

- JSON Responses – Sends and receives data in JSON format.

- Error Handling – Returns a 404 error when an item cannot be found.


## How to Run
- Clone or download the repository.

- Install the required dependencies:

    ```
    pip install flask sqlalchemy
    ```

- Make sure your database configuration and models.py are properly set up.

- Run the application:

    ```
    python app.py
    ```

- Open your browser or API testing tool (such as Postman) and access:

    ```
    http://127.0.0.1:5000
    ```

API Endpoints

Method          Endpoint                Description

GET                 /                    Home Page
GET              /items                  Retrieve all items
GET           /items/<item_id>           Search an item
POST             /items                  Add new item
PUT           /items/<item_id>           Update item stock
DELETE        /items/<item_id>           Delete an item


- Example JSON for Adding an Item

{
    "product": "Keyboard",
    "stock_qty": 20
}

- Example JSON for Updating Stock

{
    "stock_qty": 50
}


## Programming Language and Technologies
- Python – Main programming language used to develop the application.

- Flask – Python web framework used to create API routes and handle HTTP requests.

- SQLAlchemy – ORM used to communicate with the database and manage records.

- JSON – Data format used for sending and receiving information.


## Data Structures
- List – Used to store and collect multiple item records when retrieving all items.

- Dictionary – Used to organize item information into key-value pairs, such as id, product, and stock_qty.

- Database Table – Used to permanently store inventory records, with each item represented as a database row.