import smtplib
import time
from email.mime.text import MIMEText
import sendMail as sm

if __name__ == '__main__':
    # send list
    sm.mailto_list = os.getenv("MAILTO_LIST")
    sm.mail_title = 'Hey subject'
    sm.mail_content = '尊重的客户：' \
                   '         执行时间：'+time.asctime() \
                   '         任务状态：任务执行成功！' \
                   '                                   感谢使用！'
    mm = sm.Mailer(mailto_list, mail_title, mail_content)
    res = mm.sendMail()




