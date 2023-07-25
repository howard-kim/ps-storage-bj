while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except EOFError:
        break

'''
while True:
    try:
        a, b = map(int, sys.stdin.readline().rsplit())
        sys.stdout.write("{:d}\n".format(a+b))
    except EOFError:
        break
'''

"""
    if not sys.stdin.readline(): 
        break
    sys.stdin.seek(sys.stdin.tell()-sys.stdin.readline())
"""