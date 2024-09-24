from fastapi import FastAPI, BackgroundTasks, HTTPException, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# setup for jinja2 templates
templates = Jinja2Templates(directory = os.path.join(os.path.dirname(__file__), "templates"))

@app.get('/index', response_class= HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", context={'request': request})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", port = 5000, log_level = "info")