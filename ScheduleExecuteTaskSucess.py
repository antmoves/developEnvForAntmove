import os
import smtplib
import time
from email.mime.text import MIMEText
import sendMail as sm

if __name__ == '__main__':
    # send list
    sm.mailto_list = [os.getenv("MAILTO_LIST")]
    sm.mail_title = 'Hey subject'
    sm.mail_content = '尊重的客户：\r' \
                   '         执行时间：'+time.asctime()+'         \r' \
                   '         任务状态：任务执行成功\r' \
                   '                                   感谢使用\r'
    mm = sm.Mailer(sm.mailto_list, sm.mail_title, sm.mail_content)
    res = mm.sendMail()




