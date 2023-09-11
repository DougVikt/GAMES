import pygame as pyg , random 

# iniciando o pygame
pyg.init()

# tamanho da tela
altura = 750
largura = 650

# criando a tela e colocando o nome 
tela = pyg.display.set_mode((largura , altura))
pyg.display.set_caption('ploop')

# caso não carregue o icone , fica o padrão
try:
   img = pyg.image.load('bola.png')
   pyg.display.set_icon(img)
except :
   img = None
   

# para desenhar na tela
desenho = pyg.draw

# variaveis de tempo
loop = True
cronom = ""
tempo = 0

# paleta de cores
amarelo = (255 , 255 , 0)
vermelho = (255 , 0 , 0)
verde = (0 , 255 , 0)
azul = (0 , 255 , 255)
laranja = (255 , 165 , 0)
coral = (255 , 127 , 80)
branco = (255 , 255 , 255) 
cinza = (30 ,30, 30)
preto = (0 ,0 ,0)
aleatorio = [
      random.randrange(0 , 256),
      random.randrange(0 , 256),
      random.randrange(0 , 256) 
      ]

cor = branco


# tela de fundo 
def tela_fundo():
   # caso não carregue a imagem
   try : 
      load = pyg.image.load('fundo.jpg').convert_alpha()
      fundo = tela.blit(load, [0 , 0])
   except:
      fundo = tela.fill(preto)
      
   return fundo


def linhas( inicio = [0 , 0], fim = [0 , 0] ,cor = branco , espes = 20):
   # para encurtar na criação das linhas 
   return pyg.draw.line( tela, cor , inicio , fim , espes)


def fontes(tm = int):
   # encurtar na criação das fontes
   return pyg.font.SysFont(None , tm )


def formatando (entrada = float):
   # definindo o a aceleração de acordo com o tempo
    format_1 = f'{entrada:,.4f}'
    format_2 = float(format_1)
    return format_2 % 5


def tela_inicio(): # ainda vou colocar um efeito no butão
   global cor , loop 
    
   # movimento 
   velo_x = 4
   velo_y = 4 
   posit_x = 260
   posit_y = 400
   posit_x1 =  250
   posit_y1 = 400
   
   # forma do butão
   forma1 = 180
   forma2 = 40
   
   alment = 50
   
   
   
   # iniciando....
   while loop :
      
      # ao clicar no 'X' , sair  
      evento = pyg.event.poll()
      if evento.type == pyg.QUIT :
         loop = False
      
      tela_fundo()
      
      if evento.type == pyg.KEYDOWN :
         if evento.key == pyg.K_RETURN or evento.key == pyg.K_KP_ENTER:
            alment = 20 
            break
            
      # desenho do butão
      desenho.rect(tela , vermelho , [posit_x1 , posit_y1 , forma1 , forma2] , 0 , 7)   
       
       
      # nomes na tela
      fonte = fontes(35)
      button_txt = fonte.render('PRESS ENTER',True , preto)
      tela.blit(button_txt , [255 , 410])
      fonte = fontes(140)
      nome = fonte.render('Ploop',True , cor )
      tela.blit(nome , [200 , 200])
      fonte = fontes(40)
      versao = fonte.render('v1.0', True , preto)
      tela.blit(versao , [310 , 680])
      
      # movimento da bola
      posit_x +=velo_x
      posit_y +=velo_y
      
      # ilimitando movimentação da bola
      if posit_x > 610 :
         velo_x = - 2.2
         cor = amarelo
      elif posit_x < 20 :
         velo_x = 2.3
         cor = verde

      if posit_y > 715 :
         velo_y = -2.3
         cor = laranja
      elif posit_y < 20 :
         velo_y = 2.2
         cor = azul
         
      # laterais
      linhas([0 , 0],[0 , 748],cor,alment) 
      linhas([0 , 0], [648 , 0],cor,alment)
      # pisos
      linhas([0 , 748] , [648 , 748],cor,alment)
      linhas([648 , 0],[648 , 748],cor,alment)

      desenho.ellipse(tela , cor, [posit_x, posit_y , 20 ,20])
            
      pyg.display.flip()
      

