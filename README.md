# django-starter-template

Base de código para criação de novos projetos

---

### Como rodar

```bash
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Features

- [x] Configuração DEBUG de acordo com .env (dev e prod)
- [x] Sistema de autenticação
- [x] Signal para criar um objeto profile para o usuário
- [ ] Multi-idiomas
- [ ] DRF para implementação de APIs Rest
- [ ] DRF Spetacular para documentação de APIs com Swagger
- [ ] Estrutura de testes unitários com pytest
- [ ] Controle de logs
- [ ] Plataforma de pagamento Stripe
