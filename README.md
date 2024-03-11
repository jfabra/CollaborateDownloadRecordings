# CollaborateDownloadRecordings
Una colección de Bash scripts para descargar grabaciones de Collab.

Por una parte, están estos scripts sencillos, escritos en Bash y que se basan en el siguiente ciclo:
1. Descargar el RecordingReport (se puede hacer por lotes)
2. La columna que nos interesa es la que tiene de cabecera RecordingLink. Con un cut + wget, podemos descargar directamente los vídeos a un directorio. 
3. Asociamos la información del directorio con la descarga. Para eso, usamos los scripts Python

Si queremos hacer algo más elaborado, podemos utilizar el set de scripts de Python que interaccionan directamente con el API de Collaborate, https://github.com/sfc-gh-csuarez/PyCollab y https://github.com/SimonXIX/BulkExportBBCollaborateRecordings (es un fork del primero, que permite gestionar las descargas de las grabaciones).



