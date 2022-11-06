import falcon.asgi

from .config import Config
from .images import Images, Thumbnails
from .store import Store
from .hub import Events, Hub
from .chat import Chat



def create_app(config=None):
    config = config or Config()
    hub = Hub()
    store = Store(config, hub)
    images = Images(config, store)
    thumbnails = Thumbnails(store)
    # cors = CORS(allow_all_origins=True, allow_all_headers=True)
    app = falcon.asgi.App(middleware=falcon.CORSMiddleware(
    allow_origins='http://127.0.0.1:8000'))
    app.add_route('/images', images)
    app.add_route('/images/{image_id:uuid}.jpeg', images, suffix='image')
    app.add_route('/thumbnails/{image_id:uuid}/{width:int}x{height:int}.jpeg', thumbnails)
    app.add_route('/ws/{name}', Chat(hub))
    app.add_route('/sse', Events(hub))

    return app