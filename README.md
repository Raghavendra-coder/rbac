Role-Based Access Control (RBAC) System

1. Full Authentication and Authorization added using JWT.
2. Custom middleware and authorization decorators added for Industry level role and permission implementation
3. Custom Roles can be created and can be assigned
4. Role of an admin cannot be changed
5. There twi types of roles ie custom and default.
6. Default roles cannot be deleted
7. For permissions, option to create permissions is added. But practically it is not for end users, it can be added through APIs but suggestion is it should be added manully.
8. For that add permission in enums.py file in DelfaultPermissionEnum and run scripts to update to database
9. First you have to run add_all_permissions and then add_default_roles (root/main_utils.py) .
10. Except login and admin, you have to login and use the access_token/refresh_token.
11. access_token is for end users as it expires within an hour and refresh token is for devs as it expires in 3days.
12. After login you will get both in response.
        {
    "success": true,
    "message": "login success",
    "data": {
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@admin.com",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxLCJsYXN0X2xvZ2luIjoiMjAyNC0xMi0wNFQxNDo0MzoyNloiLCJpc19zdXBlcnVzZXIiOnRydWUsInVzZXJuYW1lIjoiYWRtaW4iLCJmaXJzdF9uYW1lIjoiQWRtaW4iLCJsYXN0X25hbWUiOiJBZG1pbiIsImVtYWlsIjoiYWRtaW5AYWRtaW4uY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJkYXRlX2pvaW5lZCI6IjIwMjQtMTItMDRUMTQ6NDM6MDlaIiwibW9iaWxlIjpudWxsLCJyb2xlIjoiODViMTIwOTEtYWEyNS00MzRlLThhZDYtNmJiYmQyNDM2YWE4IiwidXNlcl9wZXJtaXNzaW9ucyI6W119LCJleHAiOjE3MzM1MDQ1Nzl9.HiK80ri_-WyD8vHwbKqlBjASh-q8oDc9yOms9SxkPEQ",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoxLCJsYXN0X2xvZ2luIjoiMjAyNC0xMi0wNFQxNDo0MzoyNloiLCJpc19zdXBlcnVzZXIiOnRydWUsInVzZXJuYW1lIjoiYWRtaW4iLCJmaXJzdF9uYW1lIjoiQWRtaW4iLCJsYXN0X25hbWUiOiJBZG1pbiIsImVtYWlsIjoiYWRtaW5AYWRtaW4uY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJkYXRlX2pvaW5lZCI6IjIwMjQtMTItMDRUMTQ6NDM6MDlaIiwibW9iaWxlIjpudWxsLCJyb2xlIjoiODViMTIwOTEtYWEyNS00MzRlLThhZDYtNmJiYmQyNDM2YWE4IiwidXNlcl9wZXJtaXNzaW9ucyI6W119LCJleHAiOjE3MzM3NTI5Nzl9.2MxqsOdjHROkgWKi8Hu-fZ7sKnIxk3sN6GZAGHDjf9Q"
    }
}


13. These tokens are very strong and holds a lot of data about the user who is logged in.
14. These data get decrypted in custom middleware(created by me) and takes all the needed data for further API use.
15. After you get the token use these token in headers.
      Authorization - Bearer {{access_token}}
    Above is the format
16. This is bearer token.
17. Most of the data is added for testing the functionalities.
18. Also you can change the roles of users(only admin can do this and cannot change the role of another admin)
19. POSTMAN Collection is in root directory
20. For Admin access -> <base>/admin
    credentials : username : admin , password : 12345
