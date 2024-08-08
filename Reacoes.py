from scipy.optimize import fsolve
tamanho = float(input("Digite o tamanho da viga (Em metros [m]):"))

def sis_pos(a, # Variável que determina a angulação da reta
            x, # Variável que irão as posições (Final - Inicial)
            b, # Variável que recebe força inicial
            c): # variável que recebe força final
  return a*x + b - c

def ponto_0(ResSisPos,
            ForcaI):
  return -ForcaI/ResSisPos

def Apoios():
    tipo = input("Quais serão os tipos de apoio?\n" +
                 "Tipo 1: Rolete ou Pino;\n" +
                 "Tipo 2: Engaste.\n").upper()
    arr_apoios = []
    while tipo not in ["TIPO 1", "TIPO 2"]:
      print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'Tipo 1' ou 'Tipo 2'.\n")
      tipo = input("Quais serão os tipos de apoio?\n" +
                 "Tipo 1: Rolete ou Pino;\n" +
                 "Tipo 2: Engaste.\n").upper()
    if tipo == "TIPO 1":
            W1 = input("Qual será seu primeiro apoio?\nDigite Rolete ou Pino.\n").upper()
            if W1 == "ROLETE":
                P1 = float(input("Digite a posição do primeiro apoio em metros [m]:\n"))
                while P1 > tamanho:
                  P1 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                arr_apoios.append(("rol", P1))
            elif W1 == "PINO":
                P1 = float(input("Digite a posição do primeiro apoio em metros [m]:\n"))
                while P1 > tamanho:
                  P1 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                arr_apoios.append(("pin", P1))
            else:
                print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO, 'ROLETE' ou 'PINO'.\n")
                while W1 != "ROLETE" and W1 != "PINO":
                    W1 = input("Qual será o apoio?\nDigite Rolete ou Pino.\n").upper()
                    if W1 == "ROLETE":
                      P1 = float(input("Digite a posição do primeiro apoio em metros [m]:\n"))
                      while P1 > tamanho:
                       P1 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                      arr_apoios.append(("rol", P1))
                    elif W1 == "PINO":
                      P1 = float(input("Digite a posição do primeiro apoio em metros [m]:\n"))
                      while P1 > tamanho:
                       P1 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                      arr_apoios.append(("pin", P1))
            W2 = input("Qual será seu segundo apoio?\nDigite Rolete ou Pino.\n").upper()

            if W2 == "ROLETE":
               P2 = float(input("Digite a posição do segundo apoio em metros [m]:\n"))
               while P2 > tamanho or P2 == P1:
                if P2 > tamanho:
                    P2 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                else:
                    P2 = float(input("A posição do segundo apoio não pode ser igual à do primeiro apoio, insira um valor diferente:\n"))
               arr_apoios.append(("rol", P2))
            elif W2 == "PINO":
               P2 = float(input("Digite a posição do segundo apoio em metros [m]:\n"))
               while P2 > tamanho or P2 == P1:
                if P2 > tamanho:
                    P2 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                else:
                    P2 = float(input("A posição do segundo apoio não pode ser igual à do primeiro apoio, insira um valor diferente:\n"))
               arr_apoios.append(("pin", P2))
            else:
                print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'ROLETE' ou 'PINO'.\n")
                while W2 != "ROLETE" and W2 != "PINO":
                    W2 = input("Qual será o apoio?\nDigite Rolete ou Pino.\n").upper()
                    if W2 == "ROLETE":
                      P2 = float(input("Digite a posição do segundo apoio em metros [m]:\n"))
                      while P2 > tamanho or P2 == P1:
                        if P2 > tamanho:
                            P2 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                        else:
                            P2 = float(input("A posição do segundo apoio não pode ser igual à do primeiro apoio, insira um valor diferente:\n"))
                      arr_apoios.append(("rol", P2))
                    elif W2 == "PINO":
                      P2 = float(input("Digite a posição do segundo apoio em metros [m]:\n"))
                      while P2 > tamanho or P2 == P1:
                        if P2 > tamanho:
                            P2 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                        else:
                            P2 = float(input("A posição do segundo apoio não pode ser igual à do primeiro apoio, insira um valor diferente:\n"))
                      arr_apoios.append(("pin", P2))
    elif tipo == "TIPO 2":
        inicial = 0
        final = tamanho
        P = input("O Engaste só pode estar nas extremidades escolha a posição: inicial ou final.\n").upper()
        if P == "INICIAL":
            arr_apoios.append(("eng", inicial))
        elif P == "FINAL":
            arr_apoios.append(("eng", final))
        else:
            while P != "INICIAL" and P != "FINAL":
                print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'INICIAL' ou 'FINAL'.\n")
                P = input("O Engaste só pode estar nas extremidades escolha a posição: inicial ou final.\n").upper()
                if P == "INICIAL":
                    arr_apoios.append(("eng", inicial))
                elif P == "FINAL":
                    arr_apoios.append(("eng", final))
    #print(arr_apoios)
    return arr_apoios

