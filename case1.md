　　

## 笔试题

1. 对于一个含有n个变量的程序，采用基本边界值分析法测试程序会产生（）个测试用例。

   A、6n+1     B、7n      C、4n+1      D、5n

   答：C。做测试这么久，还真没有了解过边界值能产生多好条用例，然后我百度了一下

   作者：whylaughing，https://www.cnblogs.com/whylaughing/p/5821898.html ,里面讲的很到位：

   基本边界值产生4n+1条用例。健壮性测试生成的测试用例个数为6n+1。最坏情况的测试生成测试用例 5^n^,健壮性最坏情况的测试生成的测试为 7^n^

2. 一堆数据进行入栈出栈操作，入栈顺序为{a,b,c,d,e,f,g}，可能的出栈顺序为（）

   A、{c,d,e,f,a,g,b}      B、{e,f,d,g,b,c,a}    C、{d,e,c,f,b,g,a}    D、{f,e,g,d,b,a,c}

   答：C。栈的特点是先进后出，所以a一定是最后出的，那么排除了A、D，再看B、C，因为必须保证后进先出。

   B. a入，b入，c入，d入，e入，e出，f入，f出，d出，g入，g出，b不能出，因为c还没有出。

   C. a入，b入，c入，d入，d出，e入，c出，f入，f出，b出，g入，g出，a出 这样是ok的。

3. 当 n =5时，下列函数的返回值是（）

    ```c
    int func(int n){
      if(n<=2){ return n; }
      return func(n-1) + func(n-2);
    }
    ```
    
    
    A、8　　B、13 　　C、5　　D、6
    
    答：A。这是一道java的题，虽然我是java的小菜鸟，但是基本上还是看得懂，其实就是一个递归的用法，类似于python的
    
    
    ```python
    def func(n):
        if n<=2:
            return n
        return func(n-1)+func(n-2)
    
    print(func(5)) 
    #   func(5)=func(4)+func(3)
    # = func(3)+func(2) + fun(2)+func(1)
    # = func(2)+func(1) + func(2) + func(2) + func(1)=2+1+2+2+1
    ```



4. 已知三角形三边abc，现有个程序能判断这个三角形的类别（比如等腰三角形），请为这个程序设计测试用例。

   这个题比较简单，考虑到三角形的定义就能做出来。

   * 任意两边之和大于第三边的是三角形，否则判断未不是三级形。
   * 其余特殊情况，三条边相等就是等边三角形；
   * 两两相等就是等腰三角形；
   * 任意两边的平方等于第三边的平方就是直角。

   ```python
   a=int(input("Please input the first side:"))    #输入第一条边
   b=int(input("Please input the second side:"))   #输入第二条边
   c=int(input("Please input the third side:"))    #输入第三条边
   
   if (a+b>c) and (a+c>b) and (b+c>a):             #判断是否是三角形
       if a==b==c:
           print("This is a equilateral triangle") #等边三角形
       elif (a==b or a==c or b==c):
           print("This is a isosceles triangle")   #等腰三角形
       elif (a*a+b*b==c*c) or (a*a+c*c==b*b) or (c*c+b*b==a*a):
           print("This is a right triangle")       #直角三角形
       else:
           print("This is a scalene triangle")     #不规则三角形
   else :
       print("This isn't a triangle")              #不是三角形
   ```

   

 

5. 设计用例测试下面的Python程序

   ```python
   def Do(a,b,x):
       if(a>1) and (b==0):
           x=x/a
       if (a==2) or (x>1):
           x = x+2
       return x
   ```

   

   解题思路：可以用上unittest来进行单元测试，可能有错误，这块还得完善

   ```python
   import unittest
   
   class MyTest(unittest.TestCase):
       def setUp(self) -> None:
           pass
       def tearDown(self) -> None:
           pass
   
       def test_a_1xiaoyu1(self):
           self.assertEqual(Do(0.5,1,1),1)
   
       def test_a_2dengyu0(self):
           with self.assertRaises(ValueError):
               Do(0,0,1)
   
       def test_a_3dengyu2_1(self):
           self.assertEqual(Do(2,1,1),4)
   
       def test_a_4dengyu2_2(self):
           self.assertEqual(Do(2,1,2),4)
   
   if __name__ == '__main__':
       unittest.main()
   ```

   

 

6. 公司数据库的在职人员表有name和deptment两个字段，分别表示员工姓名和所属部门。请写出一条SQL语句查出每个部门的人数。

   解题思路，查询出每个部门的人数，就是说得通过group by 来查询出部门对应的人数

   ```sql
   select deptment,COUNT(name) from zhiyuan group by deptment 
   ```

   

7. 圣诞节到了，公司举行交换礼物活动，参加的员工每人准备一个礼物。交换完成后，自己的礼物会随机给到另一个人，自己也能随机获得一个其他人准备的礼物。不要求A拿了B的礼物.，B就一定要拿A的，只要自己不拿自己的即可。为公平起见，请你写一个随机程序来决定礼物何分配。

   答：

   ```python
   dictGiftIn = {
       'Jack':'apple',
       'Peter':'beer',
       'Tom':'card',
       'Duke':'doll',
       'Mary':'pineapple',
       'James':'flute',
       'Tina':'coffee'
   }
   dictGiftOut = {}
   
   persons = list(dictGiftIn.keys())
   
   for p in persons:
   	flag = 0 #  标记自己带来的礼物是否还未分配出去
   	if p in dictGiftIn:
   		flag = 1
   	myGift = dictGiftIn.pop(p) #  先在未分配名单中排除该礼物
   	getGift = dictGiftIn.popitem() #  随机返回并移除key-value值, 即分配礼物
   	dictGiftOut[p] = getGift[1] #  已分配礼物名单
   	if flag:
   		dictGiftIn[p] = myGift #  如果当前礼物没有分配，则该礼物重新添到未分配名单中
    
   print(dictGiftOut) #  输出礼物分配情况
   ```

   

