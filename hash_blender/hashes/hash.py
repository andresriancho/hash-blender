import hashlib
import hmac


class Md5(object):
    def get_name(self):
        return 'md5'

    def hash(self, blend):
        m = hashlib.md5()
        m.update(blend)
        return m.hexdigest()

    def is_of_type(self, str_a):
        return len(str_a) == 32


class HMacMd5(object):
    def __init__(self, secret):
        self.secret = secret

    def get_name(self):
        return 'hmac-md5 with secret: "%s" ' % self.secret

    def hash(self, blend):
        m = hmac.new(self.secret)
        m.update(blend)
        return m.hexdigest()

    def is_of_type(self, str_a):
        return len(str_a) == 32
