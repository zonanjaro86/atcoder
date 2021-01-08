import itertools
from collections import Counter

# def main(s):
#     if len(s) < 3:
#         if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
#             print('Yes')
#         else:
#             print('No')
#         return

#     for i in range(112, 1000, 8):
#         for a in itertools.permutations(str(i)):
#             if ''.join(a) in s:
#                 print('Yes')
#                 return
#     print('No')

def main(s):
    if len(s) < 3:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print('Yes')
        else:
            print('No')
        return

    cnt = Counter(s)

    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:
            print('Yes')
            return

    print('No')

if __name__ == '__main__':
    s = input()
    main(s)