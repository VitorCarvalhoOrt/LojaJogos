# Catalogo da Loja de Jogos Digitais

---
Esse sistema tem como alvo servir como solução prática para a organização de um catálogo de jogos. Também é um alvo a escalabilidade, já que um catalogo pode ser gigantesco e difícil de padronizar

## Modelos

### Desenvolvedor

| Atributo       | Tipo         | Exemplo         |
|----------------|--------------|-----------------|
| nome           | CharField    | Bethesda        |
| motor_jogos    | CharField    | Creation Engine |
| ano_fundacao   | IntegerField | 1986            |


### Plataforma

| Atributo       | Tipo         | Exemplo    |
|----------------|--------------|------------|
| tipo           | CharField    | Computador |
| nome           | CharField    | Steam      |
| ano_lancamento | IntegerField    | 2003       |
| geracao        | IntegerField | 7          |

## Jogo

| Atributo       | Tipo                      | Exemplo                                     |
|----------------|---------------------------|---------------------------------------------|
| titulo         | CharField                 | Skyrim                                      |
| descricao      | TextField                 | Skyrim é a terra natal de um povo...        |
| genero         | CharField                 | Action RPG                                  |
| ano_lancamento | IntegerField              | 2011                                        |
| preco          | DecimalField              | 149.99                                      |
| desenvolvedor  | ForeignKey(Desenvolvedor) | Bethesda                                    |
| plataforma     | ManyToMany(Plataforma)    | Steam, PS3, PS4, PS5, Xbox 360, Xbox One... |

## Atributos, modelos, relacionamentos
Cada um da tabela Jogo se relaciona com um único desenvolvedor da tablea `Desenvolvedor`. Configura-se, então, um relacionamento 1:N, já que um desenvolvedor pode desenvolver vários jogos
Paralelamente, um jogo pode ser disponível em diversas plataformas, e cada `Plataforma` pode ter vários jogo, característico do relacionamento N:M
O `ForeignKey` com o `on_delete=models.SETNULL` foi escolhido com base na possibilidade de existirem jogos ativos, mas que têm o estudio fechado. Assim, o `SET_NULL` serve para manter o registro do jogo, definindo o estudio como `NULL`, que será interpretado como estudio fechado