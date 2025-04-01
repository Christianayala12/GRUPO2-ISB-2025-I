# ¿Qué es Git y qué es GitHub?

**Git** es un sistema de control de versiones que realiza un seguimiento de los cambios en los archivos.

En cambio, **GitHub** es una plataforma basada en la nube donde puedes almacenar, compartir y trabajar junto con otros usuarios para escribir código. Además, te permite hacer:

- Presentar o compartir el trabajo.
- Seguir y administrar los cambios en el código a lo largo del tiempo.
- Colaborar en un proyecto compartido.


# Comandos Básicos de Git

Git es un sistema de control de versiones distribuido que te permite gestionar el historial de versiones de tu proyecto. Aquí dejamos una lista de comandos que usaremos para el manejo de datos:

## 1. Configura tu nombre de usuario para que ingreses al repertorio
```bash
git config --global user.name "Tu Nombre" 
```

## 2. Configura tu correo electrónico en caso no sepas tu nombre de usuario
```bash
git config --global user.email "tu.email@example.com"
```
### El git config también se puede usar para configurar comandos en alias, con el fin de simplificar los comando de ser necesarios, para esto la estructura es la siguiente:

```bash
git config --global alias.ci commit
```
Donde ci sería el nuevo comando y commmit es el nombre actual del comando.

## 3. Inicializa un repositorio vacío en el directorio actual, es para crearlo
```bash
git init
```

## 4. Clona el repositorio remoto a tu máquina, tienes que iniciarlo desde donde quieres descargar el repositorio
```bash
git clone https://github.com/usuario/repositorio.git
```

## 5. Muestra los cambios no confirmados y el estado actual del repositorio, si es que no existe cambios sin confirmar también te avisará
```bash
git status
```

## 6. Agrega un archivo específico al área de preparación, antes puedes comprobar que el archivo este en fit status
```bash
git add archivo.txt
```
Pero si deseas agregar todos los archivos modificados al área de preparación, el comando es el siguiente>
```bash
git add .
```

## 7. Realiza un commit con un mensaje descriptivo, con esto estaremos confirmando el cambio en nuestro repertorio
```bash
git commit -m "Mensaje descriptivo del commit" 
```

## 8. Muestra el historial de commits del repositorio
```bash
git log
```

## 9. Crea una nueva rama en el repositorio por si deseamos trabajar con una copia, actualmente todo se trabaja en la rama main
```bash
git branch nombre-de-la-rama
```

## 10. Cambia a una rama existente
```bash
git checkout nombre-de-la-rama
```
###Pero para crear y cambiar a una nueva rama, es>
```bash
git checkout -b nueva-rama
```

## 11. Fusiona la rama especificada con la rama actual, se le puede agregar un --no-ff antes del nombre de la rama 
```bash
git merge nombre-de-la-rama
```

## 12. Elimina una rama que ya no necesitas
```bash
git branch -d nombre-de-la-rama
```

## 13. Envía los cambios locales a un repositorio remoto, para esto se debe si o sí haber hecho un commit de manera previa
```bash
git push origin nombre-de-la-rama 
```

## 14. Obtiene los cambios más recientes desde el repositorio remoto, para esto debe estar conectado nuestro usuario
```bash
git pull origin nombre-de-la-rama
```

## 15. Muestra las diferencias entre los archivos modificados y el último commit
```bash
git diff
```

## 16. Deshace los cambios no confirmados en un archivo específico
```bash
git checkout -- archivo.txt 
```

## 17. Deshace el último commit, pero mantiene los cambios
```bash
git reset --soft HEAD~1
```

## 18. Elimina un archivo del repositorio y del sistema de archivos
```bash
git rm archivo.txt
```

## 19. Muestra quién fue el autor de cada línea de un archivo, esto puede ser importante para detectar los cambios
```bash
git blame archivo.txt
```

# REFERENCIAS
[1] https://docs.github.com/es/get-started/start-your-journey/about-github-and-git

