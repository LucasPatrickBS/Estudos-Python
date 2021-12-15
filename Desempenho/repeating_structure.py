import time


def for_sem_mult_assignments() -> float:
	start_time = time.time()

	for i in range(1, 10000):
		a = 'um'
		b = 1
		c = 'um'
		d = 1
		e = 'um'
		f = 1
		g = 'um'
		h = 1
		i = 'um'
		j = 1
		k = 'um'
		l = 1
		m = 'um'
		n = 1
		o = 'um'
		p = 1
		q = 'um'
		r = 1
		s = 'um'
		t = 1
		u = 'um'
		v = 1
		w = 'um'
		x = 1
		y = 'um'
		z = 1

	return time.time() - start_time


def for_com_mult_assignments() -> float:
	start_time = time.time()

	for i in range(1, 10000):
		a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = \
			'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1, 'um', 1

	return time.time() - start_time


def test_mult_assignments():
	i, sem_mult_assignments, com_mult_assignments = 0, 0, 0

	while 1:
		if for_sem_mult_assignments() < for_com_mult_assignments():
			i += 1
			sem_mult_assignments += 1
		else:
			i += 1
			com_mult_assignments += 1

		if i == 6 and sem_mult_assignments > com_mult_assignments:

			print('SEM mult assignments teve mais performance em ' + sem_mult_assignments.__str__() + ' casos de ' + (
					i - 1).__str__() + ' testes realizados')
			print('Testes rodados:', i, '| ', 'SEM:', sem_mult_assignments, 'COM:', com_mult_assignments)
			break

		elif i == 6 and sem_mult_assignments < com_mult_assignments:

			print('COM mult assignments teve mais performance em ' + com_mult_assignments.__str__() + ' casos de ' + (
					i - 1).__str__() + ' testes realizados')
			print('Testes rodados:', i, '| ', 'SEM:', sem_mult_assignments, 'COM:', com_mult_assignments)
			break


test_mult_assignments()
