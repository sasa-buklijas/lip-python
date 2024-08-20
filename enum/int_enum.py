import enum


class Int_Enum(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


def main():
    print(f'Addition is: {Int_Enum.ONE + Int_Enum.TWO}')

    print(f'Comparison is: {Int_Enum.ONE < Int_Enum.TWO}')
    print(f'Comparison is: {Int_Enum.ONE > Int_Enum.TWO}')


if __name__ == "__main__":
    main()