from radon.metrics import mi_visit
from radon.complexity import cc_visit, cc_rank
from radon.cli.tools import iter_filenames
from distributed import Client, LocalCluster
from time import time


# computes the cyclomatic complexity of the given code using Radon
def compute_complexity(source):
   # get cc blocks
   blocks = cc_visit(source)
   # get MI score
   mi = mi_visit(source, True)

   for func in blocks:
       print(func.name, "- CC Rank:", cc_rank(func.complexity))

def main():
    sources = []
    for filename in iter_filenames(['.']):
        with open(filename) as fobj:
            sources.append(fobj.read())

    start_time = time()

    cluster = LocalCluster(scheduler_port=8786, n_workers=4)
    print(cluster)

    client = Client('127.0.0.1:8786')
    print(client)
    L = client.submit(compute_complexity, sources)
    #print(total)
    #total.result()

    end_time = time() - start_time
    print(end_time, 'sec')

if __name__ == '__main__':
    main()

