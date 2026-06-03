# Clear Home Broker Agent

Este projeto é um agente automatizador para operar no Home Broker da Clear Corretora via automação de navegador (Selenium), usando como exemplo o ativo MGLU3.

## Recursos
- Login automático no Home Broker
- Consulta de cotação de ativos (exemplo: MGLU3)
- Estrutura pronta para envio de ordens (compra/venda)

## Requisitos
- Python 3.8+
- Google Chrome instalado

## Instalação
```bash
pip install -r requirements.txt
```

## Uso
Edite o arquivo `config.py` com seu usuário e senha da Clear.

Execute o agente:
```bash
python main.py
```

> **Atenção:**
> 1. Não compartilhe suas credenciais.
> 2. Use apenas para fins educacionais e testes. Operações reais são por sua conta e risco.

## Estrutura
- `main.py` — Script principal do agente
- `config.py` — Configurações de usuário
- `requirements.txt` — Dependências
- `README.md` — Este guia
