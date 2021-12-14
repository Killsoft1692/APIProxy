import datetime

from starlette.requests import Request

from main import app, client


@app.get('/')
async def loader(request: Request):
    # For simplicity let's limit this only for GET requests
    data = {
        'added_at': datetime.datetime.now(),
        'query_params': request.query_params
    }
    await client.main['storage'].insert_one(data)
    return {'status': 'Received'}


@app.get('/queue_length')
async def show_queues_length(request: Request):
    count = await client.main['storage'].count_documents({})
    return {'requests_count': count}
