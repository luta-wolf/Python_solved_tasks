# form_data = {}

# try:
# 	name = form_data['name']
# except KeyError:
# 	print('error')
# 	raise
# finally:
# 	print('finally')


# class Foo:
# 	var = 1

# a = Foo()
# b = Foo()

# a.var += 1
# print(b.var)


# a = 8
# b = 12.222
# print(a/b)

# def foo() -> dict:
# 	return {i: j for i in range(10) if (j := pow(i, 2)) and j & 1}


# print(foo())

# def foo2() -> dict:
# 	d = {}
# 	for i in range(1, 10 , 2):
# 		d[i] = i ** 2
# 	return d

# print(foo2())

# def foo3() -> dict:
# 	return dict(map(lambda x: pow(x, 2), range(1, 10, 2)))

# print(foo3())



# def foo2() -> dict:
# 	d = {}
# 	for i in range(10):
# 		({})
# 	return d

# def foo (db_connection: connection) -> None:
# 	with db_connection.cursor() as cursor:
# 		cursor.execute("SELECT 1;")
# 		cursor.fetchone()


def foo(basic_auth: tuple[str, str]) -> str:
	if (
		not isinstance(basic_auth, tuple)
		or len(basic_auth) != 2
		or any(not isinstance(item, str | bytes) for item in basic_auth)
	):
		raise ValueError(
			"`basic_auth` must be a 2-tuple of str/bytes (username, password)"
		)
	basic_auth_value = base64.b64encode(
		b":".join(map(to_bytes, basic_auth))
	).decode()
	return f'Basic {basic_auth_value}'
