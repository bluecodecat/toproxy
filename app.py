import tornado
import logging
import toproxy.proxy as proxy


proxy.logger.setLevel(logging.ERROR)
proxy.base_auth_user = None
proxy.base_auth_passwd = None
proxy.white_iplist = []


proxy.run_proxy(8087, start_ioloop=False)
tornado.ioloop.IOLoop.instance().start()

#if self.request.uri.endswith('media.tumblr.com:443'):
#    self.request.uri = '127.0.0.1:25443'
