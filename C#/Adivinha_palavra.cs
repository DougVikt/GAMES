
using System;
using System.Threading;
using System.Collections.Generic;


class Principal{
    static void Main(){ 
          
        Abertura();
        //atrazo 
        Thread.Sleep(1800);

        inicio:// chama para recomeçar
     
        // loop principal
        while (true){
            
            Console.Clear();
            Console.WriteLine("\tANTES DE COMEÇAR DIGITE AS PALAVRAS PARA SER USADA NO JOGO  ");
            Linhas(90);

            recolocar:
            
            List<char> letras = new List<char>();
            bool testando;
            string[] palavras = null;
            string palavra = null;
            int indice = 0;

            palavras = AdicionarPalavras();
            Console.Clear(); 
            Console.WriteLine("VERIFICANDO SUAS PALAVRAS ....");
            Linhas(90);
            Thread.Sleep(2000);
            Console.Clear();
                
            testando = TesteLetras(palavras);

            if (!testando){
                Console.WriteLine("Algo deu errado ! Voce colocou palavra(s) incorretas \n\tTente novamente");
                goto inicio;
            }
           
            recomecar:

            int aleatorio = new Random().Next(0 , palavras.Length);
            palavra = palavras[aleatorio];

            foreach(char lt in palavra){
                letras.Add(lt);
            }
            indice = palavra.Length;
            int tentativas = indice + 5;
            Jogando(letras , indice , palavra , tentativas);
                            
            Console.WriteLine("Gostou ? Bora de novo ? S(sim)/N(não)");
            string resposta = Console.ReadLine();
            if (resposta == "s" | resposta == "S"){
                Console.WriteLine("Quer refazer a lista de palavras ou fica com as que tenho aqui ? R (Refazer) / C (Continuar)");
                string confirma = Console.ReadLine(); 
                if(confirma == "R"| confirma == "r"){
                    goto recolocar;
                }
                else if(confirma == "C" | confirma == "c"){
                    goto recomecar;
                }
            }else {
                Console.WriteLine("Que pena ! ate a proxima ;)");
                break;
            }
        }
        
    }

    static void Abertura(){
        string traso = "--";
        string espaco = "\t\t\t";

        for(int n = 0; n<5 ; n++){
            traso += traso;
        }
        LinhaTraso(espaco , traso);
        Console.WriteLine("{0}|\t\t\tBEM VINDO AO JOGO\t\t       |",espaco );
        Console.WriteLine("{0}|\t\t      ADIVINHANDO A PALAVRA\t\t       |",espaco);
        LinhaTraso(espaco , traso);
        
           
    }
    static void LinhaTraso(string espaco , string traso){
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("{0}{1}",espaco, traso);
        Console.ResetColor();
        Console.WriteLine();
    }
    

    static string[] AdicionarPalavras(){
        string[] palavras = null;
        bool passa ;

        while(true){

            Console.WriteLine("coloque quantas palavras vai colocar , sedo entre 2 e 20 :");
            string entrada = Console.ReadLine();
            
            if(entrada.Length != 0 && entrada != "1"){ 
                if(entrada.Length <= 2){  
                    if(char.IsDigit(entrada[0]) && entrada.Length == 1 ){ 
                        passa = true;
                    }
                    else if (char.IsDigit(entrada[0]) && char.IsDigit(entrada[1])){ 
                        passa = true;
                    }
                    else{
                        passa = false; 
                        Console.WriteLine("Opa ! sem ser um numero não passa !");
                    }
                    if(passa){ 
                        int numero = Convert.ToInt32(entrada);
                        if(numero <= 20){
                            Console.WriteLine("Digite as palavras separadas por linha :");
                            palavras = new string[numero];
                            
                            for (int n = 0 ; n <= numero-1; n++){
                                Console.Write("digite aqui :");
                                palavras[n] = Console.ReadLine();           
                            } 
                            return palavras;
                        }
                        else{
                            Console.WriteLine("Eita ! ai não , so ate 20 ");
                        }
                        
                    }                       
                }
                else{
                    Console.WriteLine("Calma ai , so dois digitos porfavor !");
                    
                }

            }
            else {
                Console.WriteLine("Ai não meu filho ! digite algum numero maior que 1 , retornando...");
            
            }
        }
        

    }    

    static void Jogando(List<char> letras , int indice , string palavra , int tentativas){
        List<string> palavraCerta = AdicionaEspaco(palavra);
        int acertos=0 , erros=0 ;
        string letraUser ;
        char letraUserChar;
        string letrasAcertadas;

        Console.WriteLine("\t\t\tVAMOS COMEÇAR O JOGO !\n\tVOCE TEM 5 MAIS A QUANTIDADE DE LETRAS DA PALAVRA PARA ACERTA-LA\nDigite somente uma letra ");
        Linhas(90);
        Console.Write("ESCOLHI UMA BOA PALAVRA , A DICA E QUE ELA TEM ");
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("{0}",palavra.Length);
        Console.ResetColor();
        Console.WriteLine(" LETRAS");
        Console.WriteLine("Digite uma letra :"); 

        do {
            letraUser = Console.ReadLine();
            
            if(letraUser.Length == 1 && char.IsLetter(letraUser[0])){
                letraUserChar = letraUser[0];
                if(letras.Contains(letraUserChar)){
                    letras.Remove(letraUserChar);
                    ++acertos;
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.Write("== Certo => ");
                    Console.ResetColor();
                    palavraCerta = AmostraPalavra(palavraCerta ,letraUser , palavra);
                    letrasAcertadas = string.Join(" " , palavraCerta);
                    Console.WriteLine("{0}",letrasAcertadas);
                }
   
                else{
                    ++erros;
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("== Erro {0} ==",erros);
                    Console.ResetColor();
                    
                }
                if (acertos == indice ){
                    Console.WriteLine("Muito bem ! a palavra e {0}",palavra.ToUpper());
                    break;
                }
                else if(erros > acertos & erros + acertos == tentativas){
                    Console.WriteLine("Que pena, você errou mais de {0} \nA palavra era {1}",erros-1 , palavra);
                    break;
                }
            }
            else{
                Console.WriteLine("Digitou caracter errado ! Tente novamente !");
            }
        
        }while(tentativas >= acertos);
    }

    static List<string> AdicionaEspaco(string palavra){
        List<string> palavraCerta = new List<string>();
        foreach(char letra in palavra){
            palavraCerta.Add("_");
        }
        return palavraCerta;
    }

    static List<string> AmostraPalavra(List<string> palavraCerta, string letraUser , string palavra){


        for(int i=0 ;i < palavra.Length;++i){
            if(palavra[i] == letraUser[0] && palavraCerta[i] == "_"){
                palavraCerta[i] = letraUser[0].ToString().ToLower();
                break;
            }
        }
        
        return palavraCerta;
    }

    static void Linhas(int vezes){
        string barra = "_";
        string linha = "";
        for(int i = 0;i < vezes;++i){
            linha += barra;                
        }
        Console.WriteLine(linha);
    }


    static bool TesteLetras( string[] palavras){
       
        bool tem = true;

        foreach(string palavra in palavras){
            foreach (char letra in palavra ){
                if(char.IsLetter(letra)){
                   tem = true;
                }
                else{
                    tem = false;
                    break;
                }
            }
            
            if(!tem){
                break;
            } 
        
        }
        return tem;
    }
  
 
}
