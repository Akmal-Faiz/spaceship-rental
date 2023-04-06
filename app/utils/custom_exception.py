class NoValidResultException(Exception):
    def __init__(self, message: str):
        self.message = message
        
class DuplicateNameError(Exception):
    def __init__(self, message: str):
        self.message = message