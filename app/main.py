from fastapi import FastAPI # used to build the api
from pydantic import BaseModel # for schema validation
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import base64
import json
import os
import boto3 

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class RunSchema(BaseModel):
    language: str
    code: str

class TestSchema(BaseModel):
    language: str
    code: str
    question_id: str

@app.get('/')
def index():
    return {'Ready' : 'to run'}

@app.post('/run')
def serve_result(query_run: RunSchema):

    if query_run.language.lower() == 'python':
        decoded = base64.b64decode(query_run.code)
        decoded = decoded.decode('utf-8')
        stdout, stderr, exit_code = python_script_run.run(decoded)
        result = json.dumps({
                            'language':query_run.language.lower(), 
                            'stdout':stdout, 'stderr':stderr, 
                            'exit_code':exit_code
                            })
        result = str(result)
        result = result.encode('utf-8')
        result = base64.b64encode(result)
    if query_run.language.lower() == 'sql':
        pass # execute the sql query

    return result

@app.post('/test')
def serve_test(query_test: TestSchema):

    if query_test.language.lower() == 'python':
        decoded = base64.b64decode(query_test.code)
        decoded = decoded.decode('utf-8')
        _stdout, _stderr, _exit_code = python_script_test.test(query_test.language.lower(), decoded, query_test.question_id)
        result = json.dumps({
                        'language':query_test.language.lower(), 
                        'stdout':_stdout, 'stderr':_stderr, 
                        'exit_code':_exit_code
                        })
        result = str(result)
        result = result.encode('utf-8')
        result = base64.b64encode(result)
    if query_test.language.lower() == 'sql':
        pass # test the sql query

    return result
