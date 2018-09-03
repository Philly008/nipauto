# coding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import datetime
import logging
from selenium.webdriver.support.ui import WebDriverWait
from com.预生产环境 import getData
from selenium.webdriver.support.select import Select


def login_nip(user_name, password):
    logging.info('***** 登录 *****')
    # 输入用户名、密码，登录
    browser.find_element_by_id('userName').send_keys(user_name)
    browser.find_element_by_id('password').send_keys(password)
    browser.find_element_by_id('btn_login').click()
    sleep(1)
    return browser


def specimen_add(browser):
    # 鼠标移动到左侧菜单栏
    moveto = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveto).perform()
    sleep(1)
    # 双击分包物流
    fbwl = browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/span')
    ActionChains(browser).double_click(fbwl).perform()

    '''
    进入样本录入页面
    '''
    browser.find_element_by_link_text('样本录入').click()
    logging.info('***** 样本录入start *****')
    sleep(5)
    # 转到样本录入 iframe
    browser.switch_to.frame('content')

    # 点击新增
    browser.find_element_by_xpath('//*[@id="btnAdd"]').click()

    tmh_list = []
    # 编辑基本信息

    # 条码号
    browser.find_element_by_id('txtBarCode').send_keys(barcode)
    sleep(10)
    browser.find_element_by_id('txtBarCode').send_keys(Keys.ENTER)
    sleep(1)

    # 病人类型，住院
    browser.find_element_by_xpath('//*[@id="comboBtn2"]/a').click()
    browser.find_element_by_xpath('//*[@id="132"]/td[2]').click()
    # 点击医院的下拉框倒三角
    browser.find_element_by_xpath('//*[@id="comboBtn1"]/a[1]').click()
    # 搜索 天方达 并回车
    hospit = browser.find_element_by_id('comboText1')
    hospit.clear()
    hospit.send_keys(khyy)
    sleep(1)
    hospit.send_keys(Keys.ENTER)
    sleep(0.5)
    # 证件号，6位地区好、8位出生日期、4位尾号
    browser.find_element_by_id('txtRegion').send_keys('445122')
    browser.find_element_by_id('txtBirth').send_keys('19891126')
    browser.find_element_by_id('txtTail').send_keys('066X')
    # 临床诊断
    browser.find_element_by_id('txtClinicalRemark').send_keys('linchuangzhenduan')
    # 采样日期，当前日期的月、日
    browser.find_element_by_id('txtColMon').send_keys(datetime.datetime.now().month)
    browser.find_element_by_id('txtColDay').send_keys(datetime.datetime.now().day)
    # 医生电话
    browser.find_element_by_id('txtDoctorPhone').send_keys('yishengdianhua')
    # 病人电话
    browser.find_element_by_id('txtPatientPhone').send_keys('bingrendianhua')
    # 姓名
    browser.find_element_by_id('txtPatientName').send_keys('L常规')
    # 性别
    xingbie = browser.find_element_by_id('comboText8')
    xingbie.send_keys('女')
    sleep(0.5)
    xingbie.send_keys(Keys.ENTER)
    # 体重 kg
    browser.find_element_by_id('txtPatientWeight').send_keys('65')
    # 身高 cm
    browser.find_element_by_id('txtPatientHeight').send_keys('168')
    # 年龄
    # browser.find_element_by_xpath('//*[@id="comboBtn7"]/a').click()
    # browser.find_element_by_xpath('//*[@id="adult"]/td[2]').click()
    sleep(0.5)
    '''
    无创信息
    '''
    # 出生日期
    browser.find_element_by_id('txtBirYear').send_keys('1990')
    browser.find_element_by_id('txtBirMon').send_keys('11')
    browser.find_element_by_id('txtBirDay').send_keys('12')
    # B超孕周孕日
    browser.find_element_by_id('txtBultrasonic').send_keys('14')
    browser.find_element_by_id('txtPregnant').send_keys('4')
    browser.find_element_by_id('txtLmpTime').send_keys('2018-05-11')
    taishu = browser.find_element_by_id('comboText10')
    taishu.send_keys('1')
    sleep(0.5)
    taishu.send_keys(Keys.ENTER)
    sleep(1)
    # 诊疗卡号
    browser.find_element_by_id('txtPatientNo').send_keys('106000191300')
    # 床号
    browser.find_element_by_id('txtBed').send_keys('chuanghao')
    # 科室
    department = browser.find_element_by_id('comboText5')
    department.send_keys(template)
    sleep(0.5)
    department.send_keys(Keys.ENTER)
    # 医生
    doctor = browser.find_element_by_id('comboText4')
    doctor.send_keys(head)
    sleep(0.5)
    doctor.send_keys(Keys.ENTER)
    # 获取检验项目下拉框
    # for item in test_items:
    jyxm = browser.find_element_by_id('comboText3')
    jyxm.send_keys(item)
    sleep(1)
    jyxm.send_keys(Keys.ENTER)
    sleep(3)
    # 其他说明
    browser.find_element_by_id('txtRemark').send_keys('孕产史：qitashuoming')

       # 其他信息

    browser.find_element_by_xpath('//*[@id="tabOther"]').click()

    testTubeBaby = browser.find_element_by_id('testTubeBaby')
    # 根据 Select 对象的value 值选择病理类型
    Select(testTubeBaby).select_by_value("1")

    bloodTransfusion = browser.find_element_by_id('bloodTransfusion')
    # 根据 Select 对象的value 值选择病理类型
    # shuxue = Select(bloodTransfusion).select_by_value("1")
    shuxue = Select(bloodTransfusion).select_by_index("1")

    transplantation = browser.find_element_by_id('transplantation')
    # 根据 Select 对象的value 值选择病理类型
    Select(transplantation).select_by_value("1")

    stemCellTreatment = browser.find_element_by_id('stemCellTreatment')
    # 根据 Select 对象的value 值选择病理类型
    Select(stemCellTreatment).select_by_value("1")

    immune = browser.find_element_by_id('immune')
    # 根据 Select 对象的value 值选择病理类型
    Select(immune).select_by_value("1")

    tumour = browser.find_element_by_id('tumour')
    # 根据 Select 对象的value 值选择病理类型
    Select(tumour).select_by_value("1")
    browser.find_element_by_id('twentOneBodyRisk').send_keys('3')
    browser.find_element_by_id('eighteenBodyRisk').send_keys('3')
    browser.find_element_by_id('ontdRisk').send_keys('3')
    browser.find_element_by_id('inspectCustomer').send_keys('3')
    browser.find_element_by_id('samplingCustomer').send_keys('3')
    sleep(1)
    browser.find_element_by_xpath('//*[@id="tabInfo"]').click()
    sleep(1)



    # 点击保存
    bc = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_id('btnSave'))
    bc.click()
    sleep(2)
    tmh_list.append(barcode)

    # print(tmh_list)
    sleep(1)
    searcheBarcode = browser.find_element_by_id('txtBarCodeSearch')
    searcheBarcode.send_keys(barcode)
    sleep(0.5)
    searcheBarcode.send_keys(Keys.ENTER)
    sleep(1)
    gxsj = WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_id('chkPending'))
    gxsj.click()
    # 勾选待审数据
    # browser.find_element_by_xpath('//*[@id="chkPending"]').click()
    # 信息审核
    browser.find_element_by_id('btnCheckPending').click()

    # 退出样本录入 iframe
    browser.switch_to.parent_frame()
    logging.info('***** 样本录入end *****')
    return tmh_list


