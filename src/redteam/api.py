from fastapi import FastAPI
import uvicorn
from main import run_campaign

app = FastAPI()

@app.get("/run")
def run():
    """
    Endpoint pour déclencher la campagne CrewAI.
    """
    result = run_campaign()
    return {"result": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
