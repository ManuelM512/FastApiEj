from fastapi import FastAPI
from models import Links
import reach_service

app = FastAPI()


@app.post("/reach")
async def reacher(links: Links):
    from_link = links.from_link
    to_link = links.to_link
    wikipedia = "https://es.wikipedia.org"
    if from_link[:24] == wikipedia and to_link[:24] == wikipedia:
        return reach_service.reach(from_link[24:], to_link[24:])
    else:
        return reach_service.reach(wikipedia + from_link, wikipedia + to_link)
