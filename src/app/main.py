from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src.app.routers.auth import router as auth_router
from src.app.routers.devices import router as devices_router
from src.app.routers.analytics import router as analytics_router

app = FastAPI(
    title="Curvvtech Backend",
    version="0.1.0",
    description="Backend API for auth, device management, and analytics."
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost",
        "http://127.0.0.1",
        "*"  
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(devices_router, prefix="/devices", tags=["devices"])
app.include_router(analytics_router, prefix="/analytics", tags=["analytics"])

# Basic root endpoint
@app.get("/", tags=["health"])
def root():
    return {"status": "ok", "service": "curvvtech-backend"}

@app.get("/health", tags=["health"])
def health():
    return {"status": "healthy"}

# Run directly (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
