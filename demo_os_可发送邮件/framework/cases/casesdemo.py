
import unittest
from demo_os_可发送邮件.framework.util.cal import  Cal
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls)->None:
        cls.cal=Cal()
        print('初始化')
    @classmethod
    def tearDownClass(cls)->None:
        print('销毁数据')
    def test_add01(self):

        result=self.cal.add(1,1)
        self.assertEqual(result,2)
    # @unittest.skip('强制跳过')
    # @unittest.skipIf(4<2,'强制跳过')
    # skipunless
    # @unittest.skipUnless(4<2,'强制跳过')  # 4<2为False，跳过
    # @unittest.expectedFailure
    def test_add02(self):
        result=self.cal.add(1.123,3.1415)
        self.assertEqual(result,4.2645)
    def test_add03(self):
        result=self.cal.add(-1,6)
        self.assertEqual(result,5)
import  HTMLTestRunner
if __name__=='__main__':
    # suite=unittest.TestSuite()
    # testcase=unittest.TestLoader().loadTestsFromTestCase(TestAdd)
    # suite.addTest(testcase)
    # f=open('report.html','wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=f,title='自动化测试报告',description='测试报告详情')
    # runner.run(suite)
    unittest.main()