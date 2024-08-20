import enum

# since Python 3.11
class Str_Enum(enum.StrEnum):
    ONE = '1'
    TWO = '2'
    THREE = '3'

def main():
    print(f'Comparison is: {Str_Enum.ONE == "1"}')
    print(f'Comparison is: {Str_Enum.ONE != "1"}')

    print(f'Comparison is: {Str_Enum.ONE=}')
    print(f'Comparison is: {Str_Enum.ONE.value=}')
    # do net see difference from just enum.Enum


if __name__ == "__main__":
    main()