import random

# import numpy

list1 = []
dict1 = {}
n = 10
i = 0
while i < n:
    x, y = random.uniform(1, 6, 2)
    re = x + y
    list1.append(re)
    dict1[i] = list1.count(re)
    i += 1
print(dict)
'''
2. 编写程序解决以下问题：长度为N的数组，随机放入值为1-50中间的任意整数，请编写程序找出其中的偶数数字，并按照该数字在数组中出现次数从多到少排序输出。
'''

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)
dict1 = {}
for i in list1:
    print(list1.count(i))
    if i % 2 == 0:
        # dict[i] = list1.count(i)
        print(dict1)
"""
3.	（10分）编写程序列出一个目录下所有的文件，包括所有子目录下的文件，并打印出文件总数。
"""
import os

list_first = os.listdir("H:\muqia_data\python_code")
print(type(list_first), list_first)
list_second = []
i = 0
for path in list_first:
    if os.path.isdir(path):
        os.path.getsize(path)
        list_second_single = os.path.abspath(path)
        list_second.append(list_second_single)
        i += 1
print(list_second, i)
"""
4.	（20分）有一张班级学生表有3个字段分别为学生姓名：STUDENT、性别：GENDER、身高：STATURE。请编写程序为该班学生
排座位，规则如下：
1）教室共4排座位，每个座位都可以坐2人（有同桌）
2）身高矮的同学坐在前排，身高高的坐后面
3）同桌必须为同性别同学，若同性别人员为奇数，只允许最后一排位置一个人坐
"""

"""
5.	（10分）找出这样的数字：一个数字等于它的各分解项相加。示例数字 28可分解为1、2、4、7、14，1+2+4+7+14=28。
同样，数字6分解为:1、2、3，1+2+3=6。用代码找出1-500以内的所有符合这样条件的数字。
"""

"""
6.	（6分）请编写一个函数，能将字符串main-action-holder，转换为mainActionHolder
"""
str1 = "main-action-holder"
list1 = str1.split("-")
for i in range(1, len(list1)):
    list1[i] = list1[i].title()
str1 = "".join(list1)
print(str1)

"""
7.	（20分）简单实现在线购买电影票，请重点考虑多人同时购买一个座位的情况，可以使用伪代码
"""

"""
8.	（7分）学生表：STUDENT(ID,USER_NAME)和考试表：EXAM(ID,USER_ID,SCORE)表，STUDENT表主键为ID字段，
EXAM表中外键USER_ID为STUDENT的ID字段值，编写SQL查询每位学生的成绩，缺考的以0分处理（缺考的考试表中无记录）
"""
'''
CREATE TABLE `cancel1`.`student` (
    `id` INT NOT NULL,
    `username` VARCHAR(45) NULL,
    PRIMARY KEY (`id`)
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8;

CREATE TABLE `cancel1`.`exam` (
    `id` INT NOT NULL,
    `user_id` INT NOT NULL,
    `score` INT DEFAULT 0,
    PRIMARY KEY (`id`),
    CONSTRAINT `user_id` FOREIGN KEY (`user_id`)
        REFERENCES `cancel1`.`student` (`id`)
        ON DELETE CASCADE ON UPDATE CASCADE
)  CHARSET=UTF8;
use cancel1;
insert into cancel1.student (id,username) values(1,'wang'),(2,'ba'),(3,'dan'),(4,'yao'),(5,'yue');
insert into cancel1.exam (id,user_id,score) values(1,2,200),(2,3,400),(3,1,100),(4,5,230);

SELECT 
    *
FROM
    student;
SELECT 
    *
FROM
    exam;
SELECT 
    `cancel1`.`student`.`username`, `cancel1`.`exam`.`score`
FROM
    `cancel1`.`student`,
    `cancel1`.`exam`
WHERE
    `cancel1`.`student`.`id` = `cancel1`.`exam`.`user_id`;
SELECT 
    `cancel1`.`student`.`username`, `cancel1`.`exam`.`score`
FROM
    `cancel1`.`student`
        LEFT JOIN
    `cancel1`.`exam` ON `cancel1`.`student`.`id` = `cancel1`.`exam`.`user_id`;

'''

"""
9.	（7分）已知用户表USER(ID,USER_NAME,AGE),通过sql语句查询表中相同年龄（AGE）存在两条以上记录的用户年龄及
用户个数，并按照统计数量倒排序
"""
'''
CREATE TABLE `cancel1`.`user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_name` VARCHAR(45) NOT NULL,
    `age` INT(2) NOT NULL,
    PRIMARY KEY (`id`)
)  ENGINE=INNODB DEFAULT CHARACTER SET=UTF8;
insert into cancel1.user (user_name,age) values('wang',23),('ba',34),('dan',23),('yao',23),('yue',34),('xi',34),('xixi',34),('lan',22),('ren',22);
select * from user;

SELECT 
    age, COUNT(age)
FROM
    user
GROUP BY age
HAVING COUNT(age) > 2
ORDER BY COUNT(age) DESC;
'''
