class Solution:
    def eval(self,tokens):
        st = []

        def is_operator(s):
            return s in ["+", "-", "*", "/"]

        for token in tokens:
            if is_operator(token):
                ele2 = int(st.pop())
                ele1 = int(st.pop())
                if token == "+":
                    result = ele1 + ele2
                elif token == "-":
                    result = ele1 - ele2
                elif token == "/":
                    result = int(ele1 / ele2)
                elif token == "*":
                    result = ele1 * ele2
                st.append(str(result))
            else:
                st.append(token)
        return int(st[-1])
l=['2','1','+','3','*']
c=Solution()
a=c.eval(l)
print(a)