def specimen_accept(browser, tmh):
    logging.info('***** 样本核收start *****')
    '''
    进入样本核收页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 样本核收
    browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[10]/td[2]/table/tbody/tr/td[4]/span/a').click()
    sleep(2)
    # 转到样本核收 iframe
    browser.switch_to.frame('content')
    # 点击查询
    browser.find_element_by_id('btnSearch').click()
    sleep(1)
    # 点击全部选择
    #browser.find_element_by_id('btnScanAll').click()
    # 输入条码号，回车，扫描条码号
    browser.find_element_by_id('txtBarCode').send_keys(tmh)
    sleep(0.5)
    browser.find_element_by_id('txtBarCode').send_keys(Keys.ENTER)
    sleep(1)
    # 点击已扫条码
    browser.find_element_by_xpath('//*[@id="rightTabBar"]/div/div[1]/div/div[2]/span').click()

    hsr = browser.find_element_by_id('comboText6')
    hsr.send_keys(user1)
    sleep(1)
    hsr.send_keys(Keys.ENTER)
    sleep(0.5)
    # 密码
    browser.find_element_by_id('txtPassWord').send_keys(passwd)
    # 点击核收
    browser.find_element_by_id('btnCheck').click()
    # 退出样本核收 iframe
    browser.switch_to.parent_frame()
    logging.info('***** 样本核收end *****')


def specimen_distribute(browser, tmh_list):
    logging.info('***** 样本分发start *****')
    '''
    进入样本分发页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 样本分发
    browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[12]/td[2]/table/tbody/tr/td[4]/span/a').click()
    sleep(3)
    # 转到样本分发 iframe
    browser.switch_to.frame('content')

    for tmh in tmh_list:
        # 输入条码号，回车，分发条码号
        browser.find_element_by_xpath('//*[@id="barCodeInfo"]').send_keys(tmh)
        sleep(1)
        browser.find_element_by_xpath('//*[@id="barCodeInfo"]').send_keys(Keys.ENTER)
        sleep(3)
    # 接收人倒三角
    jieshouren = browser.find_element_by_id('comboText4')
    jieshouren.clear()
    jieshouren.send_keys(user1)
    sleep(1)
    # 对接收人文本框进行回车按键
    jieshouren.send_keys(Keys.ENTER)

    # 密码
    browser.find_element_by_id('receivePassword').send_keys(passwd)
    # 点击确认接收
    browser.find_element_by_id('btnReceive').click()
    sleep(1)
    # 退出样本分发 iframe
    browser.switch_to.parent_frame()
    logging.info('***** 样本分发end *****')