apoios = Apoios()

def cargas_distribuidas(Pi, # Posição Inicial 0
                        Pf, # Posição Final 10
                        Fi, # Força Inicial 3
                        Ff, # Força Final 32
                        Si, # Sentido Inicial P
                        Sf, # Sentido Final P
                        Vetor_Forca): # Vetor das forças

  if (Si == Sf): # Se não atravessa o eixo

    if (Pf > Pi): # Se a posição final for maior que a posição inicial

      if (Ff == Fi): # Caso do retângulo
        ForcaTotal = (Pf-Pi)*Fi # Cálculo da Força Total
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Posicao = Pi + ((Pf-Pi)/2) # Cálculo da Posição da Força
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Fi > Ff or Ff > Fi) and (Ff == 0): # Caso Triângulo com base na esquerda
        ForcaTotal = Fi*(Pf-Pi)/2 # Cálculo da Força Total
        Posicao = Pi + (Pf-Pi)*1/3 # Cálculo da Posição da Força
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Ff > Fi or Fi > Ff) and (Fi == 0): # Caso Triângulo com base na direita
        ForcaTotal = Ff*(Pf-Pi)/2 # Cálculo da Força Total
        Posicao = Pi + (Pf-Pi)*2/3 # Cálculo da Posição da Força
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Fi > Ff): # Caso do trapézio com base maior a esquerda
        Forca_Tri = ((Fi - Ff) * (Pf-Pi))/2 # Cálculo da Força Parcial do Triângulo
        Forca_Ret = (Pf-Pi)*Ff # Cálculo da Força Parcial do Retângulo
        Pos_Tri = Pi + (Pf-Pi)*1/3 # Cálculo da Posição da Força
        Pos_Ret = Pi + ((Pf-Pi)/2) # Cálculo da Posição da Força
        if (Si == 2):
          Forca_Tri == -1*Forca_Tri # Caso o sentido seja negativo
          Forca_Ret == -1*Forca_Ret # Caso o sentido seja negativo
        Vetor_Forca.append([Forca_Tri, Pos_Tri])
        Vetor_Forca.append([Forca_Ret, Pos_Ret])

      elif (Ff > Fi): # Caso do trapézio com base maior a direita
        Forca_Tri = ((Ff-Fi)*(Pf-Pi))/2 # Cálculo da Força Parcial do Triângulo
        Forca_Ret = (Pf-Pi)*Fi # Cálculo da Força Parcial do Retângulo
        Pos_Tri = Pi + (Pf-Pi)*2/3 # Cálculo da Posição da Força
        Pos_Ret = Pi + ((Pf-Pi)/2) # Cálculo da Posição da Força
        if (Si == 2):
          Forca_Tri == -1*Forca_Tri # Caso o sentido seja negativo
          Forca_Ret == -1*Forca_Ret # Caso o sentido seja negativo
        Vetor_Forca.append([Forca_Tri, Pos_Tri])
        Vetor_Forca.append([Forca_Ret, Pos_Ret])

    else: # Se a posição inicial for maior que a final

      if (Ff == Fi): # Caso do retângulo
        ForcaTotal = (Pi-Pf)*Fi # Cálculo da Força Total
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Posicao = Pf + ((Pi-Pf)/2) # Cálculo da Posição da Força
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Fi > Ff or Ff > Fi) and (Ff == 0): # Caso do triângulo com base na direita
        ForcaTotal = Fi*(Pi-Pf)/2 # Cálculo da Força Total
        Posicao = Pf + (Pi-Pf)*2/3 # Cálculo da Posição da Força
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Ff > Fi or Fi > Ff) and (Fi == 0): # Caso do triângulo com base na esquerda
        ForcaTotal = Ff*(Pi-Pf)/2 # Cálculo da Força Total
        Posicao = Pf + (Pi-Pf)*1/3 # Cálculo da Posição da Força
        if (Si == 2):
          ForcaTotal == -1*ForcaTotal # Caso o sentido seja negativo
        Vetor_Forca.append([ForcaTotal, Posicao])

      elif (Fi > Ff): # Caso do trapézio com base maior na esquerda
        Forca_Tri = ((Fi-Ff)*(Pi-Pf))/2 # Cálculo da Força Parcial do Triângulo
        Forca_Ret = (Pi-Pf)*Ff # Cálculo da Força Parcial do Retângulo
        Pos_Tri = Pf + (Pi-Pf)*2/3 # Cálculo da Posição da Força
        Pos_Ret = Pf + ((Pi-Pf)/2) # Cálculo da Posição da Força
        if (Si == 2):
          Forca_Tri == -1*Forca_Tri # Caso o sentido seja negativo
          Forca_Ret == -1*Forca_Ret # Caso o sentido seja negativo
        Vetor_Forca.append([Forca_Tri, Pos_Tri])
        Vetor_Forca.append([Forca_Ret, Pos_Ret])

      elif (Ff > Fi): # Caso do trapézio com base maior na direita
        Forca_Tri = ((Ff-Fi)*(Pi-Pf))/2 # Cálculo da Força Parcial do Triângulo
        Forca_Ret = (Pi-Pf)*Fi # Cálculo da Força Parcial do Retângulo
        Pos_Tri = Pf + (Pi-Pf)*1/3 # Cálculo da Posição da Força
        Pos_Ret = Pf + ((Pi-Pf)/2) # Cálculo da Posição da Força
        if (Si == 2):
          Forca_Tri == -1*Forca_Tri # Caso o sentido seja negativo
          Forca_Ret == -1*Forca_Ret # Caso o sentido seja negativo
        Vetor_Forca.append([Forca_Tri, Pos_Tri])
        Vetor_Forca.append([Forca_Ret, Pos_Ret])

  elif (Si != Sf):  # Se atravessa o eixo

    if (Pf > Pi): # Se a posição final for maior que a posição inicial

      if (Si == 1): # Se começa no positivo e vai pro negativo

        Ff1 = Ff * -1
        a0 = (Pf-Pi)/2
        a = fsolve(sis_pos, a0, args=(Pf-Pi, Fi, Ff1))
        Ponto_0 = Pi + ponto_0(a,Fi) # Ponto onde acontece a troca do eixo. Agora irá ter duas forças, uma do início até o Ponto 0 e do Ponto 0 até o final.
        Forca_Tri1 = Fi*(Ponto_0 - Pi)/2
        Forca_Tri2 = Ff*(Pf - Ponto_0)/2
        Pos_Tri1 =  Pi + (Ponto_0 - Pi)*1/3 # Cálculo da Posição da Força
        Pos_Tri2 = Ponto_0 + (Pf - Ponto_0)*2/3 # Cálculo da Posição da Força
        Forca_Tri2 = -1*Forca_Tri2
        Vetor_Forca.append([Forca_Tri1, Pos_Tri1])
        Vetor_Forca.append([Forca_Tri2, Pos_Tri2])

      else: # Se começa do negativo e vai pro positivo
        Fi1 = Fi * -1
        a0 = (Pf-Pi)/2
        a = fsolve(sis_pos, a0, args=(Pf-Pi, Fi1, Ff))
        Ponto_0 = Pi + ponto_0(a,Fi1)
        Forca_Tri1 = Fi*(Ponto_0 - Pi)/2
        Forca_Tri2 = Ff*(Pf - Ponto_0)/2
        Pos_Tri1 =  Pi + (Ponto_0 - Pi)*1/3 # Cálculo da Posição da Força
        Pos_Tri2 = Ponto_0 + (Pf - Ponto_0)*2/3 # Cálculo da Posição da Força
        Forca_Tri1 = -1*Forca_Tri1
        Vetor_Forca.append([Forca_Tri1, Pos_Tri1])
        Vetor_Forca.append([Forca_Tri2, Pos_Tri2])

    else: # Se a posição inicial for maior que a posição final

      if (Si == 1): # Se começa no positivo e vai pro negativo
        Ff1 = Ff * -1
        a0 = (Pi-Pf)/2
        a = fsolve(sis_pos, a0, args=(Pi-Pf, Fi, Ff1))
        Ponto_0 = Pf + ponto_0(a,Ff1)
        Forca_Tri1 = Ff*(Ponto_0 - Pf)/2
        Forca_Tri2 = Fi*(Pi - Ponto_0)/2
        Pos_Tri1 =  Pf + (Ponto_0 + Pf)*1/3 # Cálculo da Posição da Força
        Pos_Tri2 = Ponto_0 + (Pi - Ponto_0)*2/3 # Cálculo da Posição da Força
        Forca_Tri1 = -1*Forca_Tri1
        Vetor_Forca.append([Forca_Tri1, Pos_Tri1])
        Vetor_Forca.append([Forca_Tri2, Pos_Tri2])

      else: # Se começa do negativo e vai pro positivo
        Fi1 = Fi * -1
        a0 = (Pi-Pf)/2
        a = fsolve(sis_pos, a0, args=(Pi-Pf, Fi1, Ff))
        Ponto_0 = Pf + ponto_0(a, Fi1)
        Forca_Tri1 = Ff*(Ponto_0 - Pf)/2
        Forca_Tri2 = Fi*(Pi - Ponto_0)/2
        Pos_Tri1 =  Pf + (Ponto_0 - Pf)*1/3 # Cálculo da Posição da Força
        Pos_Tri2 = Ponto_0 + (Pi - Ponto_0)*2/3 # Cálculo da Posição da Força
        Forca_Tri2 = -1*Forca_Tri2
        Vetor_Forca.append([Forca_Tri1, Pos_Tri1])
        Vetor_Forca.append([Forca_Tri2, Pos_Tri2])
    #print(f"a = {ponto_0(a,Ff)}")
    #print(f"Ponto de Inflexão :{Ponto_0}")

