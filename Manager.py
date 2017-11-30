from flask import Flask, request, jsonify
from time import time
from pygit2 import Repository, clone_repository
import requests

app = Flask(__name__)

global next_task

def set_repo():
    try:
        repo = Repository('./repo')
    except:
        repo_url = 'https://github.com/rubik/radon.git'
        repo_path = './repo'
        repo = clone_repository(repo_url, repo_path)
    return repo

def get_commits(repo):
    commits = []
    for commit in repo.walk(repo.head.target):
        commits.append(repo.get(commit.id))
    return commits


@app.route('/work' , methods=['GET'])
def give_work():
    repo = set_repo()
    commits = get_commits(repo)

    global next_task

    try:
        commit_hash = commits[next_task]
        next_task += 1
        if commit_hash != None:
            return jsonify({'commit': str(commit_hash.id), 'id': next_task})
        else:
            return None
    except:
        return None

@app.route('/results', methods=['POST'])
def store_result():
    result = requests.get('http://127.0.0.1:5000/results', params={'key': 'value'})
    print(result.text)
    return result.text

if __name__ == '__main__':
    next_task = 0
    app.run(threaded=True, debug=True)