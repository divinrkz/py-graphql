# py-graphql
GraphQL API built with Python FAST API

## GET STARTED
To get set the app up and running follow these steps carefully.

### Clone the repository

```bash
git clone https://github.com/divinirakiza/py-graphql.git
```

### Navigate to the codebase directory

```bash
cd py-graphql
```

### Create a virtual environment
Linux

```bash
pip install virtualenv # For first use
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Windows

```bash
pip install virtualenv #For first use
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```
## Data Seeding
Checkout ```products.json``` mock products list, you can add a product, delete, edit ...

## Graphql Playground
```
localhost:8000/graphql
```
