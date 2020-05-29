# -*-coding:utf-8-*-

import smtplib
from email.mime.text import MIMEText
from datetime import datetime

def sendEmail():
    # 设置发件服务器地址
    host = 'smtp.qq.com'
    # 发件服务器端口
    port = 465
    sender = '2370951811@qq.com'              # 发送方邮箱
    pwd = ''                # 填入发送方邮箱的授权码
    # 设置邮件接收人，可以是QQ邮箱
    receiver = '1538779315@qq.com'            # 收件人邮箱
    # receiver = ['344605835@qq.com']         # 收件人邮箱
    weather_text = '123'
    # 设置邮件正文，这里是支持HTML的
    body = '<h1>%s</h1><p>zhongfs</p>'.format(weather_text)
    # 设置正文为符合邮件格式的HTML内容
    msg = MIMEText(body, 'html')
    # 设置邮件标题
    msg['subject'] = '各地天气预报详情'
    # 设置发送人
    msg['from'] = sender
    # 设置接收人
    msg['to'] = ','.join(receiver)
    server = smtplib.SMTP_SSL(host, port)
    server.login(sender, pwd)

    # 登陆邮箱
    server.sendmail(sender,msg['to'].split(','),msg.as_string())
    # 发送邮件！
    server.quit()



if __name__ == '__main__':
    sendEmail()

