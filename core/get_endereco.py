import requests
import unicodedata
import re


# Remove acentos e caracteres especiais do texto
def remover_acentos(texto):

    nfkd = unicodedata.normalize('NFKD', texto)
    texto = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', texto)


def get_endereco(texto):

    url = 'https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php'
    post_data = {'pagina': '/app/endereco/index.php',
        'cepaux': '',
        'mensagem_alerta': '',
        'endereco': f'{remover_acentos(texto)}',
        'tipoCEP': 'ALL'
    }

    request = requests.post(url, post_data)
    response = request.json()

    if response['total'] == 0:
        return None

    endereco = []
    for x in response['dados']:
        data = {}
        data['uf'] = x['uf']
        data['localidade'] = x['localidade']
        data['logradouro'] = x['logradouroDNEC']
        data['logradouroTextoAdicional'] = x['logradouroTextoAdicional']
        data['logradouroTexto'] = x['logradouroTexto']
        data['bairro'] = x['bairro']
        data['cep'] = re.sub("(\d{2})(\d{3})(\d{3})", "\\1.\\2-\\3", x['cep'])
        endereco.append(data)
    return endereco