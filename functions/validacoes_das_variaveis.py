def validar_variavel_inteira(variavel, descricao):
    """

    :param variavel: Variável a ser validada
    :return: Mensagem de erro
    """
    if variavel == "":
        print("Especifique um número para '",
              descricao, "'.")
        quit()
    if all(i in "0123456789-" for i in variavel) == True \
        and any(i in "0123456789" for i in variavel) == True \
        and variavel.count("-") <= 1 \
        and variavel.find("-") <= 0:
        variavel = int(variavel)

        return variavel
    else:
        print("Especifique um número para '",
              descricao, "'.")
        quit()

def validar_variavel_decimal(variavel, descricao):
    """

    :param variavel: Variável a ser validada
    :return: Mensagem de erro
    """
    if variavel == "":
        print("Especifique um número para '",
              descricao, "'.")
        quit()
    if all(i in "0123456789.-" for i in variavel) == True \
        and any(i in "0123456789" for i in variavel) == True \
        and variavel.count(".") <= 1 \
        and variavel.count("-") <= 1 \
        and variavel.find("-") <= 0:
        variavel = float(variavel)

        return variavel
    else:
        print("Especifique um número para '",
              descricao, "'.")
        quit()

def validar_variavel_inteira_nao_negativa(variavel, descricao):
    """

    :param variavel: Variável a ser validada
    :return: Mensagem de erro
    """
    if variavel == "":
        print("Especifique um número para '",
              descricao, "'.")
        quit()
    if all(i in "0123456789" for i in variavel) == True \
        and any(i in "0123456789" for i in variavel) == True:
        variavel = int(variavel)

        return variavel
    else:
        print("Especifique um número para '",
              descricao, "'.")
        quit()

def validar_variavel_decimal_nao_negativa(variavel):
    """

    :param variavel: Variável a ser validada
    :return: Mensagem de erro
    """
    if variavel == "":
        print("Especifique um número para '",
              descricao, "'.")
        quit()
    if all(i in "0123456789." for i in variavel) == True \
        and any(i in "0123456789" for i in variavel) == True \
        and variavel.count(".") <= 1:
        variavel = float(variavel)

        return variavel
    else:
        print("Especifique um número para '",
              descricao, "'.")
        quit()