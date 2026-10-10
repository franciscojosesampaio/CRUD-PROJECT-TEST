Esse projeto é um estudo a respeito de "CRUD" (Create, Read, Update, Delete), utilizando como base a linguagem de programação python.
O primeiro commit é apenas uma base de estudo pessoal com o intuito de fortalecer o conhecimento a respeito de manipulação de dados com SQL.
Esse projeto ainda irá receber atualizações e muito provavelmente irá ser portado para alguma outra linguagem (ex: javascript).
Existe alguns pontos de melhorias importantes a serem feitas no código, porém do jeito que está no momento já atende a proposta de um "CRUD".
Estou aberto dicas e criticas com finalidade de aprimoramento pessoal/profissional.
Utilização dos arquivos Python e DB livre para fins estudantis e uso de pesquisa.

Atualização 09/10/26
Foi feito uma atualização na parte de cadastro (match case 1).
- Ao selecionar a opção de cadastro, o programa inicia um loop até ser feito o cadastro de maneira bem sucedida
- Validações ocorrem do inicio ao fim do cadastro do jogo
- Se ocorrer um erro a tela será limpa para manter uma boa visibilidade
- Agora é feito validação nos seguintes campos : Nome, Gênero e Preço
- Se "abc" será exibido uma mensagem de erro;
- Se " " será exibido uma mensagem de erro
- Caso seja usado "," no preço, o programa converte para ".", assim evitando erro ocasionado pelo caracter digitado
- Se os dados informados forem válidos, o jogo será cadastrado no sistema (DB)
