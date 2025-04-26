# webscraping_projetos

## Iniciando Projeto

* Comando :
    * 'scrapy startproject nome_projeto'
        *'scrapy startproject coleta'   


* Comando para iniciar o Crawler:
    * 'scrapy genspider  nome do spider + url_do_site'
        * 'scrapy genspider notbook https://lista.mercadolivre.com.br/notebook#D[A:notebook]'


* Porcesso do parser(quando eu seleciono as marcações do HTML que eu quero)
    * scrapy shell (para sair usar: exit())
        * fetch('https://lista.mercadolivre.com.br/notebook#D[A:notebook]')
            * DEBUG: Crawled (403) (significa que é erro de requisição, não foi encontrada/bloqueio)
    * criando um USER AGENT (existe um user agent é u cabeçãlho que vc manda pro servidor explicando de onde esta saindo o acesso, e vai ter um use agent para cada tipo/versão de navegador, para dispositivo (celular,tablet, pc, tv-- para que ele possa voltar as info compativeis com o seu equipamento))
        * No google pesquise por : "my user agent"
            * (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36) -->retirado em 11.04.25
        * no arquivo 'settings.py' localize por 'user agent' caso estaja comentado, retire e cole o seu user agent. 

    * Comando 'response.text' no scrapy shell ele tras todas as info da páginaexit"

    * Comando para buscar algo dentro da estrutra html e css
        * após achar a tag onde esta localizado a informação que deseja no scrapy shell
        digite response.css('nome da tag + nome_classe') 
        no caso a tag é a 'span' --> product.css('span.poly-component__brand::text').get()

    * Para rodar o arquivo o comando é: 'scrapy crawl nome_arquivo -o data.json'--o (-o é para salvar)
        * 'scrapy crawl notebook -o data.json' -- salva em JSON
        * 'scrapy crawl notebook -o data.csv' -- salva em CSV

## TRATAMENTO DE DADOS COM PANDAS

Sempre no projeto é importante criar duas colunas 
* '_source' | '_datetime'  (o underline é do mesmo conceito de POO uma variável privada que não se deve mexer)
