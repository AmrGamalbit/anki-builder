from fastapi import Request


def get_api_keys(request: Request) -> dict:
    return request.session
