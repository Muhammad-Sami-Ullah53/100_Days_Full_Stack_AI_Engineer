# 200 → Success
# 201 → Created
# 400 → Bad Request
# 401 → Unauthorized
# 403 → Forbidden
# 404 → Not Found
# 500 → Server Error

# 2xx → Success
# 4xx → Client made a problem
# 5xx → Server made a problem

import requests
response=requests.get("https://api.example.com/users")
print(response)
print(response.status_code)
print(response.text)