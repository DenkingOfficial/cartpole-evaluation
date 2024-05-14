import fastapi as _fastapi
import src.contest as _contest


app = _fastapi.FastAPI()


@app.post("/api/submit")
async def get_score(submission: _fastapi.UploadFile = _fastapi.File(...)):
    submission_bytes = await submission.read()
    return {"score": _contest.check_submission(submission_bytes)}
