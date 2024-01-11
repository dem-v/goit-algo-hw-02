from collections import deque
import re


def check_symmetry():
    global q
    while len(q) > 1:
        if q.pop() != q.popleft():
            print("Це не паліндром")
            return
    if len(q) < 2:
        print("Це паліндром :)")


q = deque(re.sub("([^\wА-яіїё])", "", input("Введіть рядок: ")))

check_symmetry()
