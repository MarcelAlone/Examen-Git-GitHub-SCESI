# Examen-Git-GitHub
¿Cómo genero mi llave SSH?
♦ Poniendo el comando "ssh-keygen" es útil para autenticarte con servidores remotos sin tener que introducir tu contraseña cada vez.

En el error de la rama "feature/sum_function " revierte de manera no destructiva hacia un commit antes del error encontrado para que todo esté con normalidad, ingresa en el siguiente campo el comando utilizado:
♦ "git revert HEAD" este  comando creará un nuevo commit que deshace los cambios introducidos en el último commit, llevando la rama de vuelta al estado anterior al error encontrado.

¿Para qué sirve git push --set-upstream <alias> <rama>?
♦Configura una relación de seguimiento entre una rama local y una rama remota, permitiendo que futuros "git push" y "git pull" se realicen de forma más sencilla sin necesidad de especificar la rama y el repositorio remoto cada vez.

Crea un alias interesante y explica su utilidad e implementación, escribe en el siguiente campo en el formato correspondiente:
- Comando para crear el alias 
- Comando creado (Ejemplo: git watch)
- Explicación de la utilidad del alias

No puedes utilizar git log --oneline --graph y similares a este
♦git config --global alias.graph explicacion: El alias "git graph" ofrece una visualización gráfica del historial de commits con ramas y relaciones entre ellos, simplificando la comprensión de la estructura del proyecto y el progreso del desarrollo. Es una herramienta valiosa para entender la evolución del proyecto de manera rápida y concisa.

En la rama "feature/sum_function" se produjo un error, ingresa en el siguiente campo el SHA del primer commit que introdujo este error
♦ Usamos este comando "git log --oneline feature/sum_function" que identifica el primer commit con el error en el historial y usa su SHA para obtener más información o revertir los cambios si es necesario.


