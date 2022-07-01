## Subir imagen a registry de minikube

```bash
eval $(minikube docker-env)
docker build -t simpsons-quotes:0.1.3 .
```

## Acceder de forma externa con ingress nginx
```bash
kubectl patch configmap tcp-services -n ingress-nginx --patch '{"data":{"8000":"default/simpsons-quotes-api:8000"}}'

kubectl patch deployment ingress-nginx-controller --patch "$(cat ingress-nginx-controller-patch.yaml)" -n ingress-nginx

minikube ip

curl -X GET $(minikube ip):8000/quotes
```