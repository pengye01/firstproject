from demo_os_可发送邮件.framework.util.newestfile import newst_file
from demo_os_可发送邮件.framework.util.report import test_report
# from demo_os_可发送邮件.framework.util.sendmail import sendmail
import time
from demo_os_可发送邮件.framework.util.sendmail_01 import sendmail
if __name__=='__main__':
    test_report()
    time.sleep(2)
    file_path,filename=newst_file('.\\report')

    #把最新的测试报告做为附件，发送邮件
    sender = "pengye914@163.com"
    password="FVBPETOIXPOBBFFX"
    receiver="974720373@qq.com"

    # sendmail(sender,password,receiver,"系统测试报告",file_path,filename)
    sendmail(sender,password,receiver,u"系统测试报告",file_path)
