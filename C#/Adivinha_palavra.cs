
using System;
using System.Threading;
using System.Collections.Generic;


class Principal{
    static void Main(){ 
          
        Abertura(); // função de abertura 
        //atrazo 
        Thread.Sleep(1800);

        inicio:// chama para recomeçar
     
        // loop principal
        while (true){
            
            Console.Clear();
            Console.WriteLine("\tANTES DE COMEÇAR DIGITE AS PALAVRAS PARA SER USADA NO JOGO  ");
            Linhas(90);

            recolocar:// reicinia caso o usuario queira refazer a lista
            
            // variaveis
            List<char> letras = new List<char>();
            bool testando;
            string[] palavras = null;
            string palavra = null;
            int indice = 0;

            // atribui a lista as palavras digitadas pelo usuario
            palavras = AdicionarPalavras();
            Console.Clear(); 
            Console.WriteLine("VERIFICANDO SUAS PALAVRAS ....");
            Linhas(90);
            Thread.Sleep(2000);
            Console.Clear();

            // chama a função de testar as letras 
            testando = TesteLetras(palavras);

            // caso não passe pelo teste
            if (!testando){
                Console.WriteLine("Algo deu errado ! Voce colocou palavra(s) incorretas \n\tTente novamente");
                goto inicio;
            }
           
            recomecar: // recomeça pos usuario escolher manter a lista digitada anteriormente 

            // escolhe uma palavra aleatoriamente
            int aleatorio = new Random().Next(0 , palavras.Length);
            palavra = palavras[aleatorio];
            // adiciona cada letra da palavra a lista letra 
            foreach(char lt in palavra){
                letras.Add(lt);
            }
            indice = palavra.Length;
            int tentativas = indice + 5; // define o numero de tentativas para acerto
            // função onde roda o jogo de adivinhar
            Jogando(letras , indice , palavra , tentativas);

            // finalidades                 
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
    // função de abertura , so para mostrar o cabeçalho do jogo
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

    // função que monta uma linha de acordo com o que e passado
    static void LinhaTraso(string espaco , string traso){
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("{0}{1}",espaco, traso);
        Console.ResetColor();
        Console.WriteLine();
    }
    
    // função de adicionar as palavras na lista 
    static string[] AdicionarPalavras(){
        string[] palavras = null;
        bool passa ;

        while(true){

            Console.WriteLine("coloque quantas palavras vai colocar , sedo entre 2 e 20 :");
            string entrada = Console.ReadLine();
            
            if(entrada.Length != 0 && entrada != "1"){ // passa se o que foi digitado tem um caracter , não sendo 1
                if(entrada.Length <= 2){  // passa se foi digitado tiver no maximo 2 numeros
                    if(char.IsDigit(entrada[0]) && entrada.Length == 1 ){ // passa se a entrada for numerico com so 1 caracter
                        passa = true;
                    }
                    else if (char.IsDigit(entrada[0]) && char.IsDigit(entrada[1])){ // passa se os dois caracteres forem numericos
                        passa = true;
                    }
                    else{ // recusa caso não passem pelos casos acima 
                        passa = false; 
                        Console.WriteLine("Opa ! sem ser um numero não passa !");
                    }
                    if(passa){ // passa se os dois primeiros casos forem verdadeiros 
                        int numero = Convert.ToInt32(entrada); // converte a string para int
                        if(numero <= 20){ // verifica se a entrada e menor ou igual a 20
                            Console.WriteLine("Digite as palavras separadas por linha :");
                            palavras = new string[numero];
                            // pega as palavras na quandidade que foi escolhida 
                            for (int n = 0 ; n <= numero-1; n++){
                                Console.Write("digite aqui :");
                                palavras[n] = Console.ReadLine();           
                            } 
                            return palavras; // retorna a lista com as palavras
                        }
                        else{
                            Console.WriteLine("Eita ! ai não , so ate 20 ");
                        }
                        
                    }   // respostas para cada caso de falso                    
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
    // função do jogo 
    static void Jogando(List<char> letras , int indice , string palavra , int tentativas){
        List<string> palavraCerta = AdicionaEspaco(palavra);
        int acertos=0 , erros=0 ;
        string letraUser ;
        char letraUserChar;
        string letrasAcertadas;

        // cabeçalho da parte de adivinhar 
        Console.WriteLine("\t\t\tVAMOS COMEÇAR O JOGO !\n\tVOCE TEM 5 MAIS A QUANTIDADE DE LETRAS DA PALAVRA PARA ACERTA-LA\nDigite somente uma letra ");
        Linhas(90);
        Console.Write("ESCOLHI UMA BOA PALAVRA , A DICA E QUE ELA TEM ");
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.Write("{0}",palavra.Length);
        Console.ResetColor();
        Console.WriteLine(" LETRAS");
        Console.WriteLine("Digite uma letra :"); 
        // loop de adivinha
        do {
            letraUser = Console.ReadLine();
            
            if(letraUser.Length == 1 && char.IsLetter(letraUser[0])){ // passa se a string digitada tiver um caracter e for uma letra 
                letraUserChar = letraUser[0]; // repassa a string para char
                if(letras.Contains(letraUserChar)){ // passa se a letra tem na lista letras
                    letras.Remove(letraUserChar); // remove a letra da lista
                    ++acertos;
                    Console.ForegroundColor = ConsoleColor.Green; // muda de cor o prompt
                    Console.Write("== Certo => ");
                    Console.ResetColor();
                    palavraCerta = AmostraPalavra(palavraCerta ,letraUser , palavra); // chama a função de amostrar a palavra so com a letra(s) acertda(s)
                    letrasAcertadas = string.Join(" " , palavraCerta); // transforma a lista em um string 
                    Console.WriteLine("{0}",letrasAcertadas); // amostra na tela
                }
   
                else{ // caso seja falso o caso de cima 
                    ++erros;
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("== Erro {0} ==",erros); // mostra a quantidade de erros 
                    Console.ResetColor();
                    
                }
                if (acertos == indice ){ // passa se os acertos for igual a quantidade de letras da palavra
                    Console.WriteLine("Muito bem ! a palavra e {0}",palavra.ToUpper());
                    break;
                }
                else if(erros > acertos & erros + acertos == tentativas){ // passa se a quantidade de erros for maior aos de acertos e a soma deles de igual ao total de tentativas 
                    Console.WriteLine("Que pena, você errou mais de {0} \nA palavra era {1}",erros-1 , palavra);
                    break;
                }
            }
            else{
                Console.WriteLine("Digitou caracter errado ! Tente novamente !");
            }
        
        }while(tentativas >= acertos);
    }

    static List<string> AdicionaEspaco(string palavra){ // função que adiciona os traços a lista de letras acetadas 
        List<string> palavraCerta = new List<string>();
        foreach(char letra in palavra){
            palavraCerta.Add("_");
        }
        return palavraCerta;
    }

    static List<string> AmostraPalavra(List<string> palavraCerta, string letraUser , string palavra){
        // pega a lista de palavras ja com traços e substitui cada letra acertada no lugar da letra deacordo com a palavra

        for(int i=0 ;i < palavra.Length;++i){
            if(palavra[i] == letraUser[0] && palavraCerta[i] == "_"){
                palavraCerta[i] = letraUser[0].ToString().ToLower();
                break;
            }
        }
        
        return palavraCerta;
    }

    static void Linhas(int vezes){ // função simples para adicionar linhas na tela
        string barra = "_";
        string linha = "";
        for(int i = 0;i < vezes;++i){
            linha += barra;                
        }
        Console.WriteLine(linha);
    }


    static bool TesteLetras( string[] palavras){ // testa cada letra para que não passe nem um numero , se tiver retorna false 
       
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
