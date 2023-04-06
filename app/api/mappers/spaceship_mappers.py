def toResponse(result):
    return [contract["name"] for contract in result[0]]

def toContracts(contractList):
    return [c.__dict__ for c in contractList.__root__]