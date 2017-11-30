from radon.metrics import mi_visit
from radon.complexity import cc_visit, cc_rank
from pygit2 import Repository, clone_repository
import requests, json

def set_repo():
    try:
        repo = Repository('./repo')
    except:
        repo_url = 'https://github.com/rubik/radon.git'
        repo_path = './repo'
        repo = clone_repository(repo_url, repo_path)
    return repo

def compute_complexity(source):
    result =[]
    # get cc blocks
    blocks = cc_visit(source)
    # get MI score
    mi = mi_visit(source, True)

    for func in blocks:
        result.append(func.name+"- CC Rank:"+cc_rank(func.complexity))
    return result

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

def extract_files(sources):
    files = []
    for source in sources:
        files.append(repo[source.id].data.decode("utf-8"))
    return files

def get_work(repo):
    response = requests.get('http://127.0.0.1:5000/work', params={'key': 'value'})
    response.encoding = 'utf-8'
    json_file = response.json()
    tree = repo.get(json_file['commit']).tree
    id = json_file['id']
    sources = get_data(tree, repo)
    files = extract_files(sources)
    return files, id

def do_work(work):
    results = []
    for file in work:
        results.append(compute_complexity(file))
    return results

def send_results(result):
    result = {'Result' : result}
    post = requests.post('http://127.0.0.1:5000/results', json=result)

if __name__ == '__main__':
    #bool = True
    #while bool:
        repo = set_repo()
        work, id = get_work(repo)
        print(id)
        if id > 350:
            bool = False
            print("Process Terminated")
        result = do_work(work)
        send_results(result)