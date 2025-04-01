# Comandos Básicos de Git

Git es un sistema de control de versiones distribuido que te permite gestionar el historial de versiones de tu proyecto. Aquí te dejo una lista con los comandos más utilizados:

```bash
git config --global user.name "Tu Nombre"  # Configura tu nombre de usuario
git config --global user.email "tu.email@example.com"  # Configura tu correo electrónico

git init  # Inicializa un repositorio vacío en el directorio actual

git clone https://github.com/usuario/repositorio.git  # Clona el repositorio remoto a tu máquina

git status  # Muestra los cambios no confirmados y el estado actual del repositorio

git add archivo.txt  # Agrega un archivo específico al área de preparación
git add .  # Agrega todos los archivos modificados al área de preparación

git commit -m "Mensaje descriptivo del commit"  # Realiza un commit con un mensaje descriptivo

git log  # Muestra el historial de commits del repositorio

git branch nombre-de-la-rama  # Crea una nueva rama en el repositorio

git checkout nombre-de-la-rama  # Cambia a una rama existente
git checkout -b nueva-rama  # Crea y cambia a una nueva rama

git merge nombre-de-la-rama  # Fusiona la rama especificada con la rama actual

git branch -d nombre-de-la-rama  # Elimina una rama que ya no necesitas

git push origin nombre-de-la-rama  # Envía los cambios locales a un repositorio remoto

git pull origin nombre-de-la-rama  # Obtiene los cambios más recientes desde el repositorio remoto

git diff  # Muestra las diferencias entre los archivos modificados y el último commit

git checkout -- archivo.txt  # Deshace los cambios no confirmados en un archivo específico

git reset --soft HEAD~1  # Deshace el último commit, pero mantiene los cambios
git rm archivo.txt  # Elimina un archivo del repositorio y del sistema de archivos
