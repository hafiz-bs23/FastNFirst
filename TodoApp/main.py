from fastapi import FastAPI
from routers import auth, todo, admin, users


app = FastAPI()

@app.get("/health_check")
async def health_check():
    return {"message": "I am alive"}
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(admin.router)
app.include_router(users.router)
