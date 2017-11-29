from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
from radon.metrics import mi_visit
from radon.complexity import cc_visit, cc_rank
from time import time
from pygit2 import Repository, clone_repository, Index

app = Flask(__name__)

def compute_complexity(source):
    # get cc blocks
    blocks = cc_visit(source)
    # get MI score
    mi = mi_visit(source, True)

    for func in blocks:
        print(func.name, "- CC Rank:", cc_rank(func.complexity))

def set_repo():
    try:
        repo = Repository('./repo')
    except:
        repo_url = 'https://github.com/rubik/radon.git'
        repo_path = './repo'
        repo = clone_repository(repo_url, repo_path)
    return repo

def get_data(tree, repo):
    sources = []
    for entry in tree:
        if ".py" in entry.name:
            sources.append(entry)
        if "." not in entry.name:
           if entry.type == 'tree':
                new_tree = repo.get(entry.id)
                sources += (get_data(new_tree, repo))
    return sources

@app.route('/')
def welcome():
    repo = set_repo()
    commit = repo.revparse_single('HEAD').id
    #print(commit)
    commit_obj = repo.get("d473be0c3807ee546e90196b2215fa55ca827f5d")
    tree = commit_obj.tree

    sources = get_data(tree, repo)
    files = []
    for source in sources:
        files.append(repo[source.id].data.decode("utf-8"))

    for file in files:
        compute_complexity(file)

    return 'Welcome'

if __name__ == '__main__':
    app.run(debug=True)