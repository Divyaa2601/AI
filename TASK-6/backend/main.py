# main.py
import os
import shutil
import uuid
from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from model_utils import predict_image

app = FastAPI(title="Animal Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TEMP_DIR = os.path.join(os.path.dirname(__file__), "temp")
os.makedirs(TEMP_DIR, exist_ok=True)

ALLOWED_MODELS = ["knn", "logreg", "random_forest", "svm"]

@app.post("/classify")
async def classify(file: UploadFile, model: str = Form(...)):
    model = model.lower()
    if model not in ALLOWED_MODELS:
        raise HTTPException(status_code=400, detail=f"Unknown model '{model}'. Allowed: {sorted(ALLOWED_MODELS)}")

    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")

    # create a unique temp filename to avoid collisions
    ext = os.path.splitext(file.filename)[1] or ".jpg"
    tmp_name = f"{uuid.uuid4().hex}{ext}"
    tmp_path = os.path.join(TEMP_DIR, tmp_name)

    try:
        with open(tmp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # call prediction util
        pred = predict_image(tmp_path, model)
        return JSONResponse({"prediction": pred})
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        # for debugging you can log e
        raise HTTPException(status_code=500, detail="Prediction failed")
    finally:
        # cleanup
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass
