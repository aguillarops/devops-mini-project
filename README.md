# Mini Projeto DevOps com AWS ECS Fargate, Terraform, GitHub Actions, Prometheus e Grafana

Este mini projeto pessoal demonstra uma pipeline de DevOps completa, desde o provisionamento de infraestrutura até o monitoramento de uma aplicação containerizada na AWS.

## Visão Geral

O objetivo deste projeto é criar um ambiente de demonstração que engloba as seguintes tecnologias e conceitos:

- **Terraform**: Para provisionar a infraestrutura na AWS (VPC, Subnets, ECR, ECS Cluster, ECS Service, ALB, etc.).
- **GitHub Actions**: Para automação de CI/CD, construindo a imagem Docker, enviando para o ECR e atualizando o serviço ECS.
- **AWS ECS com Fargate**: Para orquestrar e executar a aplicação containerizada sem a necessidade de gerenciar servidores.
- **Aplicação Flask**: Uma aplicação Python simples que expõe endpoints de saúde e métricas.
- **Prometheus e Grafana**: Para monitoramento da aplicação e da infraestrutura (configurados para execução local via Docker Compose).

## Estrutura do Projeto

```
. 
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # Workflow do GitHub Actions para CI/CD
├── flask-app/
│   ├── src/                      # Código fonte da aplicação Flask
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   └── user.py
│   │   └── models/
│   │       └── user.py
│   ├── Dockerfile                # Dockerfile para a aplicação Flask
│   ├── requirements.txt          # Dependências Python
│   └── .dockerignore             # Arquivo para ignorar no build do Docker
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus.yml        # Configuração do Prometheus
│   ├── grafana/
│   │   └── provisioning/
│   │       └── datasources/
│   │           └── prometheus.yml # Configuração do datasource do Grafana
│   └── docker-compose.yml        # Docker Compose para Prometheus e Grafana
├── terraform/
│   ├── providers.tf              # Configuração dos providers do Terraform
│   ├── variables.tf              # Variáveis do Terraform
│   ├── main.tf                   # Definição dos recursos da AWS
│   └── outputs.tf                # Saídas do Terraform
└── README.md                     # Este arquivo
```

## Pré-requisitos

Para executar este projeto, você precisará ter:

- Conta AWS configurada com credenciais de acesso programático.
- Terraform instalado.
- Docker e Docker Compose instalados (para execução local do monitoramento).
- Git instalado.
- Um repositório GitHub para o projeto.

## Configuração e Execução

### 1. Configuração da AWS

Certifique-se de que suas credenciais AWS estejam configuradas. Você pode usar o AWS CLI:

```bash
aws configure
```

### 2. Provisionamento da Infraestrutura com Terraform

Navegue até o diretório `terraform` e inicialize o Terraform:

```bash
cd terraform
terraform init
```

Revise o plano de execução e aplique as mudanças:

```bash
terraform plan
terraform apply
```

Isso provisionará a VPC, subnets, ECR, ECS Cluster, Security Group, ALB e as roles IAM necessárias.

### 3. Configuração do GitHub

Crie um novo repositório no GitHub e faça o push do código:

```bash
git init
git add .
git commit -m "Initial commit: DevOps Mini Project"
git branch -M main
git remote add origin <URL_DO_SEU_REPOSITORIO>
git push -u origin main
```

Configure as seguintes `Secrets` no seu repositório GitHub (Settings -> Secrets and variables -> Actions):

- `AWS_ACCESS_KEY_ID`: Sua chave de acesso AWS.
- `AWS_SECRET_ACCESS_KEY`: Sua chave secreta AWS.

### 4. CI/CD com GitHub Actions

O workflow `ci-cd.yml` será acionado automaticamente em cada push para a branch `main`. Ele realizará as seguintes etapas:

1. Checkout do código.
2. Configuração das credenciais AWS.
3. Login no Amazon ECR.
4. Construção da imagem Docker da aplicação Flask.
5. Tagging e push da imagem para o ECR.
6. Download da definição de tarefa ECS existente.
7. Atualização da definição de tarefa com a nova imagem.
8. Implantação do serviço ECS com a nova definição de tarefa.

Você pode acompanhar o progresso na aba "Actions" do seu repositório GitHub.

### 5. Monitoramento com Prometheus e Grafana (Local)

Para monitorar a aplicação, você pode executar o Prometheus e o Grafana localmente usando Docker Compose. Certifique-se de que a aplicação Flask esteja acessível a partir do ambiente onde o Docker Compose está sendo executado (para testes locais, você pode expor a porta da aplicação Flask).

Navegue até o diretório `monitoring` e inicie os serviços:

```bash
cd monitoring
docker-compose up -d
```

- **Prometheus**: Acesse `http://localhost:9090`
- **Grafana**: Acesse `http://localhost:3000` (Credenciais padrão: `admin`/`admin`)

O Grafana já estará configurado com o datasource Prometheus. Você pode criar dashboards para visualizar as métricas expostas pela aplicação Flask (`/api/metrics`).

## Limpeza

Para evitar custos desnecessários, lembre-se de destruir a infraestrutura provisionada pelo Terraform quando não precisar mais dela:

```bash
cd terraform
terraform destroy
```

## Contribuição

Sinta-se à vontade para contribuir, abrir issues ou sugerir melhorias.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

