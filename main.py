import uuid
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from supabase_client import supabase

app = FastAPI()

class ItemCreate(BaseModel):
    eventId: str
    name: str
    description: str
    imageUrl: Optional[str] = None

@app.post("/items")
def create_item(item: ItemCreate):
    item_id = str(uuid.uuid4())

    data = {
        "eventId": item.eventId, 
        "name": item.name,
        "description": item.description,
        "imageUrl": item.imageUrl or "" 
    }

    try:
        print("Verzonden data naar Supabase:", data)

        response = supabase.table("items").insert(data).execute()
        print("Supabase response:", response)

        if hasattr(response, 'error') and response.error:
            print("Supabase error details:", response.error)
            raise Exception(f"Supabase insert mislukt. Error: {response.error}")

    except Exception as e:
        print("Fout bij Supabase-insert:", str(e))
        raise HTTPException(status_code=500, detail=f"Supabase error: {str(e)}")

    return {
        "message": "Item created successfully",
        "item": data
    }

@app.get("/items")
def get_items():
    try:
        response = supabase.table("item").select("*").execute()
        print("Supabase GET response:", response)

        if response.status_code != 200:
            print("Supabase GET error details:", response.data)
            raise Exception(f"Supabase GET mislukt. Status: {response.status_code}, data: {response.data}")

        items = response.data
    except Exception as e:
        print("Fout bij ophalen uit Supabase:", str(e))
        raise HTTPException(status_code=500, detail=f"Supabase error: {str(e)}")

    return {"items": items}

@app.get("/events")
def get_events():
    """Fetch all events from Supabase"""
    try:
        response = supabase.table("events").select("id, name").execute()
        
        if hasattr(response, 'error') and response.error:
            raise Exception(f"Supabase query failed: {response.error}")
        
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch events: {str(e)}")
