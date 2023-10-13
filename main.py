from fastapi import FastAPI
import wikipedia
from pydantic import BaseModel

wikipedia.set_lang("ru") #Язык Русский

app = FastAPI()

@app.get("/")
def wk():
    return (wikipedia.page("Your request").content)

@app.get("/{search}")
def searchwiki(search: str):
    return "Википедия говорит:" + (wikipedia.page({search}).content)


@app.get("/wk/{search}")
def wk_search_query(search: str, how_much_request: int):
    result = ""
    for i in range(how_much_request):
        result += f"В википедии про " + search + " говорится: " + (wikipedia.page({search}).content)
    return result

class Search(BaseModel):
    search: str
    result: str

class SearchInput(BaseModel):
    search: str

@app.post("/")
def create_search(search_input: SearchInput):
    return " Про " + search_input.search + " В википедии говорится: " + (wikipedia.page(search_input).content)



