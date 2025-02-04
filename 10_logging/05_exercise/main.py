from functions import count_characters, most_and_least_common

def main():
    count_characters("Hello, World!")
    count_characters("Look at me go, ma!")

    most_and_least_common([1, 1, 2, 2])
    most_and_least_common([2, 2, 1, 1, 5, 6, 1, 4, 3, 9, 7, 5, 'g'])

if __name__ == '__main__':
    main()