
# Recursive Filter (smoother) with three elements
#
# filtbin(series, number of refiltering)
#
# Carlos Schettini
# 12-may-2019


import numpy as np

def filtbin(s, rec):

    for j in range(rec):

        gsf=np.array([])

        # pega do 2.o at� o pen�limo elemento da s�rie
        for i in range(1, len(s) - 1):

            # filtra
            sf = s[i - 1] / 4 + s[i] / 2 + s[i + 1] / 4

            # guarda
            gsf=np.append(gsf,sf)

        # calcula o primeiro e �ltimo elementos
        head = s[0] *.6 + gsf[0] *.4
        tail = s[-1] *.6 + gsf[-1] *.4

        # insere o primeiro e �ltimo elementos
        gsf = np.insert(gsf,0,head)
        gsf = np.append(gsf,tail)

        # retorna para re-filtragem
        s = gsf

    return s

# testando...
# import matplotlib.pyplot as plt
#
# s=np.array([1, 3, 5, 4, 5, 4, 3, 5, 7, 6, 5, 2, 3, 5, 7])
#
# sf=filtbin(s,1)
# sf2=filtbin(s,5)
#
# print(s[0],sf[0])
#
# plt.plot(s)
# plt.plot(sf)
# plt.plot(sf2)
# plt.show()
