from typing import List

class Solution:
    def invalidTransactions(self, 
                            transactions: List[str]
                            ) -> List[str]:
        track = {}
        invalid = []
       
        for i, trans in enumerate(transactions):
            parts = trans.split(',')
            name = parts[0]
            time = int(parts[1])
            amount = int(parts[2])
            city = parts[3]

            if name not in track:
                track[name] = [(time, amount, city, i)]
            else:
                track[name].append((time, amount, city, i))
      
            #redundant comparions : if a>b, c>a => c>b
            for j, (t, a, c, index) in enumerate(track[name]):
                if (abs(time - t) <= 60) and (c != city):
                    invalid.append(index)
                    invalid.append(i)

            if int(amount) > 1000:
                invalid.append(i)

        #???
        #above is comparing all the values
        #we can reduce the pairwise comparison if we know
        #a <b, b< c => a<c, we do not need to compared
        #sorting is a way to reduce comparison

        invalid = list(set(invalid))

        return [transactions[k] for k in invalid]


transactions = [
    "alice,20,800,mtv",
    "alice,50,100,mtv",
    "alice,51,100,frankfurt"
    ]
obj = Solution()
print(obj.invalidTransactions(transactions))

#Cases for invalid: amount > 1000, occurs with 60 of another 
#transaction with same name in a different city
#Things to consider