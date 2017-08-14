from .blends.pick_n import pick_n
from .hashes.hash import Md5, HMacMd5


SEPARATORS = '.,|+/-$%!&*_=:'

COMMON_PASS_FILE = 'hash_blender/data/top1000-passwords.txt'

HASH_CLASSES = [Md5()]
HASH_CLASSES.extend([HMacMd5(passwd.strip()) for passwd in file(COMMON_PASS_FILE)])


def get_hash_functions(configured_hash_string):
    for hash_class in HASH_CLASSES:
        if hash_class.is_of_type(configured_hash_string):
            yield hash_class


def main(user_inputs, configured_hash_string, verbose=False):
    last_value = None

    for hash_class in get_hash_functions(configured_hash_string):
        for inputs_to_blend in pick_n(user_inputs):
            for separator in SEPARATORS:
                string_to_hash = separator.join(inputs_to_blend)

                # Avoid some duplicates, at least when they are consecutive
                if string_to_hash == last_value:
                    continue

                last_value = string_to_hash

                _hash = hash_class.hash(string_to_hash)

                if _hash == configured_hash_string:
                    print('%s("%s") == %s' % (hash_class.get_name(),
                                              string_to_hash,
                                              configured_hash_string))
                    print('Success!')
                else:
                    if verbose:
                        print('%s("%s") != %s' % (hash_class.get_name(),
                                                  string_to_hash,
                                                  configured_hash_string))
