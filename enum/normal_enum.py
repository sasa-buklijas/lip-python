import enum


class NormalEnum(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3

class NormalEnumStr(enum.Enum):
    ONE = '1'
    TWO = '2'
    THREE = '3'

def main():
    # TypeError: unsupported operand type(s) for +: 'NormalEnum' and 'NormalEnum'
    #print(f'Addition is: {NormalEnum.ONE + NormalEnum.TWO}')

    #TypeError: '<' not supported between instances of 'NormalEnum' and 'NormalEnum' 
    #print(f'Comparison is: {NormalEnum.ONE < NormalEnum.TWO}')
    
    print(f'Comparison is: {NormalEnum.ONE == NormalEnum.ONE}')
    print(f'Comparison is: {NormalEnum.ONE != NormalEnum.ONE}')

    print(f'Comparison is: {NormalEnumStr.ONE == "1"}')
    print(f'Comparison is: {NormalEnumStr.ONE != "1"}')

    print(f'Comparison is: {NormalEnumStr.ONE=}')
    print(f'Comparison is: {NormalEnumStr.ONE.value=}')


if __name__ == "__main__":
    main()