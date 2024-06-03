fastAPI:

Run commands:

vEnv start / stop:

To create a new environment:
    python -m venv fastapienv

to start the fast api environment:
     faseapienv/Scripts/activate.bat

then install fastapi and uvicorn:
    pip install "uvicorn[standard]"
    pip install fastapi

deactivate environment:
    "deactivate" to deactivate


to run the api:
    uvicorn books:app --reload     [books is the python file name]



