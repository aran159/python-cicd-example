from fastapi import FastAPI
from app.application.get_dice_roll import get_dice_roll
from fastapi.responses import RedirectResponse


def create_app() -> FastAPI:
    my_unused_variable = 1

    app = FastAPI()

    app.add_api_route(
        path="/",
        endpoint=lambda: RedirectResponse(app.url_path_for(get_dice_roll.__name__)),
        methods=["GET"],
        include_in_schema=False,
    )

    app.add_api_route(path="/dice/roll", endpoint=get_dice_roll)

    return app


app = create_app()
