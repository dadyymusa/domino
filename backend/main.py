from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root_page():
    return {'message: Hello this is domino'}
