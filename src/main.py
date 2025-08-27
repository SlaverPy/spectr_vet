from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="VetClinic API")

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>VetClinic</title>
        </head>
        <body>
            <h1>Добро пожаловать в Ветклинику 🐾</h1>
            <p>Скоро здесь будет сайт...</p>
        </body>
    </html>
    """