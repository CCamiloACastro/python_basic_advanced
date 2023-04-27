from fastapi import FastAPI

# Fast api de manera integrada ofrece un server
# uvicorn fichero:instancia --reload -> uvicorn main:app --reload

# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

app = FastAPI()


@app.get("/")  # Esto ya es fastapi
# Siempre que se llame desde un servidor se coloca una función asíncrona
async def root():
    return {"message": "Hola bb que mas pues!!!"}


@app.get("/url")
async def url():
    return {"url_git": "https://github.com/CCamiloACastro"}
