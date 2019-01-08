from .error_middleware import error_middleware


def setup_middlewares(app):
    app.middlewares.append(error_middleware)


