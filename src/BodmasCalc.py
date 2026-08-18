import re
import sys


class Bodmas:

    def calculate(self, inpt):
        bf = re.split(r'([+*/-])', inpt)

        num = []
        ops = []

        for i in bf:
            if i in ("+", "-", "*", "/"):
                ops.append(i)
            else:
                num.append(float(i))

        # Debug / POC
        print(num)
        print(ops)

        bnum = []
        bop = []
        x = 0

        for k in range(len(ops)):

            if ops[k] in ["+", "-"]:

                if x <= k:
                    x = k
                    bnum.append(num[x])

                bop.append(ops[k])

            elif ops[k] in ["*", "/"]:

                match ops[k]:

                    case "*":
                        bnum.append(float(num[k] * num[k + 1]))

                    case "/":
                        bnum.append(float(num[k] / num[k + 1]))

                if x < len(ops):
                    x = k + 2
                else:
                    x = k + 1

            else:
                print("Invalid operator")

        result = float(bnum[0])

        for i in range(len(bop)):

            match bop[i]:

                case "+":
                    result += bnum[i + 1]

                case "-":
                    result -= bnum[i + 1]

                case _:
                    print("Invalid operator")

        # Debug / POC
        print(bop)
        print(bnum)

        return result

    def calc(self):
        """
        Interactive mode for local execution.
        """
        inpt = input("Enter the Expression: ")

        result = self.calculate(inpt)

        print("result ", result)


if __name__ == "__main__":

    bd = Bodmas()

    # CI / command-line mode
    if len(sys.argv) > 1:

        expression = sys.argv[1]

        result = bd.calculate(expression)

        print("result ", result)

    # Local interactive mode
    else:

        bd.calc()