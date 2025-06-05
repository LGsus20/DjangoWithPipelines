# To-Do List

## 1. Secure Production Environment
- Restrict direct access to the backend service (`:8000`) and the database in the production environment.
- Ensure that only the NGINX container is accessible from outside the container network.
## 2. Obfuscate domain name 
- Remove the domain name in default.prod.config
## 3. Separate .env
- Have 1 .env for each docker compose
## 4. Move hardcoded names
- Move names like 'Users' to variables