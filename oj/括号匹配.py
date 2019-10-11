"""
在实际编程中，我们经常会嵌套使用括号，如“{}”、“[]” 、 “()”，如果括号太多，可能会出现括号不匹配的情况，
比如“(as))”、“{(bcd})”等。现希望你们编写一个程序，判断输入的一段语句中的括号是否匹配。使用栈实现这个功能。
"""
class Stack:
    def __init__(self):
        self.item=[]

    def pop(self):
        return self.item.pop()

    def push(self,data):
        self.item.append(data)

    def size(self):
        return len(self.item)

    def top(self):
        if self.isempty():
            return None
        else:
            return self.item[self.size()-1]

    def isempty(self):
        return self.size()==0


A=Stack()
str=input()

for i in str:
    if i=='('or i==')' or i=='[' or i==']' or i=='{' or i=='}':      #筛选出所需的括号
        if A.top()=='(' and i==')':
            A.pop()
        elif A.top()=='[' and i==']':
            A.pop()
        elif A.top()=='{'and i=='}':
            A.pop()
        else:
            A.push(i)                                                #输入的括号和栈顶的括号匹配则栈顶的括号出栈，否则入栈

if A.isempty():                                                      #最后，若栈为空，说明所有括号都匹配完毕，返回True
    print('True')
else:
    print('False')




