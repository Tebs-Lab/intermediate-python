import requests

requests.post('http://localhost:8000/users/4', json={'name': 'Alice', 'age': 30})
requests.post('http://localhost:8000/users/5', json={'name': 'Bob', 'age': 17})

requests.put('http://localhost:8000/users/1', json={'age': 37})
requests.put('http://localhost:8000/users/1', json={'name': 'Tim'})

print(requests.get('http://localhost:8000/users/1').json())
print(requests.get('http://localhost:8000/users/4').json())
print(requests.get('http://localhost:8000/users/5').json())