from fastapi import Request


def get_main_db(request: Request):
    return request.state.db