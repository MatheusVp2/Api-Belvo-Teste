# API BELVO TESTES

## Criado um "redirecionamento" em Python com Flask e a Biblioteca da Belvo
- Não estava consguindo usar o ajax diretamente na api da Belvo, erro de não estava autenticando direto no header e estava dando erro no CORS
- Criei "api da api" praticamente mesma ideias das rotas, e desativei o CORS no Flask, e como ja estava sendo autenticado na biblioteca da Belvo não precisaria de autenticação

## HTML CSS JS
- Criado uma pagina empresa que esta consumindo api em Flask criada, e assim conseguindo obter as informações requeridas nas rotas do FLask e indiretamente na API da Belvo
