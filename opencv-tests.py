#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

# o segundo parâmetro da função indicará o modo de cor da imagem
# 0 = modo escala de cinza (1 canal de intensidade)
# 1 = modo imagem colorida (3 canais de intensidade)
# default = 1
img = cv2.imread ('teste.jpg', 1)

# mostra a representação da matriz de intensidade da imagem
print "Matriz de Intensidade"
print img

# O padrão de cores do opencv é BGR
(b, g, r) = img[0, 0]
print "Cor do pixel em (0, 0):"
print "Vermelho: %d, Verde: %d, Azul: %d" % (r, g, b)

# Comando para exibir uma imagem
cv2.imshow('nomedajanela', img)
# Espera até que uma tecla seja precionada
# o parâmetro indica quantos milesegundos o programa deve esperar
# Se o valor 0 for passado, ele aguardará indefinidamente
cv2.waitKey(5000)
# Fecha a todas as janelas abertas pelo opencv
cv2.destroyAllWindows()

# Acessando Atributos da Imagem
print "Altura (height): %d pixels" % (img.shape[0])
print "Largura (width): %d pixels" % (img.shape[1])
print "Canais (channels): %d"      % (img.shape[2])

# Mostra quantos pixels a imagem tem
print "Quantidade de pixels na imagem : %d pixels." % (img.size)

# Editando os pixels da imagem
img[50:100, 50:100] = (0, 255, 0)

cv2.imshow('nomedajanela', img)
cv2.waitKey(10000)

# Comando que salva uma nova imagem
cv2.imwrite('novaimagem.jpg', img)

# obtem um pedaço da imagem e salva um novo arquivo
fatia = img[279:378, 411:598]
cv2.imwrite('fatia.png', fatia)
