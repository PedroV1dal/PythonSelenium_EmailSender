# Automatizador de Email

Esse é um projeto em estado de desenvolvimento onde será feito a verificação dos horários de envios de email dos terminais no porto de Satos, e caso exceda um período superior a 24 horas, o email será disparado automaticamente

## Ferramentas

- Python [https://www.python.org/downloads/]
- Pycharm Community [https://www.jetbrains.com/pycharm/]
- Chromium [https://www.chromium.org/getting-involved/download-chromium/]
- Selenium

## Features 
- [x] Logar na conta e ir até a página da tabela
- [x] Atualizar os dados da tabela e ordenar 
- [x] Verificar a data do último evento e ver se passaram 24 horas 
- [ ] Autenticar o email para envio automático
- [ ] Adicionar os destinatários certos que receberão o email
- [ ] Configurar para pegar o nome do terminal automaticamente no 'To' do email

## Configuração do projeto

Clone o projeto para a sua máquina

```bash
git clone https://github.com/PedroV1dal/PythonSelenium_EmailSender
```

### Instalação do Selenium

Rode o seguinte comando para instalar o Selenium

```bash
pip install selenium
```

### Configuração no Pycharm

Ao instalar o Pycharm, na hora de instalar marque as seguintes opções:
- Create Desktop Shortcut
- Update PATH variable
- Create Associations

Dentro do PyCharm, clique em novo projeto e faça a configuração do python no projeto

Após criar o projeto, vá em 'Files' -> 'NewProject' e crie o projeto dentro da pasta do projeto raiz.

### Sobre o Chromium 

Verifique a versão do navegador do seu google chrome para baixar versão compatível do chromium com o seu chrome

### Autor

Pedro Vidal
