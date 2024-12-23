from utils.solutionBase import SolutionBase
from functools import cache

class solution(SolutionBase):
    data = [int(line.strip()) for line in open("day22/input.txt").readlines()]

    @cache
    def secret_number(self, n):
        n = (n ^ (n * 64)) % 16777216
        n = (n ^ (n // 32)) % 16777216
        n = (n ^ (n * 2048)) % 16777216

        return n

    def p1(self):
        buyers = []
        for number in self.data:
            secret = number
            for _ in range(2000):
                secret = self.secret_number(secret)
            buyers.append(secret)

        return sum(buyers)

    def p2(self):
        prices_to_total = {}

        for line in self.data:
            num = line
            buyer = [num % 10]
            for _ in range(2000):
                num = self.secret_number(num)
                buyer.append(num % 10)
            seen = set()
            for i in range(len(buyer) - 4):
                a, b, c, d, e = buyer[i:i+5]
                seq = (b - a, c - b, d - c, e - d)
                if seq in seen: continue
                seen.add(seq)
                if seq not in prices_to_total: prices_to_total[seq] = 0
                prices_to_total[seq] += e

        return max(prices_to_total.values())
    