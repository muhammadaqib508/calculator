from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (Important!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve HTML file
@app.get("/")
def read_root():
    return FileResponse('static/index.html')

@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero!"}
    return {"result": a / b}
# Square
@app.get("/square")
def square(a: float):
    return {"result": a ** 2}

# Square Root
@app.get("/sqrt")
def sqrt(a: float):
    if a < 0:
        return {"error": "Cannot calculate square root of a negative number!"}
    return {"result": a ** 0.5}

# Percentage
@app.get("/percentage")
def percentage(a: float, b: float):
    return {"result": (a / b) * 100}

# Exponentiation
@app.get("/exponent")
def exponent(a: float, b: float):
    return {"result": a ** b}
