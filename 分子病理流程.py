# coding:utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import datetime
import random

startTime = datetime.datetime.now()
print("开始时间：" + str(startTime))


def login(user_name, passwd):
    browser.find_element_by_id('userName').send_keys(user_name)
    browser.find_element_by_id('password').send_keys(passwd)
    browser.find_element_by_id('btn_login').click()
    sleep(1)


def pathology_add():
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    # 双击分包物流
    fbwl = browser.find_element_by_xpath('//*[@id="treeboxbox_tree"]/div/table/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[4]/span')
    sleep(1)
    ActionChains(browser).double_click(fbwl).perform()

    sleep(1)
    yblr = browser.find_element_by_link_text('病理条码录入')
    yblr.click()

    # 等待病理条码录入页面加载完成
    sleep(2)
    #转到 iframe
    browser.switch_to.frame('content')
    # 选择医院
    khxz = browser.find_element_by_id('comboText1')
    khxz.send_keys(khyy)
    sleep(0.5)
    khxz.send_keys(Keys.ENTER)
    sleep(1)

    # 病理大类
    bldl = browser.find_element_by_id('comboText3')
    bldl.send_keys('分子病理')
    sleep(0.5)
    bldl.send_keys(Keys.ENTER)
    sleep(1)

    # 标本收集者
    bbsjz = browser.find_element_by_id('comboText2')
    bbsjz.send_keys(user_name)
    sleep(0.5)
    bbsjz.send_keys(Keys.ENTER)
    sleep(1)

    barcode_list = []
    # 回执单条码
    hzdtm = browser.find_element_by_id('text1')
    for i in range(bcs, bce):
        tmh = '2018200' + str(i) + '00'
        hzdtm.send_keys(tmh)
        sleep(0.5)
        hzdtm.send_keys(Keys.ENTER)
        sleep(1)
        barcode_list.append(tmh)
    browser.find_element_by_xpath('//*[@id="grid1"]/div[1]/table/tbody/tr[2]/td[1]/div/input').click()
    browser.find_element_by_xpath('//*[@id="tab1"]/div[2]/div[2]/div[1]/input[3]').click()
    sleep(1)
    browser.find_element_by_xpath('//*[@id="popup_ok"]').click()
    print('条码号：' + tmh)
    sleep(1)
    # 切出frame
    browser.switch_to.parent_frame()

    return barcode_list


def fzpathology_add(barcode_list):
    '''
    进入分子病理标本录入页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 分子病理标本录入
    ybhs = browser.find_element_by_link_text('分子病理标本录入')
    sleep(1)
    ybhs.click()

    # 等待样本核收页面加载完成
    sleep(3)
    #转到 iframe
    browser.switch_to.frame('content')

    for tmh in barcode_list:
        tmhSearch = browser.find_element_by_id('txtBarCodeSearch')
        tmhSearch.clear()
        sleep(0.5)
        tmhSearch.send_keys(tmh)
        sleep(1)
        tmhSearch.send_keys(Keys.ENTER)

        sleep(1)
        # 病人姓名
        browser.find_element_by_id('txtPatientName').send_keys('english')
        # 病人电话
        browser.find_element_by_id('txtPatientPhone').send_keys('13666666666')
        # 性别
        xb = browser.find_element_by_id('comboText8')
        xb.send_keys('女')
        sleep(0.5)
        xb.send_keys(Keys.ENTER)
        # 年龄
        nl = browser.find_element_by_id('comboText7')
        nl.send_keys('33')
        # 项目
        xm = browser.find_element_by_id('comboText3')
        xm.send_keys('N-ras基因 codon 12,13,61突变检测')
        sleep(0.5)
        xm.send_keys(Keys.ENTER)

        sleep(1)
        browser.find_element_by_id('btnSave').click()
        sleep(3)
        chebox = browser.find_element_by_id('chkPending')
        if chebox.is_selected():
            chebox.click()
            sleep(0.5)
            chebox.click()
        else:
            chebox.click()
        sleep(1)
        browser.find_element_by_id('btnCheckPending').click()

        sleep(1)
    # 切出frame
    browser.switch_to.parent_frame()


def fzpathology_dis(barcode_list):
    '''
    进入分子病理标本分发页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()


    sleep(1)
    # 分子病理标本分发
    ybhs = browser.find_element_by_link_text('分子病理分发')
    sleep(1)
    ybhs.click()

    sleep(1)
    #转到 iframe
    browser.switch_to.frame('content')

    for tmh in barcode_list:
        tmhsr = browser.find_element_by_id('barCodeInfo')
        tmhsr.send_keys(tmh)
        sleep(1)
        tmhsr.send_keys(Keys.ENTER)
        sleep(3)

    jsr = browser.find_element_by_id('comboText4')
    jsr.send_keys(user_name)
    sleep(0.5)
    jsr.send_keys(Keys.ENTER)
    sleep(0.5)

    browser.find_element_by_id('receivePassword').send_keys(passwd)
    browser.find_element_by_id('btnReceive').click()

    browser.switch_to.parent_frame()