def Cargas(t): #Função Cargas salva os valores de Inputs em arrays que serão utilizidos posteriormente no cálculo de reações.
    Cargas = []
    Momento = []
    while True:
        Q = input("Digite qual o tipo da sua carga:\nTipo 1: Carga Pontual\nTipo 2: Momento\nTipo 3: Carga Distribuída\n").upper()
        if Q == "TIPO 1":
            F = float(input("Digite o valor da força em Newton[N]:\n"))
            X = float(input("Digite a posição da força no objeto[m]:\n"))
            while X > t:
                X = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
            S = input("Digite o sentido da sua força\nPositivo ou Negativo\n").upper()
            while S not in ["POSITIVO", "NEGATIVO"]:
                print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'POSITIVO' ou 'NEGATIVO'.\n")
                S = input("Digite o sentido da sua força\nPositivo ou Negativo\n").upper()
            if S == 'NEGATIVO':
              F = F * -1
            Cargas.append([F, X])
        elif Q == "TIPO 2":
            F = float(input("Digite o valor do Momento[Nm]:\n"))
            X = float(input("Digite a posição do momento no objeto[m]:\n"))
            while X > t:
                X = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
            S = input("Qual o sentido do seu momento?\n Digite [A] se for Anti-Horário\n Digite [H] se for Horário\n").upper()
            while S not in ["A", "H"]:
                print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'ANTI-HORÁRIO' ou 'HORÁRIO'.\n")
                S = input("Qual o sentido do seu momento?\n Digite [A] se for Anti-Horário\n Digite [H] se for Horário\n").upper()
            if S == "A": #Valor Anti-horário é negativo
                F = -1* F
            Momento.append([F, X])
        elif Q == "TIPO 3":
            P = input("Como sua carga está distribuída?\nLinearmente\nOutro\n").upper()
            if P == "LINEARMENTE":
                POS = float(input("Digite a posição inicial da sua força:\n"))
                while POS > t:
                    POS = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                POS1 = float(input("Digite a posição final da sua força:\n"))
                while POS1 > t:
                    POS1 = float(input("O valor digitado é maior que o objeto, insira um valor real:\n"))
                V1 = float(input("Digite o valor inicial da força em [N]:\n"))
                V2 = float(input("Digite o valor final da força em [N]:\n"))
                Si = input("Digite o sentido da força inicial:\nPositivo ou Negativo\n").upper()
                while Si not in ["POSITIVO", "NEGATIVO"]:
                    print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'POSITIVO' ou 'NEGATIVO'.\n")
                    Si = input("Digite o sentido da força inicial:\nPositivo ou Negativo\n").upper()
                Sf = input("Digite o sentido da força final:\nPositivo ou Negativo\n").upper()
                while Sf not in ["POSITIVO", "NEGATIVO"]:
                    print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'POSITIVO' ou 'NEGATIVO'.\n")
                    Sf = input("Digite o sentido da força final:\nPositivo ou Negativo\n").upper()

                cargas_distribuidas(POS, POS1, V1, V2, Si, Sf, Cargas) #
            elif P == "OUTRO":
               print("Indisponível na versão Gratuita, por favor Adquira nosso plano PREMIUM PLUS ULTRA BIG MECSOL")
        else:
            print("ERRO: É NECESSÁRIO DIGITAR UM VALOR VÁLIDO 'TIPO 1', 'TIPO 2' ou 'TIPO 3'.\n")
            continue

        L = input("Quer adicionar outra força? [S \ N] \n").upper()
        while L not in ["S", "N"]:
            print("Digite um valor válido.\n")
            L = input("Quer adicionar outra força? [S \ N]\n").upper()
        if L == "N":
            break
    #print(f'Cargas: {Cargas}\nMomentos: {Momento}')
    return Cargas, Momento

cargas, momento = Cargas(tamanho)

def reacoes(apoio, cargas, momentos):
    if apoio[0][0] == 'eng':
        #calcula as reação para o engaste
          R1 = 0 #reação das forças
          R2 = 0 #reação dos momentos
          for carga in cargas:
            R1 += carga[0]
            R2 += carga[0] * (carga[1] - apoio[0][1])
          for momento in momentos:
            R2 += momento[0]
          return print(f'As reações são:  {R1} N e  {R2} N-m')
    else: # calcula as reaçoes para pino/rolete
        soma_forcas = 0  # reação das forças
        soma_momentos = 0  # reação dos momentos
        for carga in cargas:
            soma_forcas += carga[0]
            soma_momentos += carga[0] * (carga[1] - apoio[0][1])
        for momento in momentos:
            soma_momentos += momento[0]
        R2 = soma_momentos / (apoio[1][1]-apoio[0][1])
        R1 = soma_forcas - R2
        return print(f'As reações são:  {R1} N no primeiro apoio e  {R2} N no segundo apoio')

reacoes(apoios, cargas ,momento)
