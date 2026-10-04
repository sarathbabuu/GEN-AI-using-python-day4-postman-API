# import fastapi
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}




from fastapi import FastAPI

# Create FastAPI application
app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my first FastAPI application!"}

# Path parameter endpoint
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Welcome to FastAPI."}