def pathology_accept(barcode_list):
    '''
    进入核收生成病理号页面
    '''
    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    # 病理管理
    blgl = browser.find_element_by_xpath('//*[@id="treeboxbox_tree"]/div/table/tbody/tr[9]/td[2]/table/tbody/tr[1]/td[4]/span')
    sleep(1)
    ActionChains(browser).double_click(blgl).perform()

    sleep(1)
    hsscblh = browser.find_element_by_link_text('核收生成病理号')
    hsscblh.click()
    sleep(2)
    browser.switch_to.frame('content')
    dqbllx = browser.find_element_by_id('pathologyTypeId')
    # 根据 Select 对象的value 值选择病理类型
    # 分子病理FISH
    # Select(dqbllx).select_by_value("40288ea65ab5f078015ab6e26def001b")
    Select(dqbllx).select_by_visible_text(fzbllx)
    sleep(1)

    for tmh in barcode_list :
        #输入条码号
        tiaomahao = browser.find_element_by_id('suBarCodeId')
        tiaomahao.send_keys(tmh)
        sleep(0.5)
        tiaomahao.send_keys(Keys.ENTER)
        sleep(1)
    browser.find_element_by_id('passBtn').click()
    sleep(2)
    # 返回默认内容
    browser.switch_to.default_content()
    browser.switch_to.frame(2)
    sleep(1)
    browser.find_element_by_xpath('//*[@id="okBtn"]').click()


    sleep(2)
    # 切出frame
    browser.switch_to.parent_frame()


