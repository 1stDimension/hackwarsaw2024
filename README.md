# Project LocalHub

## Who is a target of project

LocalHub is dedicated for local communities who want to participate in local live. 
Residents can online vot for bills prepared by managers. Residents have access for read any bill
community from archive. Project give possibility for onsite voting when some residents 
do not have access to internet. 

## Run project

Run project by:

Create virtual environment:

```shell
python3 -m venv ~/.venv/hackwarsaw2024
```

Load your environment variables

```shell
. ~/.venv/hackwarsaw2024/bin/activate
```

Install dependencies:

```shell
pip install --editable .
```

Go to client directory and build npm application

```shell
npm run build
```

Run FastAPI server

```shell
fastapi dev src/localhub/main.py
```
