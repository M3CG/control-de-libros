import re


def validar_titulo(titulo):
    return bool(re.match(r"^.{1,40}$", titulo))


def validar_cantidad(cantidad):
    return bool(re.match(r"^\d{1,4}$", cantidad) and int(cantidad) >= 1)


def validar_precio(precio):
    return bool(re.match(r"^\d{1,5}\.\d{2}$", precio) and float(precio) > 0)


def validar_fecha(fecha):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", fecha))


def validar_autor(autor):
    return bool(re.match(r"^(([A-Z]{1}[a-z]+\.?)|([A-Z]{1}\.))(\s(([A-Z]{1}[a-z]+\.?)|([A-Z]{1}\.)))+$", autor) and re.match(r"^.{0,30}$", autor))


def validar_isbn(isbn):
    if bool(re.match(r"^(978|979)-\d{1,5}-\d{1,7}-\d{1,6}-\d{1}$", isbn) and len(isbn) == 17):
        digitos = re.sub("-", "", isbn)
        control = sum(int(i) for i in digitos[::2]) + sum(int(i)*3 for i in digitos[1::2])
        return control % 10 == 0
    else:
        return False

# def isbn_validar(isbn):
#     if bool(re.match(r"^(978|979)-\d{1,5}-\d{1,7}-\d{1,6}-\d{1}$", isbn) and len(isbn) == 17):
#         digitos = re.sub("-", "", isbn)
#         par_3 = digitos[1:len(digitos)-1:2]
#         impar = digitos[0:len(digitos)-1:2]
#         par_3 = [int(i)*3 for i in par_3]
#         impar = [int(i) for i in impar]
#         control = (sum(par_3) + sum(impar)) % 10
#         if control != 0:
#             control = 10 - control
#         return str(control) == isbn[len(isbn)-1]
