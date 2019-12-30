"""
input:输入第一行是n，代表有n个任务、n个人。
接下来输入n行数据，每一行有n个数字，每一行数据的结尾都没有空格。
第i行的第j个数字代表第i个人完成第j个任务所需要花费的cost。(0≤i≤n-1，0≤j≤n-1)
output:输出共有两行，第一行是该问题的最小cost，
第二行是1-n员工分别对应的任务编号list，例如[2,1,3,4]就代表1号员工执行任务2,
2号员工执行任务1,3号员工执行任务3，4号员工执行4号任务。
"""
def plan(k,cost):
    global worker
    global task
    global temp
    global mincost
    if k==n and cost<mincost:       #分配到最后一个人，且此时支出最少，则给min赋值
        mincost=cost
        for i in range(n):
            temp[i]=task[i]+1       #task会在后面置零，提前保存任务的分配方式
    else:
        for i in range(n):
            if worker[i]==0:        #worker未分配
                worker[i]=1
                task[k]=i           #第k个任务属于第i个人
                plan(k+1,cost+graph[k][i])      #分配下一个任务，graph是第k个任务分配给第i个人的支出
                worker[i]=0         #回溯
                task[k]=0
    return mincost

if __name__ == '__main__':
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    worker = [0] * n        #工人是否已经分配了任务
    task = [0] * n          #任务分配给第几个工人
    temp = [0] * n
    mincost=10000

    print(plan(0,0))
    print(temp)
