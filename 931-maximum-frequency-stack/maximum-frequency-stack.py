from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)        # value -> frequency
        self.group = defaultdict(list)      # frequency -> stack of values
        self.maxfreq = 0

    def push(self, val: int) -> None:
        # 1️⃣ Increase frequency count
        f = self.freq[val] + 1
        self.freq[val] = f

        # 2️⃣ Add to corresponding group stack
        self.group[f].append(val)

        # 3️⃣ Update max frequency
        if f > self.maxfreq:
            self.maxfreq = f

    def pop(self) -> int:
        # 1️⃣ Pop from the most frequent group
        val = self.group[self.maxfreq].pop()

        # 2️⃣ Decrease frequency count
        self.freq[val] -= 1

        # 3️⃣ If that group is empty, reduce maxfreq
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val
