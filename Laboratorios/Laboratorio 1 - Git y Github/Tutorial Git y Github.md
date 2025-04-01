# ¿Qué es Git y qué es GitHub?

Git es un sistema de control de versiones que realiza un seguimiento de los cambios en los archivos.

En cambio, GitHub es una plataforma basada en la nube donde puedes almacenar, compartir y trabajar junto con otros usuarios para escribir código. Además, te permite hacer:

- Presentar o compartir el trabajo.
- Seguir y administrar los cambios en el código a lo largo del tiempo.
- Colaborar en un proyecto compartido.


# Comandos Básicos de Git

Git es un sistema de control de versiones distribuido que te permite gestionar el historial de versiones de tu proyecto. Aquí dejamos una lista de comandos que usaremos para el manejo de datos:

```bash
git config --global user.name "Tu Nombre"  # Configura tu nombre de usuario para que ingreses al repertorio
git config --global user.email "tu.email@example.com"  # Configura tu correo electrónico en caso no sepas tu nombre de usuario
git config también se puede usar para configurar comandos en alias, con el fin de simplificar los comando de ser necesarios, para esto la estructura es la siguiente
git config --global alias.ci commit   --> donde ci sería el nuevo comando y commmit es el nombre actual del comando, 

git init  # Inicializa un repositorio vacío en el directorio actual, es para crearlo

git clone https://github.com/usuario/repositorio.git  # Clona el repositorio remoto a tu máquina, tienes que iniciarlo desde donde quieres descargar el repositorio

git status  # Muestra los cambios no confirmados y el estado actual del repositorio, si es que no existe cambios sin confirmar también te avisará

git add archivo.txt  # Agrega un archivo específico al área de preparación, antes puedes comprobar que el archivo este en fit status
git add .  # Agrega todos los archivos modificados al área de preparación

git commit -m "Mensaje descriptivo del commit"  # Realiza un commit con un mensaje descriptivo, con esto estaremos confirmando el cambio en nuestro repertorio

git log  # Muestra el historial de commits del repositorio

git branch nombre-de-la-rama  # Crea una nueva rama en el repositorio por si deseamos trabajar con una copia, actualmente todo se trabaja en la rama main

git checkout nombre-de-la-rama  # Cambia a una rama existente
git checkout -b nueva-rama  # Crea y cambia a una nueva rama

git merge nombre-de-la-rama  # Fusiona la rama especificada con la rama actual, se le puede agregar un --no-ff antes del nombre de la rama 

git branch -d nombre-de-la-rama  # Elimina una rama que ya no necesitas

git push origin nombre-de-la-rama  # Envía los cambios locales a un repositorio remoto, para esto se debe si o sí haber hecho un commit de manera previa

git pull origin nombre-de-la-rama  # Obtiene los cambios más recientes desde el repositorio remoto, para esto debe estar conectado nuestro usuario

git diff  # Muestra las diferencias entre los archivos modificados y el último commit

git checkout -- archivo.txt  # Deshace los cambios no confirmados en un archivo específico

git reset --soft HEAD~1  # Deshace el último commit, pero mantiene los cambios

git rm archivo.txt  # Elimina un archivo del repositorio y del sistema de archivos

git blame archivo.txt  # Muestra quién fue el autor de cada línea de un archivo, esto puede ser importante para detectar los cambios
