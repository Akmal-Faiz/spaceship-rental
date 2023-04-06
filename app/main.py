from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import spaceship
from app.utils.custom_exception import *

app = FastAPI()

app.include_router(spaceship.router)

# Configure CORS middleware
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(NoValidResultException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"detail": exc.message},
    )

@app.exception_handler(DuplicateNameError)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.message},
    )