from fastapi import FastAPI,Depends,Header, HTTPException

app=FastAPI()


def verify_token(token:str=Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(status_code=401,detail="Unauthorized")
    
    return {
        "user":"Authorized user"
    }

@app.get("/secure-data")
def get_secure_data(user=Depends(verify_token)):
    return{
        "message":"This is secure data that you accessed",
        "user": user
    }

# def common_logic():
#     return "this is common logic executed"

# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return{
#         "message":"this is home page",
#         "Data":data
#     }

def get_current_user():
    return {
        "user":"mohit"
    }

@app.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return user


@app.get("/dashboard")
def get_dashboard(user=Depends(get_current_user)):
    return user 