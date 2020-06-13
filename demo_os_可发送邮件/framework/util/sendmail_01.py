import smtplib
from  email.mime.text import MIMEText
from  email.header import Header
from email.mime.multipart import MIMEMultipart
import zmail,time
def sendmail(sender,password,receiver,mail_subject,file_path,):
    '''
    :param sender:  是发送邮箱
    :param password: 注意，不是登录密码，这是邮件系统的授权码
    :param receiver:  接收邮箱
    :param mail_subject: 邮件标题
    :param file_path:
    :return:
    '''
    sender = sender
    password = password
    time.sleep(2)
    mail_content = {
        "subject": mail_subject,
        # "content_html":content_html,
        "content_html": zmail.read_html(file_path),
        "attachments": file_path  # 附件
    }

    try:
        # 发件人邮箱和密码
        server = zmail.server(sender, password)
        # 发送邮件--（收件人，邮件内容）
        server.send_mail(receiver, mail_content)
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error:无法发送邮件')


