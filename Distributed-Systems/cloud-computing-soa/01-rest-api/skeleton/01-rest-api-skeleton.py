from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

shared_dict = {}

class Item(BaseModel):
    value: Optional[str] = None

class Item2(BaseModel):
    url: str

@app.get("/", status_code=200)
def read_root():
    # Return all keys from the shared dictionary
    return {"keys": list(shared_dict.keys())}

@app.get("/{id}", status_code=301)
def read_item(id: str):
    value = shared_dict.get(id)
    
    if value is not None:
        return {"value": value}
    else:
        raise HTTPException(status_code=404, detail="Key not found in shared dictionary")

@app.delete("/", status_code=404)
def delete_root():
    # Empty the shared dictionary
    shared_dict.clear()
    return {"detail": "Shared dictionary has been emptied"}

@app.delete("/{id}", status_code=204)
def delete_item(id: str):
    # Remove the record with key 'id' from the shared dictionary
    if id in shared_dict:
        del shared_dict[id]
        return {"detail": f"Record with key '{id}' has been deleted"}
    else:
        raise HTTPException(status_code=404, detail="Key not found in shared dictionary")

def is_it_an_url(string):
    return string.startswith("http://") or string.startswith("https://")

@app.post("/", status_code=201)
def create_root(item: Item):
    # Check if the request body is empty
    if not item.value:
        raise HTTPException(status_code=400, detail="Content of body was empty")
    # Add the value from the request body to the shared dictionary with a numeric key
    key = len(shared_dict) + 1
    shared_dict[str(key)+"a"] = item.value
    return {"id": str(key)+"a"}

@app.put("/{id}", status_code=200)
def update_item(id: str, item: Item2):
    if id not in shared_dict:
        raise HTTPException(status_code=404, detail="id doesnt exists")
    if is_it_an_url(str(item.url)) is False:
        raise HTTPException(status_code=400, detail="Update failed, invalid url")  
    shared_dict[id] = str(item.url)
    return {"message": "Item updated successfully"}