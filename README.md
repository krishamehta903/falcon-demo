# falcon-demo

## Requirements

* Python 3.9

## Getting Started

### Virtual Environment

1. Install the `virtualenv` package if you haven't already:
    ```
    pip3 install virtualenv
    ```
2. Create a virtual environment:
    ```
    python3.9 -m virtualenv .venv
    ```
3. Activate your virtual environment:
    ```
    source .venv/bin/activate
    ```
4. Install requirements:
    ```
    pip install -r requirements.txt
    ```
### Start Server + Websocket/SSE Demo

1. Run the following command to start the server:
    ```
    uvicorn server.asgi:app
    ```
2. Possible routes to run (via httpie, Postman, etc.):
    ```
    | HTTP METHOD | URI                                                                 | ACTION                            |
    |-------------|---------------------------------------------------------------------|-----------------------------------|
    | GET         | http://localhost:8000/images                                        | Gets all images                   |
    | GET         | http://localhost:8000/images/<image_id>                             | Gets one image                    |
    | POST        | http://localhost:8000/images @<path_to_image_file>                  | Uploads a new image               |
    | GET         | http://localhost:8000/thumbnails/<image_id>/<width>x<height>.jpeg   | Get available thumbnail for image |
    ```
    Notes: 
    1. for the GET for thumbnails, can use one of the returned thumbnail paths for an image
    2. can use test image file in repo to test upload image POST
        ```
        localhost:8000/images @~/falcon-demo/test.png
        ```
3. Open ./static/index.html in browser to see Websockets and Server Sent Events demo
    TODO: add more detail



When you are finished working in your virtual environment, use the `deactivate` command.