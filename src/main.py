import uvicorn
from fastapi import FastAPI

from lib.config import Config

app = FastAPI()


@app.get('/')
async def root():
    return {'hello': 'world'}


@app.on_event('startup')
async def on_start():
    ...


@app.on_event('shutdown')
async def on_shutdown():
    ...


if __name__ == '__main__':
    c = Config()
    port = c.as_int('api.port', 8888)
    host = c.as_str('api.host', '0.0.0.0')
    reload = c.as_bool('api.reload', True)
    uvicorn.run('main:app', port=port, host=host, reload=reload)
