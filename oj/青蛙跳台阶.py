def jump(n):
    """
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

    该问题可抽象为斐波那契数列，当青蛙处于台阶n时，它可能是由台阶n-1或台阶n-2跳上来的
    即f(n)=f(n-1)+f(n-2)
    """
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return jump(n-1)+jump(n-2)

n=int(input())
print(jump(n))