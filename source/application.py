from fastapi import FastAPI, Request

from fastapi.middleware.gzip import GZipMiddleware

from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates

from fastapi.responses import HTMLResponse, RedirectResponse

from starlette.exceptions import HTTPException as StarletteHTTPException

application = FastAPI(
    docs_url=None,
    redoc_url=None,
)

application.mount('/static', StaticFiles(directory='static'), name='static')

application.add_middleware(GZipMiddleware, minimum_size=1000)

templates = Jinja2Templates(directory='templates')


@application.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exception):
    return RedirectResponse('/')


@application.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@application.get('/privacy-policy', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('privacy_policy.html', {'request': request, 'title': 'Privacy Policy'})


@application.get('/terms-and-conditions', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('terms_and_conditions.html', {'request': request, 'title': 'Terms and conditions'})
