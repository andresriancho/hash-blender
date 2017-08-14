import hashlib


class Md5(object):
    @staticmethod
    def get_name():
        return 'md5'

    @staticmethod
    def hash(blend):
        m = hashlib.md5()
        m.update(blend)
        return m.hexdigest()

    @staticmethod
    def is_md5(str_a):
        return len(str_a) == 32
