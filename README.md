#list out the the function call stack ex. fib(5) -> fib(4) -> fib(3) ?

fib(5)-> fib(4)-> fib(3)-> fib(2)->fib(1)-> fib(0)= fib(1)-> fib(0)
fib(2)-> fib(1)-> fib(0)-> fib(0)-> fib(3)-> fib(2)-> fib(1)-> fib(0) fib(1)-> fib(0)-> fib(1)

#Prove the time complexity of the algorithms.

.Each call to fib(n) in the original Fibonacci implementation generates two further recursive calls, resulting in a branching tree 
 structure. There are two child nodes at each level of the recursion, which stand in for the two recursive calls made at that level. The 
 structure resembles a binary tree and causes an exponential increase in function calls.
.Each level's function calls follow a power of two pattern. At level n, there are precisely 2^n function calls. As a result, the recursive 
 tree's total function calls are proportional to 2^n.
.The algorithm's time complexity, expressed in big-O notation, is O(2^n), meaning that it increases exponentially with the amount of the 
 input. For higher values of, this exponential increase results in inefficiency.

 #Comment on way's you could improve your implementation.

.Because of its exponential time complexity, the original Fibonacci implementation's main drawback is that it becomes inefficient for bigger 
 values of n. This implementation has a fast growing number of recursive calls, which causes a branching tree structure and unnecessary 
 computations.
.Optimization strategies like memoization or dynamic programming can be used to overcome this inefficiency. To prevent unnecessary 
 computations, these methods store and reuse previously computed results. Memorization, as used to Fibonacci, usually involves storing 
 intermediate results in a data structure, like an array or dictionary. This minimizes the requirement to recalculate Fibonacci values for 
 the same inputs.
.The algorithm's efficiency can be greatly increased by memorization and dynamic programming, which can reduce the time complexity to O(n) 
 by removing
