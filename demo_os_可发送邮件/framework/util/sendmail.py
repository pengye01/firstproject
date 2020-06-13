import smtplib
from  email.mime.text import MIMEText
from  email.header import Header
from email.mime.multipart import MIMEMultipart

def sendmail(sender,password,receiver,mail_subject,file_path,filename):
    '''

    :param sender:  是发送邮箱
    :param password: 注意，不是登录密码，这是邮件系统的授权码
    :param receiver:  接收邮箱
    :param mail_subject: 邮件标题
    :param file_path:
    :param filename:
    :return:
    '''
    SMTPServer = "smtp.163.com"
    msg=MIMEMultipart()
    msg['Subject']=Header(mail_subject,'utf-8')
    msg["From"]=sender
    msg['to']=receiver
    #构造附件1，传递当前目录下的test.txt文件
    att1=MIMEText(open(file_path,'rb').read(),'base64','utf-8')
    att1["Content-Type"]='application/octet-stream'
    att1['Content-Disposition']='attachment;filename="%s"'%filename
    #这里的filename可以任意写，写什么名字，邮件中显示什么名字
    #Content-Disposition 是MIME协议的扩展，MIME协议指示MIME用户代理如何显示附加的文件
    #Content-Disposition 其实可以控制用户请求所得的内容存为一个文件的时候提供一个默认文件名。
    msg.attach(att1)
    try:
        smtp=smtplib.SMTP()
        smtp.connect(SMTPServer)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error:无法发送邮件')


