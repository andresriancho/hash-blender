import json
import sys

from hash_blender.main import main


if __name__ == '__main__':
    try:
        config_filename = sys.argv[1]
    except IndexError:
        print('Usage: ./hash-blender.py config.json')
        sys.exit(1)

    try:
        config = json.loads(file(config_filename).read())
    except Exception, e:
        print(e)
        sys.exit(1)

    try:
        user_inputs = config['values']
    except:
        print('config.json needs to have "values" keys')
        sys.exit(2)

    try:
        configured_hash_string = config['hash']['string']
    except:
        print('config.json needs to have "values" and "string" keys')
        sys.exit(2)

    try:
        verbose = config['verbose']
    except:
        verbose = False

    main(user_inputs=user_inputs,
         configured_hash_string=configured_hash_string,
         verbose=verbose)
