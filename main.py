import sys
if sys.platform == "win32":
    import ctypes
    import winreg


    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False


    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

from PySide2 import QtWidgets
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
import os
import pickle

import main_ui
import messagebox


class MainWindow(QtWidgets.QMainWindow, main_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.dialog = None
        self.driver = None
        self.info = {"date": "", "time": "", "ticket": "", "money": "", "id": ""}

        self.getticket.clicked.connect(self.get_ticket)
        self.save_config.clicked.connect(self.save_config_func)

        self.read_config()

    def save_config_func(self):
        select_webdriver = self.webdriver_select.currentIndex()

        account = self.account.text()
        password = self.password.text()

        yourname = self.yourname.text()
        birthday = {"year": self.biryear.text(), "month": self.birmouth.text(), "day": self.birday.text()}
        telephone = self.telephone.text()

        card_type = self.xyk_type.currentIndex()
        card_no = self.card1.text() + self.card2.text() + self.card3.text() + self.card4.text()
        card_end = {"year": self.card_year.text(), "month": self.card_mouth.text()}

        save_config = {"webdriver": select_webdriver,
                       "account": account, "password": password,
                       "yourname": yourname, "birthday": birthday, "telephone": telephone,
                       "card_type": card_type, "card_no": card_no, "card_end": card_end}
        with open("config.pickle", "wb") as file:
            pickle.dump(save_config, file)

    def read_config(self):
        try:
            with open("config.pickle", "rb") as file:
                save_config = pickle.load(file)
        except:
            return

        self.webdriver_select.setCurrentIndex(save_config["webdriver"])

        self.account.setText(save_config["account"])
        self.password.setText(save_config["password"])
        self.yourname.setText(save_config["yourname"])

        birthday = save_config["birthday"]
        self.biryear.setText(birthday["year"])
        self.birmouth.setText(birthday["month"])
        self.birday.setText(birthday["day"])

        self.telephone.setText(save_config["telephone"])
        self.xyk_type.setCurrentIndex(save_config["card_type"])

        card_no = save_config["card_no"]
        try:
            self.card1.setText(card_no[0:4])
            self.card2.setText(card_no[4:8])
            self.card3.setText(card_no[8:12])
            self.card4.setText(card_no[12:16])
        except:
            pass

        card_end = save_config["card_end"]
        self.card_year.setText(card_end["year"])
        self.card_mouth.setText(card_end["month"])

    @staticmethod
    def get_desktop_or_user_folder():
        if sys.platform == "win32":
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
            return winreg.QueryValueEx(key, "Desktop")[0]
        else:
            return os.path.expanduser("~")

    def show_msg_box(self, days):
        self.dialog = MessageBox(self)
        self.dialog.days.setText(days)
        return self.dialog.exec_()

    def get_ticket(self):
        self.getticket.setDisabled(True)
        self.url.setDisabled(True)

        if self.is_open_timeup.checkState():
            timeup1 = self.start_hour.text() + ":" + self.start_min.text() + ":" + self.start_sec.text()
            while True:
                if time.strftime("%H:%M:%S") == timeup1:
                    break

        webdrivers = [webdriver.ChromiumEdge, webdriver.Chrome, webdriver.Firefox, webdriver.Safari, webdriver.Ie]

        self.driver = webdrivers[self.webdriver_select.currentIndex()]()
        self.driver.maximize_window()
        self.driver.get("https://www.globalinterpark.com/user/signin")

        # 登录
        self.driver.find_element(By.NAME, "memEmail").send_keys(self.account.text())
        self.driver.find_element(By.NAME, "memPass").send_keys(self.password.text())
        self.driver.find_element(By.ID, "sign_in").click()
        time.sleep(1)

        # 抢票
        self.driver.get(self.url.toPlainText())

        if self.is_open_timeup.checkState():
            timeup2 = self.timeup_hour.text() + ":" + str(int(self.timeup_min.text()) - 1) + ":55"
            while True:
                if time.strftime("%H:%M:%S") == timeup2:
                    break

        self.driver.switch_to.frame(self.driver.find_element(By.ID, "product_detail_area"))
        if self.is_reload.checkState():
            self.driver.refresh()

        wait_select_dom = self.driver.find_element(By.ID, "play_date")
        wait_select_dom.click()
        time.sleep(1)
        wait_select = Select(wait_select_dom)
        wait_select.select_by_index(int(self.days.text()))

        date_dom = wait_select_dom.find_elements(By.TAG_NAME, "option")
        date_dom = [i for i in date_dom][1]
        self.info["date"] = date_dom.text

        time.sleep(1)
        wait_time_dom = self.driver.find_element(By.ID, "play_time")
        wait_time_dom.click()
        time.sleep(1)
        wait_time_select = Select(wait_time_dom)
        wait_time_select.select_by_index(1)

        time_dom = wait_time_dom.find_elements(By.TAG_NAME, "option")
        time_dom = [i for i in time_dom][1]
        self.info["time"] = time_dom.text

        self.driver.execute_script(("function new_open(url, target, feature) {"
                                    "win = new Object();"
                                    "window.uuid_uuid_uuid_uuid_url = url;"
                                    "win.focus = function() {};"
                                    "return win;"
                                    "}"
                                    "window.open = new_open;"))

        go_buy_btn = self.driver.find_element(By.CLASS_NAME, "btn_Booking")
        go_buy_images = go_buy_btn.find_elements(By.TAG_NAME, "img")
        image = [i for i in go_buy_images][0]
        image.click()

        time.sleep(0.5)
        opened_pages = self.driver.window_handles
        self.driver.switch_to.window(opened_pages[1])

        time.sleep(5)
        try:
            self.driver.execute_script("fnBookNoticeShowHide('');")
        except:
            pass
        self.driver.execute_script("document.getElementById('LargeNextBtnLink').click()")
        try:
            self.driver.switch_to.alert.accept()
        except:
            pass

        time.sleep(5)
        js = f"frame = document.getElementById('ifrmSeat').contentWindow.document;" \
             f"txt = frame.getElementsByClassName('validationTxt')[0].getElementsByClassName('lang')[0];" \
             f"txt.title = '请输入防止不当订票的文字，您目前订购的票是第{self.days.text()}天的。';" \
             f"txt.innerHTML = '请输入防止不当订票的文字，您目前订购的票是第{self.days.text()}天的。';" \
             f"ele = frame.getElementsByClassName('btnWrap')[0];" \
             f"ele.innerHTML = ele.innerHTML + '<br><p>您目前订购的票是第{self.days.text()}天的。</p>'"
        self.driver.execute_script(js)

        self.show_msg_box(self.days.text())

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmSeat"))
        [i for i in self.driver.find_element(By.CLASS_NAME, "btnWrap").find_elements(By.TAG_NAME, "a")][1].click()
        self.driver.switch_to.default_content()

        try:
            self.driver.switch_to.alert.accept()
        except:
            pass

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmBookStep"))
        Select(self.driver.find_element(By.NAME, "SeatCount")).select_by_index(1)

        time.sleep(1)
        self.driver.switch_to.default_content()
        self.info["ticket"] = self.driver.find_element(By.ID, "MySelectedSeat").find_element(By.TAG_NAME, "li").text
        self.info["money"] = self.driver.find_element(By.ID, "MyTotalAmt").find_element(By.TAG_NAME, "strong").text
        self.driver.execute_script("document.getElementById('SmallNextBtnLink').click()")

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmBookStep"))
        self.driver.find_element(By.ID, "MemberName").send_keys(self.yourname.text())
        Select(self.driver.find_element(By.ID, "BirYear")).select_by_value(self.biryear.text())
        Select(self.driver.find_element(By.ID, "BirMonth")).select_by_value(self.birmouth.text())
        Select(self.driver.find_element(By.ID, "BirDay")).select_by_value(self.birday.text())
        self.driver.find_element(By.ID, "PhoneNo").send_keys(self.telephone.text())

        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.execute_script("document.getElementById('SmallNextBtnLink').click()")

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmBookStep"))
        [i for i in self.driver.find_elements(By.NAME, "PaymentSelect")][1].click()
        Select(self.driver.find_element(By.ID, "DiscountCardGlobal")).select_by_index(self.xyk_type.currentIndex())
        self.driver.find_element(By.ID, "CardNo1").send_keys(self.card1.text())
        self.driver.find_element(By.ID, "CardNo2").send_keys(self.card2.text())
        self.driver.find_element(By.ID, "CardNo3").send_keys(self.card3.text())
        self.driver.find_element(By.ID, "CardNo4").send_keys(self.card4.text())
        Select(self.driver.find_element(By.ID, "ValidMonth")).select_by_value(self.card_mouth.text())
        Select(self.driver.find_element(By.ID, "ValidYear")).select_by_value("20" + self.card_year.text())

        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.execute_script("document.getElementById('SmallNextBtnLink').click()")

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmBookStep"))
        self.driver.find_element(By.ID, "CancelAgree").click()
        self.driver.find_element(By.ID, "CancelAgree2").click()

        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.execute_script("document.getElementById('SmallNextBtnLink').click()")

        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element(By.NAME, "ifrmBookEnd"))
        self.info["id"] = \
            [i for i in self.driver.find_element(By.CLASS_NAME, "t2").find_elements(By.TAG_NAME, "em")][0].text
        png = self.driver.get_screenshot_as_png()
        now_time = time.strftime("%Y-%m-%d %H-%M-%S")

        png_filename = now_time + ".png"
        path = os.path.join(self.get_desktop(), png_filename)
        with open(path, "wb") as file:
            file.write(png)

        txt_filename = now_time + ".txt"
        text = f"日期: {self.info['date']}\n" \
               f"时间: {self.info['time']}\n" \
               f"座位: {self.info['ticket']}\n" \
               f"花的钱: {self.info['money']}\n" \
               f"ID: {self.info['id']}"
        path = os.path.join(self.get_desktop(), txt_filename)
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)

        self.driver.quit()

        self.url.setDisabled(False)
        self.getticket.setDisabled(False)


class MessageBox(QtWidgets.QDialog, messagebox.Ui_MessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.success = False
        self.buttonBox.accepted.connect(self.on_success_event)

    def on_success_event(self):
        self.success = True

    def wait_success(self):
        while True:
            if self.success:
                return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
