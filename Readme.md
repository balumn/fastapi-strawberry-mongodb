# FastAPI GraphQL with MongoDB Boilerplate

This is a boilerplate application built with FastAPI, Strawberry GraphQL, and MongoDB. It provides a starting point for building a FastAPI application that uses GraphQL as the API layer and MongoDB as the backend database.

## Features

- Integration of FastAPI and Strawberry GraphQL.
- MongoDB integration for data storage.
- Example implementation of GraphQL queries and mutations.
- Boilerplate code for handling MongoDB operations.

## Prerequisites

- Python 3.8 or above
- MongoDB installed and running on your machine

## Installation

1. Clone the repository:

    ```commandline
   git clone origin git@github.com:balumn/fastapi-strawberry-mongodb.git
   ```   
2. Change to the project directory:
   ```commandline
    cd fastapi-strawberry-mongodb/
    ```
3. Create a virtual environment:
    ```commandline
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For Linux/Mac:

     ```
     source venv/bin/activate
     ```

   - For Windows (Command Prompt):

     ```
     .\venv\Scripts\activate.bat
     ```

   - For Windows (PowerShell):

     ```
     .\venv\Scripts\Activate.ps1
     ```

5. Install the dependencies:
    ```commandline
   pip install -r requirements.txt
   ```

6. Set up your MongoDB connection:

- Update the MongoDB connection string in `app/db.py`:

  ```python
  client = MongoClient("mongodb://localhost:27017")
  ```

- Modify the database name in `app/db.py`:

  ```python
  db = client["mydatabase"]
  ```
7. Run the application:
    ```commandline
   uvicorn main:app --reload
   ```
The application will be accessible at `http://localhost:8000`.

## Usage

- Open the GraphiQL interface to explore and test the GraphQL API:

Visit `http://localhost:8000/graphql` in your browser.

- Example queries/mutations to try:

- Get all users:

 ```graphql
 query {
   all_users {
     name
     photoUrl
     emailId
     mobile
     createdOn
     updatedOn
   }
 }
 ```

- Create a user:

 ```graphql
 mutation {
   create_user(userInput: {
     name: "John Doe",
     photoUrl: "https://example.com/photo.jpg",
     emailId: "john@example.com",
     mobile: "1234567890"
   }) {
     name
     photoUrl
     emailId
     mobile
     createdOn
     updatedOn
   }
 }
 ```

- Customize the GraphQL schema, resolvers, and MongoDB operations according to your application requirements.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

