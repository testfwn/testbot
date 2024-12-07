from aiohttp import web
import os

routes = web.RouteTableDef()


# Route to check the service status
@routes.get("/", allow_head=True)
async def root_route_handler(_):
    response = {"status": "running v1.0.0"}
    return web.json_response(response)


# Application setup
async def web_server():
    app = web.Application()
    app.add_routes(routes)
    return app
