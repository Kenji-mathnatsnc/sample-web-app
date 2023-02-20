import json

payload: str = '{"sequence_nbr": "111","first_name":"aaaa","last_name": "bbbb","gender": "male", "roles": "admin"}'

data: dict = json.loads(payload)

print(data["sequence_nbr"])
