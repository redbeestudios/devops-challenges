# "Enunciado"

Generar una herramienta para uso exclusivo de los operadores, asumiendo que no tienen conocimiento para editar o modificar el mismo.

El archivo input.json contiene configuraciones para una orquestador de contenedores (Marathon).

Dentro del mismo se encuentra la definición de N aplicaciones con información respecto al runtime (con que imagen de Docker corre, cuanta RAM/CPU tiene reservada, que puertos reserva/expone, cuantas instancias ocupa, etc.)

Para la resolución y parseo del input se deberá usar la herramienta [jq](https://stedolan.github.io/jq/)

---

## Parte 1:

- Armar un script de Bash (Linux) para obtener todas las aplicaciones que hayan cambiado su configuración (lastChangedAt) en las ultimas X horas. (Por ej: últimas 24 horas).

- La salida del script tiene que tener el nombre de cada aplicación y su fecha de modificación.

**BONUS: Debe verse primero la última que se modifico (lastChangedAt).**
**BONUS: Buscar las aplicaciones con conflicto de puerto, en la definicion de la aplicaciones hay un port (servicePort), ver que no colisionen entre ellos.**

---

## Parte 2:

- Armar una imagen de Docker que permita al operador utilizarla sin necesidad de instalarse jq localmente.

**BONUS: Armar un documento que describa la ejecucion**