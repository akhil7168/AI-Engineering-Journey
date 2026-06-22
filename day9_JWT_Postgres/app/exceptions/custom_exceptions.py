class UserAlreadyExistsException(Exception):
    pass


class UserNotFoundException(Exception):
    pass


class InvalidCredentialsException(Exception):
    pass


class InvalidTokenException(Exception):
    pass


class NoteNotFoundException(Exception):
    pass