#! /usr/bin/env python3

import string

parser = argparse.ArgumentParser(prog="pcol", description="Use it to print columns from table fed from standard input into standard output"
def pcol():
    d = sys.stdin.readlines()
    if len(sys.argv) > 1:
        for i in range(len(d)):
            e = d[i]
            f = e.split()
            for i in sys.argv:
                if i == sys.argv[0]:
                    continue
                print(f[int(i)-1], end = " ")
            print()

pcol()
