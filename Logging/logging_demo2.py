import logging
import Logging.custom_logger as cl


class LoggingDemo2():
    log = cl.customLogger(logging.DEBUG)

    def method1(self):
        self.log.debug('debug message')
        self.log.info('info message')
        self.log.warning('warn message')
        self.log.error('error message')
        self.log.critical('critical message')

    # it will create all logging functionalities with it's method instance ( Like Method name will be used as logger name, created method name as file name,etc)
    def method2(self):
        m2Log = cl.customLogger(logging.INFO)
        m2Log.debug('debug message')
        m2Log.info('info message')
        m2Log.warning('warn message')
        m2Log.error('error message')
        m2Log.critical('critical message')

    # it will assign same functionalities like method2
    def method3(self):
        m3Log = cl.customLogger(logging.WARNING)
        m3Log.debug('debug message')
        m3Log.info('info message')
        m3Log.warning('warn message')
        m3Log.error('error message')
        m3Log.critical('critical message')


demo = LoggingDemo2()
demo.method1()
demo.method2()
demo.method3()