def toResponse(result):
    return {"income": result[1], "path":[c["name"] for c in result[0]]}

def toContracts(contractList):
    return [c.__dict__ for c in contractList.__root__]