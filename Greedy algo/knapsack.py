# class Item:
#     def __init__(self, value, weight):
#         self.value = value
#         self.weight = weight

# class FranctionalKnapsack:  
#     def Solution(self, arr, N, W):
#         arr.sort(key = lambda x: x.value / x.weight, reverse = True)
#         curWeight = 0
#         finalValue = 0.0
#         for i in range(N):
#             if curWeight + arr[i].weight <= W:
#                 curWeight += arr[i].weight
#                 finalValue += arr[i].value
            
#             else:
#                 remain = W - curWeight
#                 finalValue += arr[i].value / arr[i].weight * remain
#                 break
        
#         return finalValue
    
# if __name__ == "__main__":
#     arr = [Item(60,10), Item(100,20), Item(120,30)]
#     obj = FranctionalKnapsack()
#     ans = obj.Solution(arr, 3, 50)
#     print(ans)

#######################2nd try####################
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
    
class Knapsack:
    def Solution(self,arr, N, W):
        arr.sort(key = lambda x: x.value / x.weight, reverse = True )
        weightCal=0
        profitCal=0.0
        remWeight = 0 # ei change ta ami ansi :)
        for i in range(N):

            if remWeight + weightCal <= W:
                weightCal += arr[i].weight
                profitCal += arr[i].value
            else:
                remWeight = W-weightCal
                profitCal += arr[i].value / arr[i].weight * remWeight
                break
        return profitCal

if __name__ == "__main__":
    arr = [Item(60,10), Item(100, 20), Item(120,30)]
    instance = Knapsack()
    ans = instance.Solution(arr, 3, 50)
    print(ans)
