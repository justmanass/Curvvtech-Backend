
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.auth import router as auth_router
from src.routers.devices import router as devices_router
from src.routers.analytics import router as analytics_router

app = FastAPI(
    title="Curvvtech Backend",
    version="0.1.0",
    description="JWT auth, device management, and analytics endpoints.",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost",
        "http://127.0.0.1",
        "*",  
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(devices_router)
app.include_router(analytics_router)

# Health and root endpoints
@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "service": "curvvtech-backend"}

@app.get("/health", tags=["health"])
def health():
    return {"status": "healthy"}

# Local entry point 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host="127.0.0.1", port=8000, reload=True)
