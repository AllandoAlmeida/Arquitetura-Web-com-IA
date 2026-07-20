# 🏗️ Álbum de Figurinhas - Copa do Mundo Tech (Arquitetura Web com IA)

Este projeto foi desenvolvido com o objetivo de entender **na prática** como funcionam as aplicações web modernas de ponta a ponta. Trata-se de um álbum digital interativo de figurinhas celebrando os grandes nomes e pioneiros da tecnologia e da inteligência artificial.

O projeto explora a comunicação entre cliente e servidor, a separação de responsabilidades no desenvolvimento de software e o uso de Inteligência Artificial como assistente de desenvolvimento.

---

## 🎯 Objetivo do Projeto

Demonstrar a integração entre:
- **Frontend**: Uma interface interativa e responsiva simulando um álbum físico com efeito de virar páginas.
- **Backend (API)**: Um servidor que fornece os dados e as imagens das figurinhas sob demanda.
- **Protocolo HTTP**: A ponte que viabiliza a comunicação de dados e recursos entre o cliente e o servidor.

---

## 📁 Estrutura de Arquivos e Suas Funcionalidades

Abaixo estão explicadas as responsabilidades de cada arquivo essencial do projeto:

### 1. 📄 [index.html](file:///f:/Arquitetura-Web-com-IA/index.html)
Define o esqueleto estrutural da aplicação.
- Contém a marcação HTML para o contêiner do livro e suas respectivas páginas.
- Estrutura os slots numerados (como `#01`, `#02`, etc.) correspondentes a cada figurinha e a sua categoria (IA, Python, Banco de Dados).
- Inclui os botões de navegação lateral (Página Anterior / Próxima Página) e de controle de som.

### 2. 🎨 [style.css](file:///f:/Arquitetura-Web-com-IA/style.css)
Responsável por toda a parte visual, estilização e design responsivo da aplicação.
- Define a paleta de cores moderna (tons escuros com acentos vibrantes em neon para cada categoria).
- Implementa o efeito de *glitch* tecnológico na capa do álbum.
- Aplica estilos para os slots das figurinhas, sombras realistas, cantos arredondados e transições suaves.
- Garante a responsividade do layout em diferentes tamanhos de tela.

### 3. ⚙️ [app.js](file:///f:/Arquitetura-Web-com-IA/app.js)
Contém toda a lógica de comportamento e integração da aplicação.
- **Efeito de Folha**: Inicializa e configura a biblioteca `St.PageFlip` para simular o efeito físico de folhear as páginas do álbum.
- **Interatividade**: Gerencia a navegação por botões, gestos de arrastar e o estado do áudio de fundo (mudo/ativo).
- **Consumo de API**: Faz uma requisição assíncrona (via `fetch`) para o backend em `http://localhost:8000/figurinhas` para baixar os dados das figurinhas e preencher dinamicamente os slots de `#01` a `#20` com suas respectivas imagens.

### 4. 📖 [README.md](file:///f:/Arquitetura-Web-com-IA/README.md)
Este arquivo de documentação que guia o usuário sobre a finalidade do projeto, a utilidade de cada arquivo e como executar a aplicação.

---

## 🚀 Tecnologias Utilizadas

- **HTML5**: Estruturação semântica da página.
- **CSS3 (Vanilla)**: Design premium, variáveis CSS, transições e efeitos de animação.
- **JavaScript (ES6+)**: Consumo de API, manipulação da DOM e gerenciamento de eventos.
- **St.PageFlip**: Biblioteca Javascript para simulação e animação realista de livro/álbum de páginas.
- **FastAPI / Uvicorn (Backend)**: Usado para disponibilizar a API REST local com a lista de figurinhas.

---

## 🔧 Como Executar o Projeto

1. **Backend**:
   Navegue até a pasta do backend (se aplicável) e inicie o servidor:
   ```bash
   cd backend/dia-3
   uvicorn main:app --reload
   ```
   *(Isso iniciará o servidor na porta 8000, onde a API de figurinhas estará disponível).*

2. **Frontend**:
   Abra o arquivo [index.html](file:///f:/Arquitetura-Web-com-IA/index.html) no navegador ou utilize um servidor local de desenvolvimento (como o *Live Server* do VS Code).

