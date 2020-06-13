from HTMLTestRunner import  HTMLTestRunner
from demo_os_可发送邮件.framework.cases import casesdemo,baidu,youdao,Simple_Element_Test01

import  time

import unittest

def test_report():
    suite=unittest.TestSuite()

    # testcase=unittest.TestLoader().loadTestsFromModule(baidu)

    suite.addTests([unittest.TestLoader().loadTestsFromTestCase(casesdemo.TestAdd),
                   unittest.TestLoader().loadTestsFromTestCase(baidu.Baidu),
                    unittest.TestLoader().loadTestsFromTestCase(youdao.Youdao),
                    # unittest.TestLoader().loadTestsFromModule(Simple_Element_Test01),
           ] )

    now=time.strftime('%Y-%m-%d %H_%M_%S')#获取当前时间
    filename='./report/'+now +'_report.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title=u"系统测试报告",description=u'测试用例执行情况')
    runner.run(suite)
if __name__=='__main__':
    unittest.main()