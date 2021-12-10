import asyncio


class Scanner:
    def __init__(self):
        self._is_running = False

    async def run(self):
        asyncio.create_task(self._inner_job())

    async def _inner_job(self):
        self._is_running = True
        while self._is_running:
            await asyncio.sleep(1)

    async def stop(self):
        self._is_running = False
