import numpy as np
from matplotlib import pyplot as plt
import random


def main():
    N = 100
    numOfSuccess = 10
    for i in range(0,11):
        p = float(i)/10
        dist = dict();
        for t in range(0,N):
            dist[t]=sum([1 if random.random() < p else 0 for _ in range(0,numOfSuccess)]);
        plt.plot(dist.keys(),dist.values(),label=('p='+str(p)),marker='<' if p<0.3 else 'o',linestyle='None')
    plt.legend(loc='upper right')
    plt.show()



if __name__ == '__main__':main()