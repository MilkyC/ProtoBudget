ProtoBudget
===========

Russ family budget app. 


# Running Server

## Activate virtual environment:
```source ~/.venv/budget/bin/activate```

## Run Server
```python managey.py runserver```

## Modify object using web api
```
curl -H Content-Type: application/json; indent=4' -u <username>:<password> -X PUT -d '{"name": "Groceries", "default_allotment": "500.00"}' http://127.0.0.1:8000/api/categories/1/
```
