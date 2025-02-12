from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.application.get_dice_roll import get_dice_roll


def create_app() -> FastAPI:
    app = FastAPI()

    app.add_api_route(path="/", endpoint=lambda: RedirectResponse(app.url_path_for(get_dice_roll.__name__)), methods=["GET"], include_in_schema=False)

    app.add_api_route(
        path="/dice/roll",
        endpoint=get_dice_roll,
    )

    return app


app = create_app()
