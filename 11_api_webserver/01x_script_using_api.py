import requests

requests.post('http://localhost:8000/users/4', json={'name': 'Alice', 'age': 30})
requests.post('http://localhost:8000/users/5', json={'name': 'Bob', 'age': 17})

requests.put('http://localhost:8000/users/1', json={'age': 37})
requests.put('http://localhost:8000/users/1', json={'name': 'Tim'})

print(requests.get('http://localhost:8000/users/1').json())
print(requests.get('http://localhost:8000/users/4').json())
print(requests.get('http://localhost:8000/users/5').json())

## Also, the mini-exercise solution:
# @app.put("/users/{user_id}", status_code=200)
# def update_user(user_id: int, name: str = Body(default=None), age: int = Body(default=None)):
#     if user_id not in users:
#         raise HTTPException(status_code=404, detail="User with that ID does not already exist")

#     # for simplicity, grab the current version of the object
#     current = users[user_id]

#     # add it to our list
#     users[user_id] = {
#         'name': name or current['name'],
#         'age': age or current['age']
#     }

#     return users[user_id]