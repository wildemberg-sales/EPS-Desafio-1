# Relatório de Prontidão Técnica: Onboarding SecOps
**Disciplina:** Engenharia de Produto de Software (FGA0316) - 2026.1  
**Aluno:** Wildemberg Sales da Silva Junior | **Matrícula:** [20/2017503]

## 1. Configuração do Ambiente (Zero Trust & Isolamento)
Conforme as diretrizes de Soberania Técnica, as seguintes configurações foram aplicadas:
- [x] **Python 3.12:** Instalado e verificado.
- [x] **Poetry:** Configurado para criar `.venv` dentro do projeto (`virtualenvs.in-project true`).
- [x] **Determinismo:** Arquivos `pyproject.toml` e `poetry.lock` gerados com sucesso.

## 2. Logs de Auditoria e Qualidade (Security Gate)
Abaixo constam os resumos das execuções dos comandos de segurança:

### 2.1. Auditoria Estática (Bandit)
```bash
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.12.13
Run started:2026-04-01 00:19:59.985495+00:00
Test results:
	No issues identified.
Code scanned:
	Total lines of code: 155
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0
Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 0
		High: 0
Files skipped (0):
```

*Comando: `poetry run bandit -r .`*

### 2.2. Verificação de Dependências (Safety)
```bash
+===========================================================================================================================================================================================+
DEPRECATED: this command (`check`) has been DEPRECATED, and will be unsupported beyond 01 June 2024.
We highly encourage switching to the new `scan` command which is easier to use, more powerful, and can be set up to mimic the deprecated command if required.
+===========================================================================================================================================================================================+
+==============================================================================+
                               /$$$$$$            /$$
                              /$$__  $$          | $$
           /$$$$$$$  /$$$$$$ | $$  \__//$$$$$$  /$$$$$$   /$$   /$$
          /$$_____/ |____  $$| $$$$   /$$__  $$|_  $$_/  | $$  | $$
         |  $$$$$$   /$$$$$$$| $$_/  | $$$$$$$$  | $$    | $$  | $$
          \____  $$ /$$__  $$| $$    | $$_____/  | $$ /$$| $$  | $$
          /$$$$$$$/|  $$$$$$$| $$    |  $$$$$$$  |  $$$$/|  $$$$$$$
         |_______/  \_______/|__/     \_______/   \___/   \____  $$
                                                          /$$  | $$
                                                         |  $$$$$$/
  by safetycli.com                                        \______/
+==============================================================================+
 REPORT 
  Safety v3.7.0 is scanning for Vulnerabilities...
  Scanning dependencies in your environment:
  -> /home/runner/.cache/pypoetry/virtualenvs/eps-desafio-1-KwQaythV-
  py3.12/lib/python3.12/site-packages
  Using open-source vulnerability database
  Found and scanned 50 packages
  Timestamp 2026-04-01 00:20:03
  0 vulnerabilities reported
  0 vulnerabilities ignored
+==============================================================================+
 No known security vulnerabilities reported. 
+==============================================================================+
+===========================================================================================================================================================================================+
DEPRECATED: this command (`check`) has been DEPRECATED, and will be unsupported beyond 01 June 2024.
We highly encourage switching to the new `scan` command which is easier to use, more powerful, and can be set up to mimic the deprecated command if required.
+===========================================================================================================================================================================================+
```

*Comando: `poetry run safety check`*

*OBS*: É interessante mudar a utilização do comando `check` para o novo comando `scan` do Safety, que é recomendado pela biblioteca.

### 2.3. Qualidade e Conformidade (Ruff)
```bash
Run poetry run ruff check .
  poetry run ruff check .
  shell: /usr/bin/bash -e {0}
  env:
    pythonLocation: /opt/hostedtoolcache/Python/3.12.13/x64
    PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib/pkgconfig
    Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
    Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
    Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.12.13/x64
    LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.12.13/x64/lib
  
All checks passed!
```

*Comando: `poetry run ruff check .`*

## 3. Evidência de Integração Contínua (CI)
O pipeline automatizado foi executado com sucesso no GitHub Actions:
- **Link da Action de Sucesso:** https://github.com/wildemberg-sales/EPS-Desafio-1/actions/runs/23825622089/job/69447815246

## 4. Declaração de Soberania Técnica (CISSP Domain 8)
Eu, Wildemberg Sales da Silva Junior, declaro que auditei manualmente as ferramentas e dependências deste projeto. Confirmo que o código gerado via IA (GitHub Copilot) passou pela minha revisão humana (*Human-in-the-loop*), garantindo que não há vazamento de segredos ou falhas lógicas críticas antes da migração para o ecossistema da PCDF.

---
**Data de Entrega:** [31/03/2026]