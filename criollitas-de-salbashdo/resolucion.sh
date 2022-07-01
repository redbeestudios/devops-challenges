#!/usr/bin/env bash

if [ $1 == '-h' -o $1 == '--help' ]; then
  echo "Uso del script:"
  echo "./$(basename $0) <OPCIONES>"
  exit 0
fi

#jq -r '.apps[] | "\(.id) \(.versionInfo.lastConfigChangeAt)"' input.json
jq -r '.apps[] | .id+" "+.versionInfo.lastConfigChangeAt' input.json | while read id fecha
do
  echo "appId: $id"
  echo "Fecha ultima modificacion: $fecha"
  echo ""
  #<COMANDOS DE ARITMETICA DE FECHAS>
done


# **BONUS: Buscar las aplicaciones con conflicto de puerto, en la definicion de la aplicaciones hay un port, ver que no colisionen entre ellos.**
jq -r '.apps[] | .container.portMappings[]? | .servicePort' input.json | uniq -c | awk -F' ' '{if($1>1){print $2}}'