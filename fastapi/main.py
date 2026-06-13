from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}       

@app.get("/about")
def about():
    return {"About": "This is a simple FastAPI application."
            "It demonstrates how to create a basic API with FastAPI."}

@app.get("/contactus")
def contact_us():
    return {"Contact": "You can reach us at contact@example.com."}
