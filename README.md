# ATIV_PARADIGMAS_RHAYNON_YASMIN
Atividade avaliativa de Paradigmas P1


Da linha 1 até a 13 foi utilizado paradigma funcional com o pilar do código puro.
Nas linhas 1, 4 , 7, 10 foi usado o pilar imutabilidade, não alteramos os valores de a nem b
Usamos composição de funções com as funções de soma, sub, multi e div dentro da função da calculadora.


Da linha 16 até a 51 usamos o paradigma imperativo
Usando:
- Estrutura de controle  Ex: Linha 19 até 50
- Estrutura de repetição Ex: Linha 19
- Estrutura condicional Ex: Linha 30 até linha 50
- Entrada e armazenamento de volumes Ex: Linha 35 e 36
- Comando de saída Ex: Linha 51






Consulta IA:

Os **paradigmas imperativo e funcional** são formas diferentes de organizar e pensar programas.

 ### Paradigma imperativo

 Baseia-se na ideia de **descrever como o programa deve executar uma tarefa**, por meio de mudanças de estado.

 Seus principais pilares são:

 - **Estado:** os dados do programa podem mudar ao longo da execução.
- **Variáveis:** armazenam valores que podem ser alterados.
- **Atribuição:** modifica o estado das variáveis.
- **Sequência:** comandos são executados em uma determinada ordem.
- **Estruturas de controle:** `if/else`, `for`, `while` etc. determinam o fluxo de execução.
- **Procedimentos/funções:** agrupam instruções para realizar tarefas.

 **Exemplo:**

```
total = 0
for numero in numeros:
    total = total + numero
```

 Aqui, `total` é modificado a cada iteração. O foco está em **como** chegar ao resultado.

 ### Paradigma funcional

 Baseia-se na ideia de **computar valores por meio da composição e avaliação de funções**, aproximando a programação do conceito matemático de função.

 Seus principais pilares são:

 - **Funções como valores:** funções podem ser armazenadas, passadas como argumentos e retornadas por outras funções.
- **Imutabilidade:** prefere-se não alterar valores existentes.
- **Funções puras:** para uma mesma entrada, produzem a mesma saída e evitam efeitos colaterais.
- **Composição de funções:** funções menores são combinadas para formar operações mais complexas.
- **Recursão:** frequentemente utilizada no lugar de estruturas iterativas tradicionais.
- **Expressões:** o foco está em produzir valores, em vez de executar uma sequência de comandos que modifica o estado.

 **Exemplo:**

```
total = sum(numeros)
```

 Ou, conceitualmente:

```
total = reduce(lambda x, y: x + y, numeros)
```

 Aqui, o foco está em **o que** deve ser calculado, e não em modificar explicitamente uma variável durante a execução.

 ### Diferença central

 | Imperativo | Funcional |
| --- | --- |
| Foco em **como fazer** | Foco em **o que calcular** |
| Estado mutável | Preferência por estado imutável |
| Atribuições e comandos | Expressões e funções |
| Iterações (`for`, `while`) | Composição, `map`, `filter`, `reduce`, recursão |
| Efeitos colaterais são comuns | Busca-se minimizar efeitos colaterais |

Na prática, muitas linguagens modernas, como Python, JavaScript, Java e C#, permitem combinar **características imperativas e funcionais** no mesmo programa.
