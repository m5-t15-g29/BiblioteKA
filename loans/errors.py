class LoanBlockedError(Exception):
    def __init__(self, message):
        self.message = message

class CopiesInsusicient(Exception):
    def __init__(self, message, status):
        self.message = message
        self.status = status
