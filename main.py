from celery import Celery
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


# RabbitMQをバックエンドとして使用する場合
celery = Celery("celery_sample", broker='amqp://guest:guest@rabbitmq//')


@celery.task
def add(x, y):
    return x + y


@app.get("/add/{x}/{y}")
async def execute_add(x: int, y: int):
    task = add.delay(x, y)
    return {"task_id": task.id}
