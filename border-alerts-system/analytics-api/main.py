import  json
from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI()


@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    raw = await file.read()
    try:
        orders: list = json.loads(raw)
    except json.JSONDecodeError:
        raise HTTPException(400, "Invalid JSON file")
    return raw


@app.get(" /analytics/alerts-by-border-and-priority")
async def get_priority():
    pass


@app.get("/analytics/top-urgent-zones")
async def get_priority():
    pass


@app.get("/analytics/distance-distribution")
async def get_priority():
    pass


@app.get("/analytics/low-visibility-high-activity")
async def get_priority():
    pass
@app.get(" /analytics/hot-zones")
async def get_priority():
    pass


@app.get("/health")
async def health():
    return {"status": "ok", "service": "api"}
