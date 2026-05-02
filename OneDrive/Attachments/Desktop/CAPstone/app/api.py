from fastapi import FastAPI
from routers import metrics
from routers import aws
print("metrics imported")
app = FastAPI(
    title = "Internal Devops Utilities API",
    description ="this is an internal API Utilities app for monitoring the metrices,AWS usage,log analysis , etc",
    version = "1.0.0",
    doc_url ="/docs",
)
@app.get("/")
def hello():
    return {"message":"hello dosto this is devops "}

print("route added")
print("router included")
app.include_router(metrics.router)
app.include_router(aws.router,prefix="/aws")
