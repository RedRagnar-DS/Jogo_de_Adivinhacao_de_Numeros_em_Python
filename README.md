# 🎯 Jogo de Adivinhação de Números

Jogo interativo desenvolvido em Python onde o jogador tenta adivinhar um número secreto gerado aleatoriamente pelo computador.

> Projeto desenvolvido como atividade remota PACD — **Turma 1ºTCDN**
> Tema: *Inteligência Artificial como Coautora*

---

## 🕹️ Como Funciona

O computador escolhe um número aleatório entre **1 e 50** e você tem **7 tentativas** para adivinhar. A cada palpite, o jogo informa se o número secreto é maior ou menor, e quando você chega perto (diferença ≤ 5), recebe uma dica extra.

### Sistema de Pontuação

| Tentativas | Pontos |
|:---:|:---:|
| 1ª tentativa | 100 pts |
| Até 3 | 50 pts |
| Até 5 | 25 pts |
| 6–7 | 10 pts |

O jogo permite múltiplas rodadas e exibe um resumo final com estatísticas.

---

## 🚀 Como Executar

```bash
python jogo_adivinhacao.py
```

Requisitos: **Python 3.6+** (usa apenas a biblioteca padrão `random`).

---

## 📚 Conceitos de Programação Utilizados

### Variáveis
Armazenam limites do jogo, pontuação, contadores de rodadas e tentativas, o número secreto e o palpite do jogador.

### Estruturas de Decisão (`if` / `elif` / `else`)
- Comparação do palpite com o número secreto
- Cálculo de pontuação por faixa de tentativas
- Dica de proximidade
- Tratamento de entrada inválida (`try`/`except`)
- Mensagem personalizada no resumo final

### Estruturas de Repetição (`while` / `for`)
- `while jogando` — loop principal que mantém o jogo ativo
- `for tentativa_atual in range(...)` — controla as 7 tentativas por rodada
- `while True` — validação da resposta para continuar ou parar

---

## 💡 Curiosidade: Busca Binária

Se você sempre chutar o número do meio do intervalo possível, consegue adivinhar qualquer número de 1 a 50 em no máximo **6 tentativas** (log₂(50) ≈ 5,64). Esse é o princípio do algoritmo de **busca binária**, um dos mais importantes da ciência da computação.

---

## 🤖 IA Utilizada

Este projeto foi desenvolvido com auxílio do **Claude** (Anthropic), utilizado como coautor para geração do código.

---

## 📄 Licença

Projeto acadêmico — uso livre para fins educacionais.
