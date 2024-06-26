from fastapi import FastAPI
from .api.v1.api_v1 import router as api_router_v1

app = FastAPI(title="Image Recognition and De-Identification Service")

app.include_router(api_router_v1, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
