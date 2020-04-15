问卷星快速交卷，做全班最靓的仔！  
==============================

这是什么？
---------------------
* 这个项目能做什么?
    >使用Python+Selenium模拟用户动作，自动填写问卷星号。  
    >通常在3秒内完成从打开到提交的操作。
* 这个项目的意义是什么?
    >在考试中用最快的速度交卷，让你成为众人关注的焦点。
    >![GitHub Logo](./demo.png)

怎么用？
----------------------
不要忘记程序员从0开始计数。
* 选择题
    >submit_choice(question_number, choose)
* 多选题
    >submit_multi_choice(question_number, choose_list)
* 填空题
    >submit_text(question_number, text)
* 多空填空题
    >submit_multi_text(question_number, answers_list)
* 翻页
    >next_page()
* 提交
    >submit()

项目需求
--------------------------
以下是需要为项目安装的库(模块)。点击文本将会出现相应的官方文档。请确保安装了相应的最新版本。另外不要忘记安装WebDriver，这里我使用的是Chrome浏览器，所以你应该安装的是ChromeDriver。

* [selenium](https://www.selenium.dev/documentation/zh-cn/)
