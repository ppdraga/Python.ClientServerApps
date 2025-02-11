import zlib
from functools import wraps

def compression_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        b_request = zlib.decompress(request)
        b_response = func(b_request, *args, **kwargs)
        return zlib.compress(b_response)
    return wrapper

def encryption_middleware(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # decryption  text
        b_response = func(request, *args, **kwargs)
        # enctipion text
        return b_response
    return wrapper
