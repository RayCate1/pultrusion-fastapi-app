from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Enable running with `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
