# webscraping_projetos

## Iniciando Projeto

- Comando :
    - 'scrapy startproject nome_projeto'
        -'scrapy startproject coleta'   


-Comando para iniciar o Crawler:
    - 'scrapy genspider  nome do spider + url_do_site'
        - 'scrapy genspider notbook https://lista.mercadolivre.com.br/notebook#D[A:notebook]'


-Porcesso do parser(quando eu seleciono as marcações do HTML que eu quero)
    - scrapy shell (para sair usar: exit())
        -fetch('https://lista.mercadolivre.com.br/notebook#D[A:notebook]')
            -DEBUG: Crawled (403) (significa que é erro de requisição, não foi encontrada/bloqueio)
    -criando um USER AGENT (existe um user agent é u cabeçãlho que vc manda pro servidor explicando de onde esta saindo o acesso, e vai ter um use agent para cada tipo/versão de navegador, para dispositivo (celular,tablet, pc, tv-- para que ele possa voltar as info compativeis com o seu equipamento))
        - No google pesquise por : "my user agent"
            -(Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36) -->retirado em 11.04.25
        - no arquivo 'settings.py' localize por 'user agent' caso estaja comentado, retire e cole o seu user agent.               
