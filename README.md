# 🔐 AES Password Encryptor

Projeto simples em Python para **criptografar e descriptografar senhas** utilizando o algoritmo AES (Advanced Encryption Standard) no modo CBC, com preenchimento PKCS7 e codificação Base64.

> ⚠️ **Este projeto é para fins educacionais.** Em aplicações reais, utilize hashing seguro (como bcrypt) para armazenar senhas. Não utilize criptografia reversível em produção para esse propósito.

---

## 📂 Arquivos incluídos

- `encrypt.py` – Script para criptografar senhas.
- `descrip.py` – Script para descriptografar senhas previamente criptografadas.

---

## 🛠 Requisitos

- Python 3.6+
- Biblioteca `cryptography`

### Instalação da biblioteca:

```bash
pip install cryptography
```

---

## 🚀 Como usar

### 🔑 1. Criptografar uma senha

Execute o script `encrypt.py`:

```bash
python encrypt.py
```

Digite a senha quando solicitado. O script irá gerar e exibir a senha criptografada em Base64.

### 🔓 2. Descriptografar uma senha

Execute o script `descrip.py`:

```bash
python descrip.py
```

Cole a senha criptografada gerada anteriormente e veja a versão descriptografada (original).

---

## 🧠 Como funciona

- **AES (CBC Mode)**: Utiliza uma chave simétrica de 16 bytes e um IV aleatório de 16 bytes.
- **PKCS7 Padding**: Garante que os dados tenham um tamanho múltiplo do bloco AES (128 bits).
- **Base64**: Facilita a exibição e armazenamento da saída criptografada em formato de texto.

---

## ❗ Aviso de Segurança

Este projeto **não deve ser utilizado para proteger senhas de usuários em produção**. Use **hashing com salt** (como `bcrypt`, `argon2`, ou `scrypt`) para armazenamento seguro.  
Criptografia reversível só deve ser usada quando **você precisa recuperar o valor original**, o que **não é o caso de senhas de autenticação**.

---

## ✍️ Autora

Desenvolvido por Gaby Valéria.  
Sinta-se à vontade para usar, adaptar e contribuir!
