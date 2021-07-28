from fastapi import FastAPI

from fastapi.middleware.gzip import GZipMiddleware

from fastapi.staticfiles import StaticFiles

from fastapi.responses import RedirectResponse


application = FastAPI()

application.add_middleware(GZipMiddleware, minimum_size=1000)

application.mount(
    '/public', StaticFiles(directory='public', html=True), name='public')


@application.get('/', tags=['Index'])
async def index():
    return RedirectResponse('/public/index.html')
