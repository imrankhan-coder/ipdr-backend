from fastapi import Depends

def get_current_user():
    return {"user": "admin"}
