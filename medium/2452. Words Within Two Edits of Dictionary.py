class Solution:
    def twoEditWords(self, queries, dictionary):
        result = []

        for query in queries:
            for word in dictionary:
                differences = 0

                for i in range(len(query)):
                    if query[i] != word[i]:
                        differences += 1
                        if differences > 2:
                            break

                if differences <= 2:
                    result.append(query)
                    break

        return result