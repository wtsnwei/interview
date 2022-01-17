### 算法设计

#### 步骤1：确定合适的数据结构

设置带权领接矩阵 `C` 存储图 `G`，如果图 `G` 中存在边 `(u, x)`，令 `C[u][x]` 等于边 `(u, x)` 上的权值，否则， $C[u][x] = \infty$；bool 数组 `s[]`，如果 `s[i]=true`，说明顶点 `i` 已加入集合 `U`。

`closest[j]` 表示 V-U 中的顶点 j 到集合 U 中的最临近点，`lowcost[j]` 表示 V-U 中的顶点 j 到集合 U 中的最临近点的边值，即边 `(j, closest[j])` 的权值。

#### 步骤2：初始化

令集合 U={$u_0$}，$u_0$ 属于V，初始化数组 closest[]、lowcost[] 和 s[]。

#### 步骤3

在 V-U 集合中找 lowcost 值最小的顶点 t，即 $lowcost[t]=min\{lowcost[j]\ |\ j \in V-U\}$，满足该公式的顶点 t 就是集合 V-U 中连接 U 的最临近点。

#### 步骤4

将顶点 t 加入到集合 U

#### 步骤5

如果集合 V-U，算法结束，否则，转步骤6.

#### 步骤6

对集合 V-U 中所有的顶点 j，更新其 lowcost[] 和 closest[]。更新公式：$if (C[t][j]<lowcost[j])\ \{lowcost[j]=C[t][j];\ closest[j]=t;\}$，转步骤3。



### 伪代码详解

#### 1、初始化

`s[1]=true`，初始化数组 `closest`，除了 $u_0$ 外其余顶点最临近点均为 $u_0$，表示 V-U 中的顶点到集合 U 的最临近点均为 $u_0$；初代数组 lowcost，$u_0$ 到 V-U 中的顶点的边值，无边相连为 $\infty$。

```c++
s[u0]=true; // 初始时，集合U中只有一个元素，即顶点u0
for(i=1; i<=n; i++){ // n为顶点个数
    if(i!=u0) // 除u0外的顶点
    {
        lowcost[i] = c[u0][i]; //u0到其他顶点的边值
        closest[i] = u0; //最临近点初始化为u0
        s[i] = false;  //初始化u0之外的顶点不属于U集合，即V-U集合
    } else{
        lowcost[i] = 0;
    }
}
```

#### 2、在集合 V-U 中寻找距离集合 U 最近的顶点 t。

```c++
int temp = INF;
int t = u0;
for(j=1; j<=n; j++){  //在集合中V-U中寻找距离U最近的顶点t
    if(!s[j] && (lowcost[j]<temp)) //!s[j]表示j节点在V-U中
    {
        t=j;
        temp=lowcost[j];
    }
}
if(t==u0) //找不到t，跳出循环
{
    break;
}
```

#### 3、更新 lowcost 和 closest 数组

```c++
s[t]=true;  //否则，将t加入集合U
for(j=1; j<=n; j++) // 更新lowcost和closest
{
    if((!s[j]) && (c[t][j]<lowcost[j])) // !s[j]表示j节点在V-U中，t到j的边值小于当前最临近值
    {
        lowcost[j]=c[t][j]; // 更新j的最临近值为t到j的边值
        closest[j]=t; //更新j的最临近点为t
    }
}
```



### 实战代码

```c++
#include <iostream>
using namespace std;
const int INF = 0x3fffffff;
const int N = 100;
bool s[N];
int closest[N];
int lowcost[N];

void Prim(int n, int u0, int c[N][N])
{
    s[u0] = true; //初始时，集合U中只有一个元素u0
    int i;
    int j;
    for(i=1; i<=n; i++){
        if(i!=u0){
            lowcost[i] = c[u0][i];
            closest[i] = u0;
            s[i] = false;
        }
        else {
            lowcost[i] = 0;
        }
    }
    
    for(i=1; i<=n; i++){
        int temp = INF;
        int t = u0;
        for(j=1; j<=n; j++) //在集合V-U中寻找距离集合U最近的顶点t
        {
            if((!s[j]) && (lowcost[j]<temp)){
                t = j;
                temp = lowcost[j];
            }
        }
        if(t == u0) {break;} // 找不到t，跳出循环
        
        s[t] = true; //否则将t加入集合U
        for(j=1; j<=n; j++) // 更新lowcost和closest
        {
            if({(!s[j]) && (c[t][j] < lowcost[j])){
                lowcost[j] = c[t][j];
                closest[j] = t;
            }
        }
    }
}
```



