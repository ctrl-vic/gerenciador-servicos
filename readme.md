# Gerenciador de Serviços

---

Criei esse projeto apenas para desenvolver minhas habilidades com o framework Flask. Você pode utilizá-lo como molde para desenvolver seus próprios projetos em Flask, mas não recomendo seguir a risca o que estou fazendo aqui, ainda tem muitos pontos frágeis e ele estará sempre sendo atualizado e corrigido conforme eu for me desenvolvendo. Se você tiverr qualquer dúvida sobre o projeto pode me perguntar, vou ajudar como puder! :)

---

## Resumo

Este projeto disponibiliza uma aplicação onde é possível gerenciar serviços a partir de um painel de controle, estes serviços são scripts em python que são executados e monitorados pela aplicação principal e que pode executar tarefas variadas. A aplicação também tem um sistema de gerenciamento de usuários, que faz com que o painel de controle só seja acessível após o login de um usuário, e os serviços disponíveis no painel dependam das permissões de cada usuário.

---

## Organização dos Arquivos

Os arquivos deste projeto estão dispostos da seguinte forma atualmente:

```
_____________________________________________________________________________________________________________

[ API-BASE ]
|
├─ readme.md			 
├─ app.py				> script da aplicação principal, inicia o servidor flask
├─ mapa_servicos.json			> json contendo informações sobre os serviços e suas rotas
├─ logs\				> pasta para salvar os logs  
|   ├─── logs_app\			> 	└─ referentes a aplicação principal 
|   |     └─── LOG_<datahora>.log	> 		└─ arquivos contendo os logs gerais de execução da aplicação
|   └─── logs_serv\			> 	└─ referentes aos servicos executados
└─ servicos\				> pasta onde estarão salvos todos os serviços para a aplicação
    └─── internos\			> 	└─ serviços internos como gerenciamento de usuários, grupos, etc
    └─── <nome_servico>\		> 	└─ uma pasta para um serviço específico, apenas para os scripts


_____________________________________________________________________________________________________________
```

##### Registro de Logs da Aplicação

O logger utilizado é o logger interno do Python associado à aplicação Flask.

Eles sempre estarão salvos como "

Os níveis de log disponíveis nele são os seguintes.

##### Registro de Logs dos Serviços

| tipo     | desc                 | valor |
| -------- | -------------------- | ----- |
| debug    | debug log info       | 10    |
| info     | info log information | 20    |
| warning  | warning log info     | 30    |
| error    | error log info       | 40    |
| critical | critical log info    | 50    |
