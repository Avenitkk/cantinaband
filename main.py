import os, time, sys;from colorama import Fore, Back, Style, init

init()

cantinaBand = ("  ____            _   _               ____                  _", " / ___|__ _ _ __ | |_(_)_ __   __ _  | __ )  __ _ _ __   __| |", "| |   / _` | '_ \| __| | '_ \ / _` | |  _ \ / _` | '_ \ / _` |", "| |__| (_| | | | | |_| | | | | (_| | | |_) | (_| | | | | (_| |", " \____\__,_|_| |_|\__|_|_| |_|\__,_| |____/ \__,_|_| |_|\__,_|")

for i in range(5):print(Fore.RED + cantinaBand[i]);time.sleep(0.1)
try:input('\nНажмите Enter, чтобы продолжить...')
except KeyboardInterrupt:close()
except EOFError:close()
print(Style.RESET_ALL);os.system('cls')

def close():os.system('cls');print(Fore.RED + 'Закрытие программы...' + Style.RESET_ALL);sys.exit()

run = True
actionName = 'cantinaband_terminal'
network = False

while run:
	if network == True: actionName = 'cantinaband_terminal/network'
	try:command = input(Fore.GREEN + actionName + Fore.BLUE + '>> ' + Style.RESET_ALL)
	except KeyboardInterrupt:close()
	except EOFError:close()

	file = open('history.txt', 'a')
	if command == '':file.write('Тут была пустая строка\n')
	else:file.write(command + '\n');file.close()

	#basic commands
	if command == 'exit':close()
	elif command == 'contacs':print('Telegram - @kurlandxxx')
	elif command == 'cls' or command == 'clear':os.system('cls')
	elif command == 'history':file = open('history.txt', 'r');print(file.read());file.close()
	#elif command == 'cmd':os.system('cmd')

	#network commands
	elif command == 'network':network = True
	elif command == 'ping' and network == True:ip = input('ip or domain: ');os.system('ping ' + ip)
	elif command == 'ipconfig' and network == True:os.system('ipconfig')
	elif command == 'ifconfig' and network == True:os.system('ifconfig')

	#exit from all types of operations
	elif command == '..': network = False; actionName = 'cantinaband_terminal'

	#help
	elif command == 'help':print('exit - закрыть программу\ncontacs - контакты\ncls или clear - очистить экран\nhistory - история команд\nnetwork - режим network\n.. - выйти из всех режимов')

	else:print('?')