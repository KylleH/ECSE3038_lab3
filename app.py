import uuid
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI, HTTPException,Request,Response,status
app=FastAPI()


tanks=[]

# Create a new dictionary

@app.post("/tank")
async def display (tank:dict,response:Response):
   output=[]
   new_uuid = str(uuid.uuid4())

   tank["id"] = new_uuid
   tank["location"]
   tank["lat"]
   tank["lat"]
   tanks.append(tank)
   output.append(tank)
   response.status_code = 201  # Set status code to 201 Created
   return output
   

@app.get("/tank")
async def show_data():
   return tanks

# Define a function to find a tank by its id
def find_tank_by_id(id):
    for tank in tanks:
        if tank["id"] == id:
            return tank
    return None

# Endpoint to retrieve data for a specific tank by its id
@app.get("/tank/{id}")
async def show_tank(id: str):
    tank = find_tank_by_id(id)
    if tank:
        return tank
    else:
        raise HTTPException(status_code=404, detail="Tank not found")

@app.patch("/tank/{id}")
async def partial_edit(id:str,request:Request,response:Response):
    edit= await request.json()
    for i,tank in enumerate(tanks):
        if tank["id"] == id:
            tanks[i]={**tank, **edit}
            tanks[i]["id"]=id # repastes old id
            response.status_code = 206  # indicates partial change
            return tanks[i]
    raise HTTPException(status_code=404, detail=f"Tank with ID {id} not found")
    
@app.delete("/tank/{id}")
async def delete_T(id: str, response: Response):

    for i in range(len(tanks)):
        if tanks[i]["id"] == id:
            del tanks[i]
            response.status_code = 204  # indicatre
            return()
    
    raise HTTPException(status_code=404, detail="Item not found")    

import uvicorn
uvicorn.run(app, host="127.0.0.1", port=8000)