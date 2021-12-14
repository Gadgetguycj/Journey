# main.py
# https://testdriven.io/blog/fastapi-jwt-auth
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-your-fastapi-path-operations
# https://testdriven.io/blog/fastapi-mongo/#mongodb

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8080, reload=True)