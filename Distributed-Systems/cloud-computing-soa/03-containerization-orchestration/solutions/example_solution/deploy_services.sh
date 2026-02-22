kubectl label nodes wscbs-023 role=backend --overwrite=true 
kubectl label nodes wscbs-024 role=backend --overwrite=true 
kubectl label nodes wscbs-025 role=backend --overwrite=true 

# create volumes
kubectl apply -f k8s/volumes/db_volume.yaml
kubectl apply -f k8s/volumes/redis_volume.yaml

# create config maps
kubectl apply -f k8s/config_maps/auth_service_config.yaml
kubectl apply -f k8s/config_maps/db_config.yaml
kubectl apply -f k8s/config_maps/url_shortener_service_config.yaml

# create deployments and services
kubectl apply -f k8s/deployments/redis_deployment.yaml
kubectl apply -f k8s/services/redis_service.yaml
kubectl apply -f k8s/deployments/db_deployment.yaml
kubectl apply -f k8s/services/db_service.yaml
kubectl apply -f k8s/deployments/auth_service_deployment.yaml
kubectl apply -f k8s/services/auth_service_service.yaml
kubectl apply -f k8s/deployments/url_shortener_service_deployment.yaml
kubectl apply -f k8s/services/url_shortener_service_service.yaml
kubectl apply -f k8s/deployments/gateway_deployment.yaml
kubectl apply -f k8s/services/gateway_service.yaml

# rollout and restart after changes
kubectl rollout restart deployment redis
kubectl rollout restart deployment db
kubectl rollout restart deployment auth-service
kubectl rollout restart deployment url-shortener-service
kubectl rollout restart deployment gateway
