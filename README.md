# User List Application

Application that allows a user to view, add, and delete users from a list.


## Requirements
Python3 is needed with following requirements:

- Flask~=2.2.3
- Flask-SQLAlchemy
- Flask-WTF
- WTForms~=3.0.1
- email_validator


## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   

## Run:
1. Running the app:
   ```bash
    python app.py


### Potential optimizations

Optimizations can vary depending on scenario. Here are some potential optimizations:

- Using more elaborate database as OracleSQL, MySQL or NoSQL as MongoDB, DynamoDB.
- Cache frequent database queries to reduce the load on the database.
- Improving frontend UI design, including error messaging.
- Use a CDN to serve static assets from servers to reduce latency.
- Adding unit/integration test in perspective.
- Adding authentication/credentials.
- Implement a throttling mechanism to limit signals in specific scenarios.
- Form functionalities into libraries for better readability and maintainability.
- Utilize multiprocessing (or multithreading in some cases) for better performance.
- Use a more robust server framework, such as Gunicorn.
- Implement logging for analytics.

