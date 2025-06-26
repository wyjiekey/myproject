一、标题：
    使用 # 符号来定义标题，从一级标题到六级标题，分别对应 1 到 6 个 # 号。标题级别调整快捷键 Ctrl + Shift + [ 或者 ]

# 第一级标题
## 第二级标题
### 第三级标题
#### 第四级标题
##### 第五级标题
###### 第六级标题

####### 这不是标题

- [第一级标题](#第一级标题)
  - [第二级标题](#第二级标题)
    - [第三级标题](#第三级标题)
      - [第四级标题](#第四级标题)
        - [第五级标题](#第五级标题)
          - [第六级标题](#第六级标题)


二、列表：使用 - * + 开头的无序列表， 使用数字.开头的有序列表

- 列表1-
- 列表2-

* 列表1*
* 列表2*
* 列表3*

+ 列表3 +
+ 列表4 +

1. 列表 1.
2. 列表 2.

三、表格： 使用 | -， ： 对齐

| Header | Header | Header |
| :------ | :------: | ------: |
|   1     |   2     |   \|   1 |
|      3  |  4      |   5    |

四、字体处理

*斜体*

**加粗**

***斜体加粗***

~~删除~~

<u>自带下划线</u>

五、引用、嵌套引用

> 引用
>> 嵌套引用
>>>123


六：任务列表

- [x] 已完成任务
- [ ] 未完成任务

七：行内代码和代码块

行内代码 `print("Hello ,行内代码！')`

```python
# 这是一段python语言
def hello():
    print("hello markdown!")
```

```c
--这里可以写C语言
```

八：图片及链接

![一个爱笑的女孩](./girl.png "test")

[github](https://github.com "github首页")

快捷键

加粗：Ctrl+B（Windows/Linux）或 Command+B（Mac）

斜体：Ctrl+I（Windows/Linux）或 Command+I（Mac）

标题：Ctrl+Shift+H（Windows/Linux）或 Command+Shift+H（Mac）

列表：输入 - 或 1. 后按空格自动生成

任务列表：输入 - [ ] 或 - [x] 后按空格

链接：Ctrl+K（Windows/Linux）或 Command+K（Mac）

代码块：输入 ``` 后按回车

自动生成目录

在文档中插入 [TOC] 并按 Ctrl+Shift+I（Windows/Linux）或 Command+Shift+I（Mac），可自动生成目录。

数学公式

使用 LaTeX 语法：

行内公式：$E=mc^2$

块级公式：
$$
\int_{0}^{\infty} e^{-x^2}   dx = \frac{\sqrt{\pi}}{2}
$$

$$
\int_{-1}^{-\infty}e^{-x^3} 
$$

$$
dx = \frac{\sqrt{\pi}}{3}
$$

自动补全

输入 [ 会自动补全为 []()

输入 ![ 会自动补全为 ![](/path/to/image.png)

其他功能

折叠代码块：点击代码块旁边的 + 或 - 图标

同步滚动：在预览窗口点击同步图标，编辑时预览会自动更新

导出 PDF/HTML：右键点击编辑器，选择 "Export Markdown to PDF/HTML"

脚注

这里有一个脚注引用[^1]

[^1]: 这是脚注的内容

定义列表

术语1
: 定义1

术语2
: 定义2
: 定义3

缩写

*[HTML]: Hyper Text Markup Language
*[CSS]: Cascading Style Sheets

HTML 和 CSS 是网页开发的基础。