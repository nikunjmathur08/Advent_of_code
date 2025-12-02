from sys import argv
from collections import defaultdict

with open(argv[1]) as f:
    initials = [int(l) for l in f]

if len(argv) <= 2 or argv[2] == "1":
    sum = 0
    for n in initials:
        for i in range(2000):
            n = (n^(n<<6))%16777216
            n = (n^(n>>5))%16777216
            n = (n^(n<<11))%16777216
        sum+=n
    print(f"sum = {sum}")

elif argv[2] == "2":
    total = defaultdict(int)
    for n in initials:
        seqs = dict()
        seq = (0,0,0,0)
        for i in range(2000):
            prev = n%10
            n = (n^(n<<6))%16777216
            n = (n^(n>>5))%16777216
            n = (n^(n<<11))%16777216
            seq = (*seq[1:],n%10-prev)
            if i >= 3 and seq not in seqs:
                seqs[seq] = n%10
        for s in seqs:
            total[s] += seqs[s]
    winner = sorted([(v,k) for k,v in total.items()])[-1]
    print(f"Max profit: {winner[0]} with sequence {winner[1]}")
