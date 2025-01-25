from stars import Statistics


def main():
    stars = Statistics(init_numbers=[12, 37, 6])

    while True:
        new_number = input('Add number to the set ("exit" to exit): ')
        if new_number != 'exit':
            stars.add_number(int(new_number))
        else:
            break

    stars.display_numbers()
    stars.print_statistics()
    

if __name__ == '__main__':
    main()