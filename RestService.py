from radon.metrics import mi_visit
from radon.complexity import cc_visit, cc_rank
from radon.cli.tools import iter_filenames
from distributed import Client, LocalCluster
import dask.bag as db
from time import time
from multiprocessing import Pool


# computes the cyclomatic complexity of the given code using Radon
def compute_complexity(source):
   # get cc blocks
   blocks = cc_visit(source)
   # get MI score
   mi = mi_visit(source, True)

   #for func in blocks:
   #    print(func.name, "- CC Rank:", cc_rank(func.complexity))

def main():
    sources = []
    for filename in iter_filenames(['.']):
        if filename.endswith(".py"):
            with open(filename) as fobj:
                sources.append(fobj.read())

    steps = [1,2,3,4,5,6]
    times = []
    for i in steps:
        pool = Pool(processes=i)

        cluster = LocalCluster(scheduler_port=8786+i, n_workers=i)
        # print(cluster)

        string = str(8786+i)
        client = Client('127.0.0.1:'+ string)
        #print(client)

        start_time = time()

        #pool.map(compute_complexity, sources)
        bag = db.from_sequence(sources)

        futures = client.map(compute_complexity, sources)
        #futures = db.map(compute_complexity, bag)

        #results = client.gather(futures)
        #print(results)

        end_time = time() - start_time
        times.append(end_time)
    print(times)

if __name__ == '__main__':
    main()

