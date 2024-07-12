from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Подключение статики
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_file_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
    with open(html_file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return HTMLResponse(content=content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
