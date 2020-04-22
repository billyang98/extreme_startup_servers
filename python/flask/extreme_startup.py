import math
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print q

    def get_nums(s):
        c_idx = q.rindex(':')
        substr = q[c_idx+1:]
        nums = substr.split(",")
        nums = [ int(n) for n in nums]
        return nums
    
    def is_prime(a):    
        return all(a % i for i in range(2,a))

    def is_square(a):
        return int(a**(1./2))**2 == a

    def is_cube(a):
        return int(a**(1./3)) ** 3 == a

    if 'plus' in q:
        words = q.split(" ")
        num1 = int(words[-1])
        num2 = int(words[-3])
        print num1 + num2
        return str(num1 + num2)
    elif 'largest' in q:
        nums = get_nums(q)
        return str(max(nums))
    elif 'primes' in q:
        nums = get_nums(q)
        primes = [n for n in nums if is_prime(n)]
        strs = [str(n) for n in primes]
        return ", ".join(strs)
    elif 'square' in q and 'cube' in q:
        nums = get_nums(q)
        words = [n for n in nums if is_square(n) and is_cube(n)]
        strs = [str(n) for n in words]
        return ", ".join(strs)
    elif 'minus' in q:
        nums = [int(s) for s in q.split() if s.isdigit()]
        return str(nums[0] - nums[1])
    elif 'Fibonacci' in q:
        num = q[index('th number')- 1: index('th number')]

        return str(fibonacci())
    elif 'Prime Minister' in q:
        return 'Theresa May'
    elif 'James Bond' in q:
        return 'Sean Connery'

    return "Cancun"


    fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986, 102334155, 165580141, 267914296, 433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976, 7778742049, 12586269025, 20365011074, 32951280099, 53316291173, 86267571272, 139583862445, 225851433717, 365435296162, 591286729879, 956722026041, 1548008755920, 2504730781961, 4052739537881, 6557470319842, 10610209857723, 17167680177565, 27777890035288, 44945570212853, 72723460248141, 117669030460994, 190392490709135, 308061521170129, 498454011879264, 806515533049393, 1304969544928657, 2111485077978050, 3416454622906707, 5527939700884757, 8944394323791464, 14472334024676221, 23416728348467685, 37889062373143906, 61305790721611591, 99194853094755497, 160500643816367088, 259695496911122585, 420196140727489673, 679891637638612258, 1100087778366101931, 1779979416004714189, 2880067194370816120, 4660046610375530309, 7540113804746346429, 12200160415121876738, 19740274219868223167, 31940434634990099905, 51680708854858323072, 83621143489848422977, 135301852344706746049, 218922995834555169026, 354224848179261915075, 573147844013817084101, 927372692193078999176] 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

