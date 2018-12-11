from . import index


@index.route('/')
def index_view():
    return 'index_view'