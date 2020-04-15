from selenium import webdriver


def translate(choose):
    if choose == 'A' or choose == 'a':
        return 0
    elif choose == 'B' or choose == 'b':
        return 1
    elif choose == 'C' or choose == 'c':
        return 2
    elif choose == 'D' or choose == 'd':
        return 3
    elif choose == 'E' or choose == 'e':
        return 4
    elif choose == 'F' or choose == 'f':
        return 5
    elif choose == 'G' or choose == 'g':
        return 6
    else:
        pass


def submit_choice(question_number, choose):    #选择题

    answer = questions[question_number].find_elements_by_css_selector('li')
    answer[translate(choose)].click()


def submit_multi_choice(question_number, choose):    #多选题
    pass
    answer = questions[question_number].find_elements_by_css_selector('li')
    for i in range(len(choose)):
        answer[translate(choose[i])].click()


def submit_text(question_number, text):    #填空题
    text_area = questions[question_number].find_element_by_css_selector(
        'textarea')
    text_area.send_keys(text)


def submit_multi_text(question_number, answers_list):    #多空填空题
    text_area = questions[question_number].find_elements_by_class_name(
        'underline')
    for i in range(len(answers_list)):
        text_area[i].send_keys(answers_list[i])


def next_page():    #翻页
    next_button = driver.find_element_by_css_selector('#btnNext')
    next_button.click()
    questions = driver.find_elements_by_css_selector('.div_question')


def main():
    submit_text(0, '李狗蛋')
    submit_choice(1, 'A')
    submit_multi_choice(2, ['a', 'b', 'c', 'e'])
    submit_choice(3, 'A')
    submit_text(4, '司马光')
    submit_multi_text(5, ['床前明月光', '举头望明月'])
    submit_text(6, '打119')
    next_page()
    submit_choice(7, 'A')

    # 提交
    submit_button = driver.find_element_by_css_selector('#submit_button')
    submit_button.click()

    input() #等待用户操作后再关闭浏览器
    driver.close()


driver = webdriver.Chrome()
driver.get('https://ks.wjx.top/jq/71431917.aspx')
questions = driver.find_elements_by_css_selector('.div_question')


if __name__ == "__main__":
    main()