from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
from radon.metrics import mi_visit
from radon.complexity import cc_visit, cc_rank
from time import time
from pygit2 import Repository, clone_repository

app = Flask(__name__)

def set_repo():
    try:
        repo = Repository('./repo')
    except:
        repo_url = 'https://github.com/rubik/radon.git'
        repo_path = './repo'
        repo = clone_repository(repo_url, repo_path)
    return repo

@app.route('/')
def welcome():
    return 'Welcome'

if __name__ == '__main__':
    app.run(debug=True)