class AppValidationError(Exception):
    def __init__(self, msg, response=None):
        super(AppValidationError, self).__init__(msg)
        self.response = response