def main(): # colocar fisica na bola
   
   global cor,loop , tempo , cronom
   
   
   # movimentos
   aceler = 1.0
   velocit = 5
   movimento = 300
   posit_x = 320
   posit_y = 100
   velo_x = 1
   velo_y = 1

   bola = desenho.ellipse(tela , branco , [320, 690 , 20 ,20])
   
    
   
   # iniciando...
   while loop:
      
      # contador
      tempo+=0.0005
      if tempo > 0.9 :
         fast = formatando(tempo)
         if fast == 0:
            aceler += 0.5
            
      # ao clicar no 'X' , sair  
      evento = pyg.event.poll()
      if evento.type == pyg.QUIT :
         loop = False

      # movimento da bola
      posit_x+=velo_x
      posit_y+=velo_y

      # cronometro na tela
      cronom = "{:.1f}".format(tempo)
      fonte = fontes(100)
      contador = fonte.render(cronom,True ,cinza)

      tela_fundo()
      tela.blit(contador , [280 , 320])

      # laterais
      linhas([0 , 0],[0 , 748],cor) 
      linhas([0 , 0], [648 , 0],cor)
      # pisos
      piso = linhas([0 , 748] , [648 , 748],cor)
      linhas([648 , 0],[648 , 748],cor)

         
      acao = pyg.key.get_pressed()
      # para ação continua do persona 
      if acao[pyg.K_LEFT] or acao[pyg.K_a]:
         movimento -= velocit
      if acao[pyg.K_RIGHT] or acao[pyg.K_d]:
         movimento += velocit

      # limitando o persona 
      if movimento <= 7 :
         movimento += 5
      elif movimento >= 570:
         movimento -= 5


      # os personas
      retang1 = desenho.rect(tela , coral , [movimento , 705 , 76 ,23], 0 , 5)
      retang2 = desenho.rect(tela , coral , [posit_x , 20 , 76 ,23] , 0 , 5)

      # colisões da bola
      if bola.colliderect(retang2):
         if velo_x != 0:
            velo_y = aceler

      if bola.colliderect(retang1):
         if velo_x != 0:
            velo_y = -aceler 
            
      if bola.colliderect(piso):
         break
         


      # ilimitando movimentação da bola
      if posit_x > 620 :
         velo_x = -aceler
         cor = amarelo
      elif posit_x < 10 :
         velo_x = aceler
         cor = verde

      if posit_y > 725 :
         velo_y = -aceler
         cor = laranja
      elif posit_y < 10 :
         velo_y = aceler
         cor = azul

      # velocidade na tela 
      velocidade = fonte.render(('x'+ str(aceler)),True ,cinza)
      tela.blit(velocidade , [270 , 420])

      bola = desenho.ellipse(tela , cor, [posit_x, posit_y , 20 ,20])


         
      pyg.display.flip()


def gameover():
   # FIM DE JOGO 
   global desenho ,branco , loop , cronom ,tempo
   
   # aparecendo o tempo jogado
   def recordes(cor):
      fonte = fontes(40)
      recorde = fonte.render('Seu Recorde :' , True ,cor) 
      tempo_r = fonte.render( cronom, True , cor)
     
      return tela.blit(recorde , [187 , 450]) , tela.blit(tempo_r , [400 ,450])

   tela_fundo()
   
   while loop :
      # ao clicar no 'X' , sair  
      evento = pyg.event.poll()
      if evento.type == pyg.QUIT :
         loop = False

      # resposta dependendo do tempo jogado
      if tempo <= 10.0 :
        
         fonte = fontes(90)
         frase_1 = fonte.render('QUE FALTA ' , False,branco )
         tela.blit(frase_1 , [160 , 200])
         frase_2 = fonte.render('DE AGILIDADE !', False , branco)
         tela.blit(frase_2 , [100 , 320])
         recordes(vermelho)
        
        
      elif 10.0 < tempo <= 15.0 :
         
         fonte = fontes(90)
         frase_1 = fonte.render('ATE QUE' , False,branco )
         tela.blit(frase_1 , [180 , 200])
         frase_2 = fonte.render('VOCÊ E AGIL !', False , branco)
         tela.blit(frase_2 , [120 , 320])
         recordes(laranja)
        
      elif 15.0 < tempo <= 20.0 :
         
         fonte = fontes(90)
         frase_1 = fonte.render('E UMA MAQUINA !' , False,branco )
         tela.blit(frase_1 , [60 , 250])
         recordes(verde)
        
         
         
      elif 20.0 < tempo  :
         
         fonte = fontes(80)
         frase_1 = fonte.render('CALMA ! VAI ' , False,branco )
         tela.blit(frase_1 , [140 , 200])
         frase_2 = fonte.render('QUEBRAR O TECLADO !', False , branco)
         tela.blit(frase_2 , [10 , 320])
         recordes(azul)
      
      # para fechar e voltar a tela inicial
      fonte = fontes(40) 
      continuar = fonte.render('PRESS ENTER' , True , amarelo)
      tela.blit(continuar , [240 , 690])
      
      if evento.type == pyg.KEYDOWN :
         if evento.key == pyg.K_RETURN or evento.key == pyg.K_KP_ENTER:
            break   
      
     
      pyg.display.flip() 

# rodando o jogo ....
while loop :  
   tela_inicio()
   main()
   gameover()


