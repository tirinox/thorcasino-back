import uvicorn
from fastapi import FastAPI

from blockchain.scanner import Scanner
from lib.config import Config

cfg = Config()
app = FastAPI()
scanner = Scanner()


@app.get('/')
async def root():
    return {'hello': 'world'}


@app.on_event('startup')
async def on_start():
    await scanner.run()


@app.on_event('shutdown')
async def on_shutdown():
    await scanner.stop()


if __name__ == '__main__':
    port = cfg.as_int('api.port', 8888)
    host = cfg.as_str('api.host', '0.0.0.0')
    reload = cfg.as_bool('api.reload', True)
    uvicorn.run('main:app', port=port, host=host, reload=reload)
