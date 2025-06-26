import sys
args = sys.argv[1:]

def  downcase_it (str) :
    x = str.lower()
    return x

if len(args) == 0 :
    print("none")
else :
    for args in sys.argv[1:]:
        print(downcase_it(args))

