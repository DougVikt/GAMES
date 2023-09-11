import pygame as pyg , random as rdn
from palette_cors import cors

# iniciando
pyg.init()

# tamanho
width = 840
height = 560 

screen = pyg.display.set_mode((width,height))
pyg.display.set_caption('SNAKE CORAL')

# cores
yellow = cors('yellow')
white = cors('white')
green = cors('green', 9)
purple = cors('purple' , 7)
black = cors('black')
red = cors('red' , 8)
draw = pyg.draw

# variaveis globais
loop = True
record = 0
score = [0,0,0]
 
# função de fechar ao clicar no 'X'
def close(event):
    
    global loop
      
    if event.type == pyg.QUIT :
        loop = False
    return loop
        
        
# função para criar as linhas        
def lines( start = [0 , 0], end = [0 , 0] , thick = 20 , cor = white ):
   
   return pyg.draw.line( screen, cor , start , end , thick)


# encurtar na criação das fontes
def sources(tm = int , bold = False):
  
   return pyg.font.SysFont(None , tm , bold)


# criando o quadro de linhas
def frame(thick = 20 , cor = white):
    
    lines_list = [
        lines([0 , 0], [0 , 560],thick , cor) ,
        lines([0, 0],[840 ,0 ], thick , cor) ,
        lines([840 , 0] , [840 , 560], thick , cor) ,
        lines([0 , 560],[840, 560], thick , cor)  
    ]
    return lines_list
      

# fução de colocar texto na tela
def text_screen( text = 'text' ,num = 20 , cor = white , local = [0 , 0] ,background = None ,  bold = False):
    
    source = sources(num , bold)
    button_txt = source.render(text,True , cor , background)
    return screen.blit(button_txt , local)


# tela inicial 
def screen_initial():
    
    global loop
    
    end = 0
    cor = yellow
    grow = 40
    
    while loop :
        
        event = pyg.event.poll()
        loop = close(event)
    
        screen.fill(black)
        
        # desenhando na tela 
        draw.polygon(screen , cors('red' , 10) , [(400 , 330), (420 , 330),  (480 , 540) ,(340 , 540)])
        draw.polygon(screen , white , [(200 , 450), (150 , 545),  (250 , 545)])
        draw.polygon(screen , white , [(620 , 450), (570 , 545),  (670 , 545)])
        draw.polygon(screen , white , [(130 , 300), (95 , 15),  (30 , 15)])
        draw.polygon(screen , white , [(700 , 300), (745 , 15),  (810 , 15)])
        
        # nomes na tela
        text_screen('SNAKE' , 120, white , [255 , 120]) 
        text_screen('SNAKE' , 120, purple , [258 , 125]) 
        text_screen('CORAL' , 90, red , [300 , 200], True) 
       
        # fazendo o nome piscar       
        time = pyg.time.get_ticks() 
        if time % 2 == 0 :
            cor = black
            if end == 0:
                pyg.time.delay(100)
        else :
            cor = yellow  
        
        text_screen('-- PRESS ENTER --' , 30 , cor , [320 , 300])   
        
        # ao apertar 'enter' as linhas aumentarão
        if event.type == pyg.KEYDOWN :
            if event.key == pyg.K_RETURN or event.key == pyg.K_KP_ENTER:
                          
                end = 2
        
        # quando as linhas preencherem a tela a função e encerrada
        if grow >= height :
            main()       
                
        
        grow += end 
        
        # quadro de fechamento
        frame(grow , red)    
      
        
       
            
        pyg.display.flip()
    
    
    
