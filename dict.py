def main():
    # empty dict
    d = {} 
    d = dict()
    print(f'{d=}')

    # create key value in dict
    d['a'] = 11
    d['b'] = 22
    print(f'{d=}')

    # dict with multiple elements
    d = {'a': 1, 'b': 2, 'c': 3}
    print(f'{d=}')

    # get -> get value from dict according to key
    get_ = d.get('a')
    print(f'{get_=} {d=}')
    get_ = d.get('d')   # None, because there is no key d
    print(f'{get_=} {d=}')
    get_ = d.get('d', 'no_key')   # no_key, because there is no key d
    print(f'{get_=} {d=}')

    # pop -> get value from dict according to key, but key and value are removed 
    pop_ = d.pop('a')
    print(f'{pop_=} {d=}')
    #pop_ = d.pop('a')   # KeyError exception, because there is no a key in dict
    pop_ = d.pop('a', 'no_key') # no_key, because there is no key d
    print(f'{pop_=} {d=}')


if __name__ == "__main__":
    main()