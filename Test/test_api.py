import pytest
from httpx import AsyncClient

#import sys
#sys.path.append("../App")
import app


@pytest.mark.asyncio
async def test_read_tasks():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/tasks")
        assert response.status_code == 200
        assert response.json() == {"tasks": []}

##criar test create task
##criar test delete task
##resolver o problema do modulo app não localizado