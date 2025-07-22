import uvicorn
from fastapi import FastAPI

from src.applications.routers import people_routers as router


app = FastAPI(
    title="explicando fast API para o Joao",
    description="OI",
    version="1.0.0"
)

app.include_router(router.router_app, tags=["Webhooks"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)





