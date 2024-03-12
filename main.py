from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html, AnyComponent
from fastui import components as c

app = FastAPI()


@app.get("/api", response_model=FastUI, response_model_exclude_none=True)
async def api() -> list[AnyComponent]:
    return [c.Div(components=[c.Text(text="Halo Tiktok")])]


@app.get("/")
async def hendra_application() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title="Hendra Application"))
