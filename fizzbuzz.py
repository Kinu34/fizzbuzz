# add your code here

def fizzbuzz(n):
    for i in range(1, n + 1):
       
        if i % 3 == 0 and i % 5 == 0: # If the number is divisible by both 3 and 5, print FizzBuzz
            
            print("FizzBuzz")
       
        elif i % 3 == 0: #If the number is only divisible by 3, print Fizz
            
            print("Fizz")
       
        elif i % 5 == 0: #If the number is only divisible by 5, print Buzz.
           
            print("Buzz")
        else:#  If the number is not divisible by 3 or 5, print the number itself.
            print(i)

# Example usage
if __name__ == "__main__":
    fizzbuzz(100)

