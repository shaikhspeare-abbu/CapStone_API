from fastapi import FASTAPI, Request
from fastapi.responses import JS0NResponse


def register_exception_handlers(app: FastAPI):
    @app.add_exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JS0NResponse(status_code=500, content={'detail': str(exc)})
    