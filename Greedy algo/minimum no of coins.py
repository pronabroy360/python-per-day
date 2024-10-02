if __name__ == "__main__":
    V=49
    ans = []
    coins = [1,2,5,10,20,50,100,500,1000]
    for i in range(len(coins)-1,-1,-1): #started from n-1 to n >=0
        while V >= coins[i]: 
            V-=coins[i]
            ans.append(coins[i])
            
    # while inside for: When you have a finite set of elements but need to perform multiple checks or actions on each one.
    
    for i in range(len(ans)):
        print(ans[i], end=" ")



#Conclusion
# Each loop combination serves different purposes based on the complexity of the task at hand. Here's a summary of when to use which combination:

# for inside for: When iterating over multi-dimensional data or performing cross-product operations.
# while inside while: For handling multi-level dynamic conditions and simulating complex interactions.
# for inside while: When the outer condition is dynamic, but you still need to iterate over a set of data.
# while inside for: When you have a finite set of elements but need to perform multiple checks or actions on each one.
# for/while with break/continue: For selective stopping or skipping iterations based on dynamic conditions.
# for-else and while-else: For handling actions when loops complete without interruption.
# These patterns provide flexibility for different use cases, from simple iterations to complex simulations and dynamic processing.






