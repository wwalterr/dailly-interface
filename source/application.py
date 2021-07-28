from fastapi import FastAPI, Request

from fastapi.middleware.gzip import GZipMiddleware

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse


application = FastAPI()

application.mount('/static', StaticFiles(directory='static'), name='static')

application.add_middleware(GZipMiddleware, minimum_size=1000)

templates = Jinja2Templates(directory='templates')


@application.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
