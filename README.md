
# Terraform Infrastructure as Code Repository

Este repositório organiza e gerencia infraestrutura como código (IaC) utilizando **Terraform**. Ele foi projetado para seguir as melhores práticas, garantindo modularidade, reutilização, e uma estrutura clara para ambientes distintos.

---

## Estrutura do Repositório

Abaixo está uma visão geral da estrutura de pastas e arquivos:

```plaintext
├── environments
│   ├── dev
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   ├── prod
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── terraform.tfvars
│   │   └── backend.tf
│   └── staging
│       ├── main.tf
│       ├── variables.tf
│       ├── terraform.tfvars
│       └── backend.tf
├── modules
│   ├── network
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── variables.tf
│   │   └── README.md
│   ├── compute
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── variables.tf
│   │   └── README.md
│   ├── security
│   │   ├── main.tf
│   │   ├── outputs.tf
│   │   ├── variables.tf
│   │   └── README.md
│   └── storage
│       ├── main.tf
│       ├── outputs.tf
│       ├── variables.tf
│       └── README.md
├── pipelines
│   ├── dev-pipeline.yaml
│   ├── prod-pipeline.yaml
│   └── staging-pipeline.yaml
├── scripts
│   ├── pre-deploy.sh
│   └── post-deploy.sh
├── .gitignore
├── README.md
└── versions.tf
```

---

## Descrição das Pastas e Arquivos

### **1. Environments**
A pasta `environments` contém configurações específicas para cada ambiente (ex.: `dev`, `staging`, `prod`).  
Cada ambiente possui:
- **`main.tf`:** Declara os recursos do Terraform, referenciando módulos reutilizáveis.
- **`variables.tf`:** Define as variáveis usadas nesse ambiente.
- **`terraform.tfvars`:** Valores específicos das variáveis (ex.: região, tipo de instância).
- **`backend.tf`:** Configuração do estado remoto (ex.: S3 + DynamoDB).

### **2. Modules**
A pasta `modules` contém módulos reutilizáveis que abstraem componentes da infraestrutura, como:
- **`network`:** Gerencia VPCs, sub-redes, gateways, etc.
- **`compute`:** Gerencia instâncias EC2, grupos de escalabilidade, etc.
- **`security`:** Gerencia grupos de segurança, regras de IAM, etc.
- **`storage`:** Gerencia buckets S3, volumes EBS, etc.

Cada módulo segue este padrão:
- **`main.tf`:** Define a lógica e os recursos principais.
- **`variables.tf`:** Variáveis necessárias para parametrizar o módulo.
- **`outputs.tf`:** Valores de saída (ex.: IDs, IPs) para serem usados em outros módulos.
- **`README.md`:** Documentação do módulo.

### **3. Pipelines**
Arquivos YAML para configurar pipelines de CI/CD para cada ambiente:
- **`terraform fmt`:** Formata o código.
- **`terraform validate`:** Valida a sintaxe.
- **`terraform plan`:** Planeja mudanças.
- **`terraform apply`:** Aplica mudanças aprovadas.

### **4. Scripts**
Scripts complementares para execução antes e depois de aplicar as configurações:
- **`pre-deploy.sh`:** Valida pré-requisitos e dependências.
- **`post-deploy.sh`:** Ações pós-deploy, como notificações ou configuração adicional.

### **5. Outros Arquivos**
- **`.gitignore`:** Evita versionar arquivos sensíveis como:
  ```plaintext
  *.tfstate
  .terraform/
  terraform.tfvars
  ```
- **`versions.tf`:** Especifica versões do Terraform e provedores:
  ```hcl
  terraform {
    required_version = ">= 1.5.0"
    required_providers {
      aws = {
        source  = "hashicorp/aws"
        version = "~> 5.0"
      }
    }
  }
  ```

---

## Requisitos

1. **Terraform instalado:** [Download](https://www.terraform.io/downloads.html).
2. **Configuração de backend remoto:** Exemplo no arquivo `backend.tf`.
3. **Credenciais de provedor:** Use variáveis de ambiente ou ferramentas de gestão de segredos.

---

## Comandos Básicos

### Inicializar o Terraform
```bash
terraform init
```

### Planejar mudanças
```bash
terraform plan -var-file="terraform.tfvars"
```

### Aplicar mudanças
```bash
terraform apply -var-file="terraform.tfvars"
```

### Formatar o código
```bash
terraform fmt
```

### Validar a configuração
```bash
terraform validate
```

---

## Contribuindo

1. Faça um fork do repositório.
2. Crie um branch para suas alterações: `git checkout -b feature/nova-funcionalidade`.
3. Submeta um pull request após os testes.

---

## Autor

Este repositório foi configurado para seguir padrões DevOps modernos em **Infraestrutura como Código**. Para dúvidas ou suporte, entre em contato.
