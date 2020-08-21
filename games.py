# Guessing Game
# win_num = 7
# guess_count = 1
# guess_limit = 3
# while guess_count <= guess_limit:
#     guess_num = int(input("Guess: "))
#     if guess_num == win_num:
#         print('You won!')
#         break
#     if guess_count < 3:
#         print("Try again!")
#     guess_count += 1
# else:
#     print('Sorry, you failed!')

# Car Game
car_started = False
while True:
    command = input('> ').lower()
    if command == 'help':
        msg = 'Start - to start the car\nStop - to stop the car\nQuit - to quit the car\n'
        print(msg)
    elif command == 'start':
        if car_started:
            msg = 'Car already started!\n'
            print(msg)
        else:
            msg = 'Car started .... ready to go.\n'
            car_started = True
            print(msg)
    # elif command == 'start' and not car_started:
    #     msg = 'Car started .... ready to go.\n'
    #     car_started = True
    #     print(msg)
    # elif command == 'start' and car_started:
    #     msg = 'Car already started!\n'
    #     print(msg)
    elif command == 'stop':
        if car_started:
            msg = 'Car stopped.\n'
            car_started = False
            print(msg)
        else:
            msg = 'Car already stopped.\n'
            print(msg)
    # elif command == 'stop' and car_started:
    #     msg = 'Car stopped.\n'
    #     car_started = False
    #     print(msg)
    # elif command == 'stop' and not car_started:
    #     msg = 'Car already stopped.\n'
    #     print(msg)
    elif command == 'quit':
        print('See you later!')
        break
    else:
        msg = "Oops! I don't understand that.\n"
        print(msg)