def specimen_ready(browser, tmh_list):
    logging.info('***** 样本准备start *****')
    '''
    进入样本准备页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 样本检测
    ybjc = browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[1]/td[4]/span')
    # sleep(1)
    ActionChains(browser).double_click(ybjc).perform()

    sleep(1)
    # 样本准备
    browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[4]/span/a').click()
    sleep(1)
    # 转到 iframe
    browser.switch_to.frame('content')
    sleep(1)
    aa = browser.find_element_by_xpath('//*[@id="comboText1"]')
    aa.send_keys(instrument)
    sleep(1)
    aa.send_keys(Keys.ENTER)
    sleep(1)
    bb = browser.find_element_by_id('subarCodeId')
    bb.send_keys(tmh_list)
    sleep(1)
    bb.send_keys(Keys.ENTER)
    sleep(1)
    browser.switch_to.default_content()


def specimen_result(browser, tmh_list, xmjg):
    logging.info('***** 结果录入start *****')
    '''
    进入结果录入页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 样本检测
    ybjc = browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[1]/td[4]/span')
    # sleep(1)
    ActionChains(browser).double_click(ybjc).perform()

    sleep(1)
    # 结果录入
    browser.find_element_by_xpath('//*[@id="treeboxbox_tree"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr/td[4]/span/a').click()
    sleep(2)
    # 转到 iframe
    browser.switch_to.frame('content')

    sleep(1)

    # 仪器倒三角
    browser.find_element_by_xpath('//*[@id="comboBtn1"]/a[1]').click()
    sleep(1)
    # 搜索仪器 西门子2 并回车
    instrumentE = browser.find_element_by_id('comboText1')
    instrumentE.send_keys(instrument)
    sleep(1)
    instrumentE.send_keys(Keys.ENTER)
    sleep(3)
    for tmh in tmh_list:
        cztm = browser.find_element_by_id('txtSearchSubBarCode')
        cztm.send_keys(tmh)
        sleep(1)
        cztm.send_keys(Keys.ENTER)
        sleep(2)
        table_element = browser.find_element_by_id('gridTestItem')
        # 定位到行
        tr_elements = table_element.find_elements_by_tag_name('tr')
        td_list = []
        for td in tr_elements:
            td_elements = td.find_elements_by_tag_name('td')
            # 第 6 列，即结果输入列拼接在列表中
            td_list.append(td_elements[5])

        # 循环结果列
        for j in range(len(td_list)):
            # 结果列为空才输入结果
            if td_list[j].text == '':
                # 定位到列的对应输入框
                jg1 = td_list[j].find_element_by_id('comboText5')
                jg1.click()
                # 清空并填写结果值
                jg1.clear()
                jg1.send_keys(xmjg)
                sleep(0.5)
                jg1.send_keys(Keys.ENTER)
                sleep(1)

        jyjs = browser.find_element_by_id('txtReportRemark')
        jyjs.clear()
        jyjs.send_keys('jianyijieshi')
        zdxj = browser.find_element_by_id('txtReportBrief')
        zdxj.clear()
        zdxj.send_keys('zidongxiaojie')

    # 点击提交标本
    browser.find_element_by_id('btnSubmitSpecimen').click()
    sleep(1)
    browser.find_element_by_id('popup_ok').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="popup_ok"]').send_keys(Keys.ENTER)

    logging.info('***** 结果录入end *****')
    sleep(1)
    browser.switch_to.default_content()
    # 点击安全退出，退出浏览器
    browser.find_element_by_link_text('安全退出').click()
    sleep(1)


