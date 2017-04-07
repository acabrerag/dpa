#!/usr/bin/env python

def fibonacci(x):
  a,b = 0,1
  while True:
    yield a
    a, b = b, a + b


if __name__ == "__main__":
  import sys
  x = int(sys.argv[1]) # Hay maneras mas elegantes
  print(fibonacci(x))
