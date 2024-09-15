#list out the the function call stack ex. fib(5) -> fib(4) -> fib(3) ?

fib(5)-> fib(4)-> fib(3)-> fib(2)->fib(1)-> fib(0)= fib(1)-> fib(0)
fib(2)-> fib(1)-> fib(0)-> fib(0)-> fib(3)-> fib(2)-> fib(1)-> fib(0) fib(1)-> fib(0)-> fib(1)

#Prove the time complexity of the algorithms.

Answer:
.The major drawback of the original Fibonacci method is that it turns inefficient for larger values of n owing to its exponential time complexity. This approach employs an increasing 
 amount of recursive calls, leading to needless computations and a branching tree structure.

.To get around this inefficiency, optimization techniques like memoization and programming with variables might be applied. These methods store and reuse computed results earlier to 
 avoid doing needless computations. While memorizing Fibonacci, the intermediate results usually remain in a data structure such as an array or a dictionary. By doing this, the need to 
 recalculate Fibonacci values for the same inputs is reduced.

.Memorizing and flexible programming can significantly boost the algorithm's performance and lower the time complexity to O(n) by eliminating
