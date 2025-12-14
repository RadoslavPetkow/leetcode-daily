class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7

        total_seats = corridor.count('S')
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        ways = 1
        seats_seen = 0
        plants_between = 0
        waiting_for_next_pair = False

        for ch in corridor:
            if ch == 'S':
                seats_seen += 1

                if seats_seen % 2 == 0:
                    waiting_for_next_pair = True
                    plants_between = 0
                else:
                    if waiting_for_next_pair:
                        ways = (ways * (plants_between + 1)) % MOD
                        waiting_for_next_pair = False

            else:
                if waiting_for_next_pair:
                    plants_between += 1

        return ways