def fzpathology_result(barcode_list):


    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()

    sleep(1)
    # 病理管理
    # blgl = browser.find_element_by_xpath(
    #     '//*[@id="treeboxbox_tree"]/div/table/tbody/tr[9]/td[2]/table/tbody/tr[1]/td[4]/span')
    # sleep(1)
    # ActionChains(browser).double_click(blgl).perform()
    # sleep(1)

    # 分子病理结果录入
    bbjglr = browser.find_element_by_link_text('分子病理结果录入')
    sleep(1)
    bbjglr.click()

    # 等待分子病理结果录入页面加载完成
    sleep(2)
    #转到 iframe
    browser.switch_to.frame('content')

    for tmh in barcode_list:
        # 输入条码号，回车
        tiaomahao2 = browser.find_element_by_id('searchCode')
        tiaomahao2.clear()
        sleep(0.5)
        tiaomahao2.send_keys(tmh)
        sleep(1)
        tiaomahao2.send_keys(Keys.ENTER)
        sleep(2)

        browser.find_element_by_id('modifyButton').click()
        sleep(1)
        # 添加项目用药
        browser.find_element_by_id('addMedicationButton').click()
        sleep(1)
        # 返回默认内容
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element_by_xpath('//iframe[contains(@src, "' + tmh + '")]'))

        sleep(1)
        browser.find_element_by_xpath('//*[@id="datagridLeft"]/div[2]/table/tbody/tr[2]/td[2]').click()
        sleep(0.5)
        browser.find_element_by_xpath('/html/body/div[1]/fieldset[2]/div[2]/div[1]/input').click()
        sleep(0.5)
        browser.find_element_by_xpath('/html/body/div[2]/input[1]').click()
        sleep(1)

        browser.switch_to.default_content()
        browser.switch_to.frame('content')
        sleep(1)

        # 点击文字结果录入
        browser.find_element_by_id('editResultButton').click()
        # 返回默认内容
        browser.switch_to.default_content()
        jieg = '/NIP/lab/fzblTestItemResultInfo.action?subBarcode=' + str(tmh)
        browser.switch_to.frame(browser.find_element_by_xpath('//iframe[contains(@src, "' + jieg + '")]'))
        sleep(1)
        if fzbllx == "分子病理FISH":
            browser.find_element_by_id('textarea_0').send_keys('jiancejieguo')
            browser.find_element_by_id('textarea_1').send_keys('jielun')
            browser.find_element_by_id('textarea_2').send_keys('beizhu')
            browser.find_element_by_id('textarea_3').send_keys('pandubiaozhun')
        elif fzbllx == "分子病理测序":
            browser.find_element_by_id('textarea_0').send_keys('jiancejieguo')
        elif fzbllx == "分子病理表达水平":
            browser.find_element_by_id('textarea_0').send_keys('jiancejieguo')
            browser.find_element_by_id('textarea_1').send_keys('jielun')
            browser.find_element_by_id('textarea_2').send_keys('beizhu')
        sleep(1)

        browser.find_element_by_xpath('/html/body/div[2]/input[1]').click()

        sleep(1)
        browser.switch_to.default_content()
        browser.switch_to.frame('content')
        sleep(1)
        qcys = browser.find_element_by_id('comboText2')
        qcys.send_keys(user_name)
        sleep(0.5)
        qcys.send_keys(Keys.ENTER)
        sleep(0.5)
        czys = browser.find_element_by_id('comboText3')
        czys.send_keys(user_name)
        sleep(0.5)
        czys.send_keys(Keys.ENTER)
        sleep(0.5)
        fzys = browser.find_element_by_id('comboText4')
        fzys.send_keys(user_name)
        sleep(0.5)
        fzys.send_keys(Keys.ENTER)
        sleep(0.5)
        yes_time = datetime.datetime.now() + datetime.timedelta(days=-1)
        yes_time_str = yes_time.strftime('%Y-%m-%d %H:%M')
        bbgdsj = browser.find_element_by_id('fixedDate')
        bbgdsj.send_keys(yes_time_str)
        browser.find_element_by_id('remark').send_keys('qitashuoming')
        browser.find_element_by_id('source').send_keys('songjianwu')
        sleep(0.5)
        browser.find_element_by_id('saveButton').click()
        sleep(1)

        browser.find_element_by_id('submitBtn').click()
        sleep(1)
        browser.find_element_by_id('popup_ok').click()
        sleep(1)
        browser.find_element_by_id('popup_ok').click()

        sleep(2)
    # 切出frame
    browser.switch_to.parent_frame()


def pathology_confirm(barcode_list):

    moveto = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveto).perform()

    sleep(1)
    # 医师复核
    browser.find_element_by_link_text('医师复核').click()
    sleep(2)

    browser.switch_to.frame('content')
    sleep(1)
    for tmh in barcode_list:

        seq = browser.find_element_by_id('seq')
        seq.clear()
        sleep(0.5)
        seq.send_keys(tmh)
        sleep(0.5)
        seq.send_keys(Keys.ENTER)
        sleep(2)
        browser.find_element_by_id('finishBtn').click()

        sleep(2)
    # 切出frame
    browser.switch_to.parent_frame()

