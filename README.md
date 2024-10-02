# **Apache Airflow & Kubernetes**

Este repositório contém estudos e experimentos envolvendo o [Apache Airflow](https://airflow.apache.org/) e a integração com o [Kubernetes](https://kubernetes.io/), duas ferramentas amplamente usadas para automação de workflows e orquestração de containers. O objetivo é explorar as funcionalidades dessas duas ferramentas e demonstrar sua aplicação em cenários práticos de automação de pipelines e orquestração de containers.

## **Apache Airflow**

O **Apache Airflow** é uma plataforma para criar, agendar e monitorar fluxos de trabalho programáticos. Ele é amplamente utilizado para gerenciar pipelines de dados, automatizando processos de ETL e outros tipos de workflows complexos.

## **Kubernetes**

O **Kubernetes** é uma plataforma de orquestração de containers que permite automatizar a implantação, o dimensionamento e a operação de aplicações em containers.

#### **Vantagens de usar o Airflow com Kubernetes:**

1. **Escalabilidade automática**: O Kubernetes pode automaticamente ajustar a quantidade de workers do Airflow dependendo da carga de trabalho.
2. **Isolamento**: Cada tarefa do Airflow pode ser executada em seu próprio container, garantindo que dependências e recursos sejam isolados.
3. **Gerenciamento simplificado**: Com o Kubernetes, é possível gerenciar o Airflow de maneira distribuída e resiliente, garantindo alta disponibilidade.

**Configuração do Airflow com Kubernetes:**

Para integrar o Airflow com o Kubernetes, os seguintes componentes são configurados:

1. **Executores Kubernetes**: O executor do Kubernetes executa as tarefas do Airflow em containers isolados, escalando conforme necessário.
2. **Helm Chart**: Utilize o Helm Chart oficial para a instalação do Airflow no Kubernetes.
3. **Volumes Persistentes**: Defina volumes persistentes no values.yaml para garantir que os logs e outros dados do Airflow sejam mantidos entre os reinícios.
4. **Configuração do RBAC**: O RBAC precisa estar ativado para permitir que o Airflow se comunique com a API do Kubernetes.

#### **Arquitetura:**

A integração do Airflow com o Kubernetes segue a seguinte arquitetura:

- Webserver: O front-end do Airflow, acessível via navegador para visualização e controle dos DAGs.
- Scheduler: Responsável por monitorar as tarefas e agendar as execuções no Kubernetes.
- Workers (Pods): Cada tarefa é executada em um Pod isolado no Kubernetes.
- Cluster Kubernetes: Orquestra os Pods, garantindo escalabilidade e resiliência.