from fastapi import FastAPI, HTTPException
app=FastAPI()

data=[]

@app.post("/person")
async def add_person(result: dict):
    if result["name"] and result["occupation"] and result[ "address"]:
        data.append(result)
        return {"sucess": True,"result":result} 
            
            
    else:
        result={"error_message":"invalid request"}
        return {"sucess": False,"result":result} 

@app.get("/person")
async def get_data():
    output=[]
    for person in data:
        formatted_person = {
            "name": person["name"],
            "occupation": person["occupation"],
            "address": person["address"]
        }
        output.append(formatted_person)
    return output

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)