def specimen_audit(browser):
    logging.info('***** 签字审核start *****')
    '''
    进入签字审核页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    ybjc = browser.find_element_by_xpath(
        '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[8]/td[2]/table/tbody/tr[1]/td[4]/span')
    sleep(1)
    ActionChains(browser).double_click(ybjc).perform()

    sleep(1)
    # 签字审核
    browser.find_element_by_link_text('签字审核').click()

    sleep(2)
    # 转到 iframe
    browser.switch_to.frame('content')

    sleep(1)

    # 仪器倒三角
    yq = browser.find_element_by_xpath('//*[@id="comboBtn1"]/a[1]').click()
    sleep(1)
    # 搜索仪器 并回车
    instrumentE = browser.find_element_by_id('comboText1')
    instrumentE.send_keys(instrument)
    sleep(1)
    instrumentE.send_keys(Keys.ENTER)
    sleep(5)
    browser.find_element_by_id('chkList').click()

    # 点击审核标本
    browser.find_element_by_id('btnAuditSpecimen').click()
    sleep(1)
    browser.find_element_by_id('popup_ok').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="popup_ok"]').send_keys(Keys.ENTER)
    logging.info('***** 签字审核end *****')
    sleep(1)
    browser.switch_to.default_content()
    # 点击安全退出，退出浏览器
    browser.find_element_by_link_text('安全退出').click()
    sleep(1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s ')
    startTime = datetime.datetime.now()
    logging.info("开始时间：" + str(startTime))

    chromedriver = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chromedriver)
    # 隐性等待 10 秒，只需要设置一次
    browser.implicitly_wait(30)
    # 最大化浏览器
    browser.maximize_window()
    # 访问网址
    browser.get('http://47.99.16.10/NIP/home.action')
    #browser.get('http://192.168.14.37/NIP/home.action')

    user1 = 'liu1'
    user2 = 'liu2'
    passwd = '123abc'

    # barcode = '2018' + str(random.randint(2000, 2999)) + '0000'
    xmjg = '1'
    # khyy = '郑州大学附属郑州中心医院'
    # item = '血清C肽测定(CP)'
    # instrument = '西门子2'
    # i = 0
    tmhec = []
    tmhsh = []
    for i in range(190, 191):
        barcode = getData.get_normal_barcodes()[i]
        khyy = getData.get_normal_customers()[i]
        item = getData.get_normal_items()[i]
        instrument = getData.get_normal_instruments()[i]
        template = getData.get_report_templates()[i]
        head = getData.get_report_heads()[i]

        try:
            login_nip(user1, passwd)
            tmh_list = specimen_add(browser)
            specimen_accept(browser,tmh_list)
            specimen_distribute(browser, tmh_list)
            # specimen_ready(browser, tmh_list)
            specimen_result(browser, tmh_list, xmjg)
            login_nip(user2, passwd)
            specimen_audit(browser)
            print('已签字审核的条码号为：' + str(barcode))
            tmhsh.append(barcode)
            sleep(1)
        except Exception as e:
            print('出现异常的条码号为：' + barcode + '\n' + str(e))
            browser.get_screenshot_as_file(str(barcode) + 'Error.png')
            tmhec.append(barcode)
            sleep(1)
            browser.switch_to.default_content()
            # 点击安全退出，退出浏览器
            browser.find_element_by_link_text('安全退出').click()
            sleep(1)
            continue

    print('异常条码号有这些：' + str(len(tmhec)) + '个。\n'+ str(tmhec))
    print('已审核条码号有这些：' + str(len(tmhsh)) + '个。\n'+ str(tmhsh))



    endTime = datetime.datetime.now()
    logging.info('结束时间：' + str(endTime))
    totalTime = endTime - startTime
    logging.info('消耗时间(s)：' + str(totalTime.seconds))
