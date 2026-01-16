# WordPress CI/CD - ESIEA DevOps 2026


## Architecture

- **WordPress** (Bitnami)
- **MySQL 8.0**
- **Docker Compose** pour le développement local
- **Kubernetes** pour la production
- **CI/CD** avec GitHub Actions
- **Génération automatique** des manifests via Kompose

## CI/CD Pipeline

### Étapes

1. **Validation** des manifests (docker-compose + kubernetes)
2. **Tests** (WordPress + MySQL)
3. **Génération des manifests** via Kompose
4. **Upload sur FTP** OVH

### Configuration des secrets GitHub

Dans `Settings > Secrets and variables > Actions` :

**Obligatoires** (pour l'upload FTP) :
```
FTP_SERVER = ftp.cluster118.voh.com
FTP_USERNAME = loudivuine
FTP_PASSWORD = TempPass62
```
