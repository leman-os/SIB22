#!/bin/bash -
if [ $3 ]; then
	echo "Ошибка. Больше 2-х параметров."
	exit 1

elif [[ "$1" == "crypt" ]]; then
	result="$(echo $2 | Base64)"

elif [[ "$1" == "decrypt" ]]; then
	result="$(echo $2 | Base64 -d)"

else
	echo "Ошибка. Неверные параметры."
	exit 1

fi
echo $result
