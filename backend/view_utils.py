from uuid import UUID

def error(msg:str, code=400) -> (dict, int):
    '''Error Logging'''
    headers = {}
    if code == 401:
        headers["WWW-Authenticate"] = "Digest"
    if type(msg) != str:
        msg = str(msg)
    print(msg)
    return {"error": msg}, code, headers

def to_uuid(id) -> UUID:
    if type(id) != UUID:
        try:
            return UUID(id)
        except:
            raise AttributeError("Invalid UUID")
    else:
        return id