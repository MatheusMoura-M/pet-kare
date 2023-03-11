# Pet Kare

<h3><strong>Proposta:</strong></h3>
<p>Esse projeto tem uma aplicação simples para ajudar donos de Pet Shop a guardar dados de animais. Esta sendo utilizado:</p>

- Conceitos de Relacionamento e Serializers.
- Diagrama de Entidade e Relacionamento.
- Relacionamentos entre pets, grupos e características.
- Serializadores para validação, entrada e saída de dados para pets, grupos e características.
- Views de criação, listagem, filtragem, atualização e deleção de pets, recebendo informações de três tabelas de uma vez, com filtro na listagem.
- Tratamento de exceção nas rotas de criação, atualização, filtragem e deleção.
<hr noshade />

## Como rodar os testes localmente

- Verifique se os pacotes pytest e/ou pytest-testdox estão instalados globalmente em seu sistema:

```shell
pip list
```

- Caso seja listado o pytest e/ou pytest-testdox e/ou pytest-django em seu ambiente global, utilize os seguintes comando para desinstalá-los globalmente:

```shell
pip uninstall pytest pytest-testdox -y
```

<hr>

## Próximos passos:

### 1 Crie seu ambiente virtual:

```shell
python -m venv venv
```

### 2 Ative seu venv:

```shell
# linux:
source venv/bin/activate

# windows (powershell):
.\venv\Scripts\activate

# windows (git bash):
source venv/Scripts/activate
```

### 3 Instalar o pacote <strong>pytest-testdox</strong>:

```shell
pip install pytest-testdox pytest-django
```

### 4 Rodar os testes referentes a cada tarefa isoladamente:

Exemplo:

- Tarefa 1

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/
```

- Tarefa 2

```shell
pytest --testdox -vvs tests/tarefas/tarefa_2/
```

- Tarefa 3

```shell
pytest --testdox -vvs tests/tarefas/tarefa_3/
```

Você também pode rodar cada método de teste isoladamente seguindo uma substring, adicionando a flag `-k` seguido da substring a ser encontrada
(atenção, se o pytest achar multiplos métodos que contenham a mesma substring em seu nome, ele executará todos):

```shell
pytest --testdox -vvsk test_can_not_create_pet_when_missing_keys
```

<hr>

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

Exemplo: executar somente "test_can_get_product_by_id".

```shell
pytest --testdox -vvs tests/tarefas/tarefa_1/test_get_product_by_id.py::TestGetProductById::test_can_get_product_by_id
```
