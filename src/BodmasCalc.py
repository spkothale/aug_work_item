import re
class Bodmas:
    def calc(self):
        inpt = input("Enter the Expression: ")
        bf = re.split(r'([+*/-])',inpt)

        num = []
        ops = []
        for i in bf:
            if i in ("+","-","*","/"):
                ops.append(i)
            else:
                num.append(float(i))
        # result = float(num[0])

        print(num)
        print(ops)
        #step for poc
        bnum = []
        bop  = []
        x = 0

        for k in range(len(ops)):
            if ops[k] in ["+","-"]:
                if (x <= k):
                    x = k
                    bnum.append(num[x])
                bop.append(ops[k])

            elif ops[k] in ["*","/"]:
                match ops[k]:
                    case "*":
                        bnum.append(float(num[k] * num[k+1]))
                    case "/":
                        bnum.append(float(num[k] / num[k+1]))
                if x<len(ops):
                    x = k+2
                else:
                    x=k+1
            else:
                print("Invalid operator")

        result = float(bnum[0])
        for i in range(len(bop)):
            match bop[i]:
                case "+":
                    result += bnum[i+1]
                case "-":
                    result -= bnum[i+1]
                case _:
                    print("Invalid operator")

        print(bop)
        print(bnum)
        print("result ",result)


bd=Bodmas()
bd.calc()