from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

# Создаем экземпляр приложения FastAPI
app = FastAPI(title="Todo API", version="1.0.0")

# Модель данных для задачи
class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False

# "База данных" в памяти
todos = []
current_id = 0

# Твой первый эндпоинт!
@app.get("/")
async def root():
    return {"message": "Welcome to Todo API!"}

# Эндпоинт для получения всех задач
@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

# Запуск приложения
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)