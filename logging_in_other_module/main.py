import logging
import other_modul

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s:%(msecs)03d:%(filename)s:%(lineno)5d:%(levelname)10s:%(name)s:%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler()
        ]
    )

    logging.debug('Hello World !')

if __name__ == '__main__':
    main()