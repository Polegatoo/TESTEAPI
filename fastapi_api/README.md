# FastAPI - Azure App Service

## Rodar local
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```
Abra http://localhost:8000/docs

## Deploy no Azure
Este repo já contém o workflow do GitHub Actions. Crie o secret `AZUREAPPSERVICE_PUBLISHPROFILE` com o Publish Profile do seu App Service.

No App Service, em Startup Command, use:
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```
