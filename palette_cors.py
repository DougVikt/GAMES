
# paleta de cores simples , para usar coloca a cor e o ton 
# não esta completa , pode adicionar muito mais cores e variações 
def cors(cor = 'black' ,tint = 0):

        try :
                        
                palet_cor = {
                        'blue': [[135,206,235],
                                [135,206,230],
                                [0,191,255],
                                [30,144,255],
                                [100,149,237],
                                [70,130,180],
                                [65,105,255],
                                [0,0,255],
                                [0,0,205],
                                [0,0,139],
                                [0,0,108],
                                [0,0,50]
                                ],
                        'red' : [[255,164,164],
                                [255,129,129],
                                [255,91,91],
                                [239,49,49],
                                [213,30,30],
                                [255,0,0],
                                [166,25,25],
                                [160,0,0],
                                [119,21,21],
                                [102,2,2],
                                [75,2,2],
                                [40,1,1]
                                ],
                        'green' : [[152,251,152],
                                [144,238,144],
                                [0,255,127],
                                [127,255,0],
                                [0,255,0],
                                [50,205,50],
                                [60,179,113],
                                [46,139,87],
                                [0,128,0],
                                [0,100,0],
                                [47,79,79]
                                ],
                        'orange' : [[255,165,0],
                                [255,140,0],
                                [255,127,80],
                                [255,99,71],
                                [255,69,0]                     
                                ],
                        'yellow' : [[240,230,140],
                                [255,255,0],
                                [255,215,0]
                                ],
                        'purple' : [[131,111,255],
                                [105,89,205],
                                [147,112,219],
                                [148,0,211],
                                [153,50,204],
                                [138,43,226],
                                [123,104,238],                     
                                [75,0,130]],
                        'pink' : [[255,192,203],
                                [221,160,221],
                                [238,130,238],
                                [255,0,255],
                                [219,112,147],
                                [255,20,147],
                                [199,21,133],
                                [128,0,128],
                                [139,0,139],
                                [128,0,128],
                                [153,50,204]                                                
                                ],
                        'cyan' : [[]],
                        'black' : [[0,0,0]],
                        'grey' : [[28,28,28],
                                [54,54,54],
                                [79,79,79],
                                [105,105,105],
                                [128,128,128],
                                [169,169,169],
                                [192,192,192],
                                [211,211,211],
                                [220,220,220]
                                ],
                        'white' : [[255,255,255]]
                                }


                if cor in palet_cor :
                        return palet_cor[cor][tint]

        except :
                return print('non-existent color !')