def fzpathology_reconfirm(barcode_list):

    moveTo = browser.find_element_by_id('left2')
    ActionChains(browser).move_to_element(moveTo).perform()
    sleep(1)


    browser.find_element_by_link_text('总检录入').click()
    sleep(3)

    browser.switch_to.frame('content')
    for tmh in barcode_list:
        searchCode = browser.find_element_by_id('searchCode')
        searchCode.clear()
        sleep(0.5)
        searchCode.send_keys(tmh)
        sleep(1)
        searchCode.send_keys(Keys.ENTER)
        sleep(1)

        browser.find_element_by_id('modifyButton').click()
        sleep(1)
        browser.find_element_by_id('fzblReportRemark').send_keys('fzblReportRemark')
        browser.find_element_by_id('fzblGlassQuality').send_keys('fzblGlassQuality')
        txtResult1 = browser.find_element_by_id('txtResult1')
        txtResult1.send_keys('3')
        sleep(0.5)

        txtResult2 = browser.find_element_by_id('txtResult2')
        txtResult2.send_keys('3')
        sleep(0.5)


        comboText1 = browser.find_element_by_id('comboText1')
        comboText1.send_keys('敏感性很高')
        sleep(0.5)
        comboText1.send_keys(Keys.ENTER)
        sleep(0.5)

        comboText2 = browser.find_element_by_id('comboText2')
        comboText2.send_keys('毒副作用很高')
        sleep(0.5)
        comboText2.send_keys(Keys.ENTER)
        sleep(0.5)

        browser.find_element_by_id('saveButton').click()
        sleep(1)

        browser.find_element_by_id('adviceButton').click()
        sleep(1)
        browser.switch_to.frame(browser.find_element_by_xpath('/html/body/div[9]/div/div[5]/div[1]/iframe'))
        browser.find_element_by_xpath('//*[@id="gridMicAntibioticAdvice"]/tbody/tr/td[3]').click()
        comboText1 = browser.find_element_by_id('comboText1')
        comboText1.send_keys('可选择')
        sleep(0.5)
        comboText1.send_keys(Keys.ENTER)
        sleep(0.5)

        browser.find_element_by_xpath('//*[@id="cancle"]').click()

        sleep(1.5)
        browser.switch_to.parent_frame()
        browser.find_element_by_id('modifyButton').click()
        sleep(1)
        browser.find_element_by_id('saveButton').click()
        sleep(1)

        browser.find_element_by_id('primaryAuditButton').click()
        sleep(1)
        browser.find_element_by_xpath('//*[@id="popup_ok"]').click()
        sleep(1)
        browser.find_element_by_id('reviewButton').click()
        sleep(1)
        browser.find_element_by_xpath('//*[@id="popup_ok"]').click()
        sleep(1)


    browser.switch_to.default_content()
    # 点击安全退出，退出浏览器
    browser.find_element_by_link_text('安全退出').click()
    sleep(1)





if __name__ == '__main__':

    browser = webdriver.Chrome()
    # 隐性等待 10 秒
    browser.implicitly_wait(10)
    browser.maximize_window()
    # browser.get('http://183.63.91.140:8088/NIP/home.action')  # 外网windows测试环境
    # browser.get('http://192.168.14.37/NIP/login.action')        # windows测试环境
    browser.get('http://202.116.104.161/NIP/home.action')     # linux测试环境

    khyy = '潮州中医院'
    user_name = 'daan'
    passwd = '123@abc'
    # 分子病理类型仅有三种：分子病理FISH、分子病理测序、分子病理表达水平
    fzbllx = "分子病理测序"

    bcs = 169
    bce = 175



    login(user_name, passwd)
    barcode_list = pathology_add()
    fzpathology_add(barcode_list)
    fzpathology_dis(barcode_list)

    # sleep(1)
    # browser.switch_to.default_content()
    # # 点击安全退出，退出浏览器
    # browser.find_element_by_link_text('安全退出').click()
    # sleep(1)


    pathology_accept(barcode_list)
    fzpathology_result(barcode_list)
    pathology_confirm(barcode_list)
    fzpathology_reconfirm(barcode_list)

        # browser.quit()


