<h1>Criptografia com Python</h1>
<p>Este é um dos projetos com resultados de estudos sobre Python e suas funcionalidades.</p>
<p>O princípio do projeto é realizar a criptografia e descriptografia de mensagens através da quantidade de vezes que
o usuário seleciona para embaralhar suas mensagens. Este projeto utiliza-se do conceito de criptografia de Caesar que
embaralha as letras de uma frase ou palavra através do alfabeto.</p>
<p>Para este projeto não será utilizado nenhuma biblioteca externa, tudo será desenvolvido apenas com a base de Python.
</p>

<h2>Configurando o alfabeto</h2>
<p>Antes de iniciar o projeto, vamos criar uma lista chamada <i>alphabet</i>, nessa lista deve conter o alfabeto por
inteiro escrito duas vezes, duas vezes devido algumas limitações que serão explicadas posteriormente. O resultado da
lista deverá ser da seguinte forma:</p>

```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```
<h2>Definindo a função de criptografia</h2>
<p>Agora com nosso alfabeto atribuido, podemos definir a função que fará todo processo de criptografia e descriptografia
, vamos chamar essa função de <i>caesar</i>, essa função receberá 3 argumentos, sendo eles <i>direct, text_input,
shift_number</i> sendo a função de cada um:
<li><i><b>direct</b></i></li>
O argumento direct será o responsável por identificar se vamos criptografar ou descriptografar uma mensagem.
<li><i><b>text_input</b></i></li>
É o argumento que irá receber a mensagem que deve ser criptografada ou descriptografada.
<li><i><b>shift_number</b></i></li>
Shift_number é o argumento que irá passar quantas vezes a mensagem será criptografada, essa informação é necessária
para realizar a descriptografia.
</p>
<p>Agora que temos todos os argumentos definidos, precisamos passar uma variável com uma string vazia, para receber o
nosso texto criptografado, vamos chamar essa variável de <i>cypher_text</i></p>
<p>Com a variável definida, vamos criar uma condição para identificar se nosso texto está sendo descritografado, caso
a informação seja verdadeira, a função deve tornar nosso shift_number negativo, isso significa que se utilizamos 8x
para embaralhar a mensagem, caso precise descriptografar, a função torna -8x transformando em um processo reverso.</p>
<p>Com a condição para identificar a descriptografia criada, vamos realizar uma iteração com o nosso texto adicionado em
<i>text_input</i> onde, para cada caractere no nosso <i>text_input</i> ele captura o index daquele caractere na nossa
lista <i>alphabet</i> criada anteriormente. Agora que temos a iteração, criamos uma condição que verifica se os
caracteres estão dentro da nossa lista com o alfabeto criada anteriomente. Essa informação do index capturado deverá 
ser armazenada em uma variável que vamos chamar de <i>position</i>.</p>
<p>Com o index das posições originais definidos em uma variável, vamos criar uma nova variável chamada de
<i>new_position</i>, essa variável receberá a posição atual + a quantidade de vezes que optamos por criptografar a
mensagem.</p>
<p>Temos uma variável com as novas posições, agora iremos chamar a variável <i>cypher_text</i> que foi criada com uma
string vazia no inicio e vamos incrementar nesta todos os caracteres da nossa lista contendo o alfabeto com as novas
posições.</p>
<p>Caso os caracteres não estejam no nosso alfabeto vamos apenas incrementar dentro da nossa variável <i>cypher_text</i>
os caracteres que não estão na lista com o alfabeto.</p>
<p>Por fim essa função deve imprimir na tela a nossas mensagem criptografada. Toda função deve ficar da seguinte maneira:
</p>

```
def caesar(direct, text_input, shift_number):
    cypher_text = ''
    if direct == "decode":
        shift_number *= -1
    for char in text_input:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            cypher_text = alphabet[new_position]
        else:
            cypher_text += char
    print(f"A mensagem {direct}d é: {cypher_text}")
```
<h2>Configurando a aplicação</h2>
<p>Como agora já temos a função que realiza a criptografia e descriptografia, precisamos criar a aplicação que irá
executar todo nosso projeto. Para isso vamos criar uma variável chamada <i>restart</i> e essa irá receber um valor
<i><b>True</b></i>, com isso definido iremos criar um <b>while loop</b> ou seja, enquanto nossa variável <i>restart
</i> for verdadeira, nosso projeto irá sempre se manter em execução.</p>
<p>Assim que o loop é iniciado, vamos criar uma váriavel chamada <i>direction</i> que irá receber um input solicitando
duas opções de <b>encode</b> para criptografar uma mensagem ou <b>decode</b> para descriptografar. Após o primeiro input
mais uma variável é declarada chamada <i>text</i> responsável por receber o texto que iremos manipular. Por fim criamos
a variável <i>shift</i> que recebe quantas vezes nosso texto será embaralhado.</p>
<p>Após os 3 inputs, precisamos tratar quantas vezes devemos embaralhar, tendo em vista que nossa lista de alfabeto não
é longa. Para isso colocamos para sempre retornar o resto da divisão com o valor total de caracteres no alfabeto,
realizamos isso utilizando um operador aritimético '%', por fimnossa função <i><b>caesar</b></i> é chamada, 
recebendo como argumento os 3 inputs armazenados em variáveis distintas. Conforme vimos, a função já nos retorna o 
resultado, ou seja o resultado já foi impresso, agora criamos uma variável chamada <i>result</i> que irá receber um 
input se queremos ou não utilizar a aplicação novamente. Com isso definido, por fim criamos uma condição que verifica 
se o resultado condiz em utilizar novamente ou não, caso o usuário opte por não utilizar novamente, definimos a função 
<i><b>restart</b></i> como <b>False</b>, que impede o loop de percorrer novamente e finaliza a aplicação.</p>
<p>O resultado final da aplicação é a seguinte:</p>

```
restart = True
while restart:
    direction = input("Digite 'encode' para criptografar ou 'decode' para descriptografar: ")
# Note que para o input da mensagem temos o "lower()" que mantém todos caracteres em minusculo
    text = input("Escreva sua mensagem: ").lower()
    shift = int(input("Quantas vezes deseja embaralhar: "))
    shift = shift % 26
    caesar(text_input=text, shift_number=shift, direct=direction)
    result = input("Deseja utilizar novamente? 'y' ou 'n': ").lower()
    if result == 'n':
        restart = False
```

<h2>Resultados</h2>
<p>Agora com o projeto finalizado, você pode ver os resultados dessa aplicação em tempo real acessando este 
<a href="https://replit.com/@AyrtonYamashita/Criptografia-com-Python">link</a>
com este projeto em nuvem utilizando Replit. Ao acessar basta logar com uma conta (se necessário) e clicar em run.</p>