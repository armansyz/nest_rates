import json
import sys
import logging
import argparse

logging.basicConfig(level=logging.INFO)


def read_json():
    """Function that reads json from stdin
    and returns json"""
    try:
        with sys.stdin as f:
            logging.info('\nReading input')
            json_file = json.loads(f.read())
            return json_file
    except AttributeError as e:
        logging.error('\nFailed to read the input')
        raise e
    except json.JSONDecodeError as e:
        logging.error('\nInvalid JSON')
        raise e


def parse_args(args):
    """Function that parses arguments
    """
    parser = argparse.ArgumentParser(add_help=False, description='Given an input as json array '
                                                                 '(each element is a flat dictionary) '
                                                                 'a program that will parse this json, '
                                                                 'and return a nested dictionary of dictionaries '
                                                                 'of arrays, with keys specified in command '
                                                                 'line arguments and the leaf values as arrays '
                                                                 'of flat dictionaries matching appropriate groups')

    parser.add_argument('-h', '--help', action='help', help='Show help message and exit')
    parser.add_argument('nkeys', nargs='*', help='Nesting keys (1..n)')

    return parser.parse_args(args)


def nest_array(json_prm, key):
    """Function that nests an array given a key and returns a dictionary
    """
    return dict((
                    json_prm[y][key],
                    list(dict((k, v) for k, v in x.items() if k != key)
                         for x in json_prm if x[key] == json_prm[y][key])
                )
                for y in range(len(json_prm)))


def nest_json(json_dict, nkeys):
    """Function that nests dictionaries recursively
    """
    if not nkeys:
        return json_dict
    try:
        array = nest_array(json_dict, nkeys[0])
        return {k: nest_json(v, nkeys[1:]) for k, v in array.items()}
    except KeyError as e:
        logging.info("\nSpecified key does not exist")
        raise e


if __name__ == '__main__':
    parser = parse_args(sys.argv[1:])

    json_data = read_json()

    print(json.dumps(nest_json(json_data, parser.nkeys), indent=2))