def main():
    
    
    global loop ,record
    
    # variaveis
    nivel = 0 
    num_r = [1,1]
    aceler = 0.5
    posit_x = width - 400
    posit_y = height - 200
    velo_x = velo_y = 0
    snake_l = [[posit_x , posit_y]]
    food_x = rdn.randint(30,820)
    food_y = rdn.randint(30,540)
    num_food = 0 
    grow_1 = height
    init = 2
    
    while loop:
           
        event = pyg.event.poll()
        loop = close(event)
        
        # diminuindo o quadro
        grow_1 -= init
        if grow_1 <= 20 :
            init = 0        
        if grow_1 >= height and init == -2 :
           game_over()
        
        # tela de fundo
        screen.fill(green)
        framer = frame(cor=red)  
        
        # posição da cobra 
        posit_y += velo_y
        posit_x += velo_x
        snake_l.append([posit_x , posit_y ])
        
        # fazendo o corpo da cobra
        for grow  in snake_l :
            snake = draw.rect(screen , black, [grow[0], grow[1], 10, 10], 0, 4) 
            draw.rect(screen , red, [grow[0], grow[1], 10, 10], 1, 6)
            
        # limitando o corpo de acordo com a quantidade da comida 
        if len(snake_l) > num_food :
            snake_l.pop(0)       
          
       
        # movimentando a cobra 
        if event.type == pyg.KEYDOWN:
            if event.key == pyg.K_LEFT:
                if velo_x == 0 :
                    velo_x = - aceler
                    velo_y = 0
                    
                    
            elif event.key == pyg.K_RIGHT:
                if velo_x == 0 :
                    velo_x = aceler
                    velo_y = 0
                    
                  
            elif event.key == pyg.K_UP:
                if velo_y == 0 :
                    velo_x = 0
                    velo_y = -aceler
                    
                 
            elif event.key == pyg.K_DOWN:
                if velo_y == 0 :
                    velo_x = 0
                    velo_y = aceler
                    
        
        
        # desenhando a comida
        food = draw.ellipse(screen , purple ,[food_x, food_y  , 10 , 10])
       
        # aparecendo a comida aleatoriamente depois do contato com a cobra
        if grow[0] == food_x and grow[1] == food_y or snake.colliderect(food):
            food_x = rdn.randint(30,820)
            food_y = rdn.randint(30,540)     
            num_food += 10
        
      
        # determinando o nivel do jogo e assim a velocidade a cobra
        num_r.insert(0 , num_food)
        if num_r[0] != num_r[1] :
            if num_r[0] % 120 == 0 :
                aceler += 0.5
                nivel += 1
           
       # quando a cobra bate no quadro 
        if snake.collidelistall(framer) : 
            init = - 2 
            record = num_food
        
        # textos na tela
        text_screen('SCORE : '+str(num_food), 35 , black , [200 , 20])     
        text_screen('NIVEL '+str(nivel) , 35 , black , [500 , 20])   
       
        # quadro de abertura 
        frame(grow_1 , red) 
        pyg.display.flip()
        
        
        
def game_over():
    
    global loop , record
    
    end = 0
    cor = yellow
    grow_1 = height
    go = 600
    go_1 = 950
    
    go_2 = [-130 , -230 , -330 , -430]
    init = {'grow_1' :3, 
            'go':0 , 
            'go_1':0 , 
            'go_2':0 ,
            'go_3':0 , 
            'go_4' :0 ,
            'go_5':0
            }
    
    # limitando e gravando o record 
    score.insert(0 ,record)
    if len(score) > 3 :
        score.pop()
    
    score.sort(reverse=True)
    
    while loop :
         
        event = pyg.event.poll()
        loop = close(event)
        
        screen.fill(black)
        
        # dando movimento aos textos
        grow_1 -= init['grow_1']
        go -= init['go']
        go_1 -= init['go_1']
        go_2[0] += init['go_2']
        go_2[1] += init['go_3']
        go_2[2] += init['go_4']
        go_2[3] += init['go_5']
        
        # parando o movimento
        if grow_1 <= 40 :
            
            init['grow_1'] = 0 
            init['go'] = 5
            
        if go <= 150 :
            
            init['go'] = 0
            init['go_1'] = 5
            
        if go_1 == 320 :
            
            init['go_1'] = 0 
            init['go_2'] = init['go_3'] = 5
            init['go_4'] = init['go_5'] = 5
            
        if go_2[0] == 350 : 
            init['go_2'] = 0
            
        if go_2[1] == 380 :
            init['go_3'] = 0
            
        if go_2[2] == 380 : 
            init['go_4'] = 0
            
        if go_2[3] == 380 :
            init['go_5'] = 0
            # texto para retornar a tela inicial 
            text_screen("-- BAR TO RETURN --" , 25 , cor , [320 , 430 ])   
            time = pyg.time.get_ticks() 
            if time % 2 == 0 :
                cor = black
                if end == 0:
                    pyg.time.delay(100)
            else :
                cor = yellow  
    
        # textos na tela 
        text_screen("GAME OVER !" ,80 , red , [ 240 , go])
        text_screen("YOU RECORD : "+ str(record) , 30 , white ,[go_1 , 220])
        text_screen("BEST SCORES :" , 25 , yellow , [go_2[0] , 270])
        text_screen("1° =  " + str(score[0]) , 25 ,yellow , [go_2[1] , 300])
        text_screen("2° =  " + str(score[1]), 25 ,yellow , [go_2[2] , 330])
        text_screen("3° =  " + str(score[2]) , 25 ,yellow , [go_2[3] , 360])
       
        # no caso da tecla barra ser apertada
        if event.type == pyg.KEYDOWN :
            if event.key == pyg.K_SPACE:
                screen_initial()
        
        
        
        frame(grow_1 , red)
        pyg.display.flip()  
        
        
    

    
# inicio ao jogo 
screen_initial()

    
    
    
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                           
            
