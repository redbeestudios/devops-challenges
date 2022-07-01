## Ejecutar cliente SQL:

kubectl run -it --rm --image=mysql:8.0.29 --restart=Never mysql-client -- mysql -h simpsons-quotes-mysql -pPassword123