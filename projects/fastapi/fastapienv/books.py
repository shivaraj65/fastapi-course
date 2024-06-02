from fastapi import Body,FastAPI

app = FastAPI()

users_data = {
    1: {
        "user_id": 1,
        "name": "Alice Smith",
        "email": "alice.smith@example.com",
        "age": 28,
        "gender": "Female",
        "country": "USA",
        "is_active": True
    },
    2: {
        "user_id": 2,
        "name": "Bob Johnson",
        "email": "bob.johnson@example.com",
        "age": 34,
        "gender": "Male",
        "country": "Canada",
        "is_active": False
    },
    3: {
        "user_id": 3,
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "age": 22,
        "gender": "Male",
        "country": "UK",
        "is_active": True
    },
    4: {
        "user_id": 4,
        "name": "Diana Prince",
        "email": "diana.prince@example.com",
        "age": 30,
        "gender": "Female",
        "country": "Australia",
        "is_active": True
    },
    5: {
        "user_id": 5,
        "name": "Eve Adams",
        "email": "eve.adams@example.com",
        "age": 26,
        "gender": "Female",
        "country": "New Zealand",
        "is_active": False
    },
    6: {
        "user_id": 6,
        "name": "Frank White",
        "email": "frank.white@example.com",
        "age": 40,
        "gender": "Male",
        "country": "Ireland",
        "is_active": True
    },
    7: {
        "user_id": 7,
        "name": "Grace Lee",
        "email": "grace.lee@example.com",
        "age": 31,
        "gender": "Female",
        "country": "Singapore",
        "is_active": False
    },
    8: {
        "user_id": 8,
        "name": "Henry Clark",
        "email": "henry.clark@example.com",
        "age": 29,
        "gender": "Male",
        "country": "South Africa",
        "is_active": True
    },
    9: {
        "user_id": 9,
        "name": "Isabella Gomez",
        "email": "isabella.gomez@example.com",
        "age": 24,
        "gender": "Female",
        "country": "Spain",
        "is_active": True
    },
    10: {
        "user_id": 10,
        "name": "Jack Wilson",
        "email": "jack.wilson@example.com",
        "age": 35,
        "gender": "Male",
        "country": "USA",
        "is_active": False
    }
}


@app.get("/test")
async def first_api():
    return {'message':'hello from fastAPI'}

@app.get("/test2")
async def second_api():
    return users_data

@app.get("/dynamic_param/{params}")
async def paramApi(params):
    return {"entered_value" : params}

@app.post('/post_test')
async def funct(body=Body()):
    print(body)
    return body
