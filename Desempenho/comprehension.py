import time


def for_sem_comprehension() -> float:
	start_time = time.time()

	L = []
	for i in range(1, 10000):
		if i % 3 == 0:
			L.append(i)

	return time.time() - start_time


def for_com_comprehension() -> float:
	start_time = time.time()

	L = [i for i in range(1, 10000) if i % 3 == 0]

	return time.time() - start_time


def test_comprehension():
	i, sem_comprehension, com_comprehension = 0, 0, 0

	while 1:
		if for_sem_comprehension() < for_com_comprehension():
			i += 1
			sem_comprehension += 1
		else:
			i += 1
			com_comprehension += 1

		if i == 6 and sem_comprehension > com_comprehension:

			print('SEM comprehension teve mais performance em ' + sem_comprehension.__str__() + ' casos de ' + (
					i - 1).__str__() + ' testes realizados')
			print('Testes rodados:', i, '| ', 'Manual:', sem_comprehension, 'Nativa:', com_comprehension)
			break

		elif i == 6 and sem_comprehension < com_comprehension:

			print('COM comprehension teve mais performance em ' + com_comprehension.__str__() + ' casos de ' + (
					i - 1).__str__() + ' testes realizados')
			print('Testes rodados:', i, '| ', 'Manual:', sem_comprehension, 'Nativa:', com_comprehension)
			break


test_comprehension()
