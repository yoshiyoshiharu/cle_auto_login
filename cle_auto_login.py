from selenium import webdriver
from time import sleep

USERID = 'ID'
PASSWORD = 'パスワード'

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver\chromedriver.exe')

    error_flg = False
    driver.get('https://www.cle.osaka-u.ac.jp/webapps/login/')
    sleep(1)
try:
    driver.find_element_by_id('loginsaml').click()
    sleep(1)
except Exception:
    error_flg = True
    print('ログインボタン押下ときにエラーが発生しました。')

try:
    driver.find_element_by_id('USER_ID').send_keys(USERID)
    driver.find_element_by_id('USER_PASSWORD').send_keys(PASSWORD)
    driver.find_element_by_class_name('Btn1Def').click()
except Exception:
    error_flg = True
    print('ログイン時にエラーが発生しました。')
