# starter-fastapi

## Features

- ⚡️ [FastAPI](https://fastapi.tiangolo.com/), [Starlette](https://www.starlette.io/), [Uvicorn](https://www.uvicorn.org/), [Pydantic](https://pydantic-docs.helpmanual.io/) - born with fastness

- 📦 [Poetry](https://python-poetry.org/) - manage your dependencies

- 🛡 [Flake8](https://flake8.pycqa.org/en/latest/) - linting

- 🐳 [Docker](https://www.docker.com/) - containerize your app

- 🚀 [Gunicorn](https://gunicorn.org/) - production-ready server

- 📝 [Swagger](https://swagger.io/) - API documentation

- 📦 [Celery](https://docs.celeryproject.org/en/stable/) - asynchronous task queue

## Usage

### Development

```bash
# install dependencies
poetry install

# run server
poetry run uvicorn app.main:app --reload
```

### Production

```bash
# build docker image
docker build -t starter-fastapi .

# run docker container
docker run -d -p 8000:8000 starter-fastapi
```

## License

[MIT](LICENSE)

