## 兔子序列

题目：假设第1个月有1对刚诞生的兔子，第2个月进入成熟期，第3个月开始生育兔子，而1对成熟的兔子每月会生1对兔子，兔子永不死去……那么，由1对兔子开始，12个月后会有多少对兔子呢？

解答：当月兔子数=上月兔子数+当月新生兔子数=上月兔子数+上上月兔子数

斐波那挈数列：1，1，2，3，5，8，13，21，34，…

递归表达式如下：

$$
F(n) =
\begin{cases}
1, & \text{n = 1}  \\
1, & \text{n = 2}  \\
F(n-1)+F(n-2), & \text{n > 2}
\end{cases}
$$


### 算法设计

```c
Fib1(int n)
{
    if(n<1)
        return -1;
    if(n==1||n==2)
        return 1;
    return Fib1(n-1) + Fib1(n-2);
}
```

算法复杂度为指数阶



### 算法改进1

使用数组记录前两项的和

```c
Fib2(int n)
{
    if(n<1)
        return -1;
    int *a = new int[n+1];  //定义一个长度为n+1的数组
    a[1]=1;
    a[2]=1;
    for(int i=3;i<=n;i++){
        a[i]=a[i-1]+a[i-2];
    }
    return a[n];
}
```

时间复杂度为 $O(n)$，空间复杂度将为了 $O(n)$。



### 算法改进2

抛弃中间结果，使用**迭代法**

```c
Fib3(int n)
{
    int i, s1, s2;
    if(n<1)
        return -1;
    if(n==1||n==2)
        return 1;
    s1=1;
    s2=2;
    
    for(int i=3;i<=n;i++){
        s2=s1+s2;
        s1=s2-s1;
    }
    return s2;
}
```

时间复杂度为 $O(n)$，空间复杂度将为了 $O(1)$。



## 哥德巴赫猜想

哥德巴赫猜想：任一大于2的偶数，都可以表示成两个素数之和。

验证：2000以内大于2的偶数都能够分解为两个素数之和。

算法1：试除法

```c
#include<iostream>
#include<math.h>
int prime(int n);  //判断是否为素数
{
    int i,n;
    for(i=4;i<=2000;i+=2)  //对2000大于2的偶数分解判断，从4开始，每次增加2
    {
        for(n=2;n<i;n++)  //将偶数i分解为两个整数，一个是n，一个是i-n
            if(prime(n))  //判断第一个整数是否为素数
                if(prime(i-n))  //判断第二个整数是否为素数
                {
                    count<< i <<"=" << n << "+"<<i-n<<end1; //若是素数则输出
                    break;
                }
            if(n==i)
                count<< "error "<<end1;
    }
}

int prime(int i)  //判读是否为素数
{
    int j;
    if(i<=1) return 0;
    if(i==2) return 1;
    for(j=2; j<=(int)(sqrt((double)i)); j++)
        if(!(i%j)) return 0;
    return 1;
}
```

改进思路：

1. 用布尔型数组 `flag[2...1998]` 记录分解可能得到的数(2~1998)所有数是不是素数，分解后的值作为下标，调用该数组即可。时间复杂度减少但空间复杂度增加。
2. 用数值型数组 `data[302]` 记录2~1998中所有的素数（302个）
   * 分解后的值，采用折半查找（素数数组为有序存储）的办法在素数数组中查找，找到就是素数，否则不是。