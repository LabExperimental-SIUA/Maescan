# Librescan

Librescan es un flujo de trabajo que combina varios programas para facilitar el proceso de digitalizar un documento.

Este proceso en particular consta de la captura de varias fotos que son procesadas para la obtención de un producto digital resultante, por ejemplo un PDF. 

LibreScan brinda una interfaz amigable y fácil de utilizar para la administración de las imágenes capturadas y un procesamiento eficiente.

Actualmente se cuenta con una versión en línea de comandos. En la carpeta presentationPrototype se puede visualizar cómo será la interfaz gráfica web en la que estamos trabajando.

### Instalación de LibreScan
- Instalar dependencias que serán utilizadas:

        # apt-get install python-pip lua5.2 liblua5.2 git-svn libusb-dev python3.4 libmagickwand-dev

        # pip3 install pyYAML Pillow bottle pyjade jinja2

---

- Instalar tesseract-ocr para el reconocimiento de texto:

        # apt-get install tesseract-ocr

    Nota: Para más idiomas se instala de esta forma (Ejemplo con español)
    
        # apt-get install tesseract-ocr-spa (Para Español)

---

- Instalar scantailor para el procesamiento de las fotos:

        # apt-get install scantailor
    
    Nota: Si no se encuentra el package (mensaje de "Unable to locate package xyz") se debe hacer lo siguiente:
    
        # nano /etc/apt/sources.list
        
    y agregar la siguiente linea al final del archivo 
    "deb http://http.debian.net/debian wheezy-backports main" (sin comillas).

    

---

- Instalar pdfbeads para generar pdfs a partir de tifs+hocr:

        # apt-get install ruby1.9.1 ruby-dev ruby-rmagick 
        # gem install iconv pdfbeads


---
- En cuanto a las cámaras hay que instalar el CHDKPTP en el sistema.

        $ git svn clone http://subversion.assembla.com/svn/chdkptp/trunk chdkptp

        $ cd chdkptp
    
        $ mv config-sample-linux.mk config.mk

        $ make

        # mkdir /usr/bin/chdkptp

        # cp chdkptp-sample.sh /usr/bin/chdkptp/chdkptp

        # nano /usr/bin/chdkptp/chdkptp

    Modificar la línea que dice
    
    CHDKPTP_DIR=/home/ruta_clonado/chdkptp (Y guardamos los cambios)
    
     por la ruta donde fue clonado el chdkptp.

        # ln -s /usr/bin/chdkptp/chdkptp /bin

---

- Para reconocer cuál cámara es la derecha y cuál es la izquierda hacemos uso de un archivo 'orientation.txt', que se encuentra almacenado la raíz de la tarjeta SD de cada cámara. Por ahora este proceso se debe hacer manualmente, introduciendo la SD en la computadora y creando el archivo manualmente. Pasos:
    
    1. Asegurarse que la SD esté desbloqueada.
    2. Para la cámara que desea usar al lado izquierdo, crear un archivo orientation.txt que tenga la palabra 'left' (sin comillas) como contenido.
    3. Para la cámara que desea usar al lado derecho, crear un archivo orientation.txt que tenga la palabra 'right' (sin comillas) como contenido.

- Nota: Estamos trabajando en automatizar este proceso, de modo que se el usuario conecte las cámaras y decida la orientación sin crear el archivo manualmente.

---

- Una vez instaladas todas las dependencias, procedemos a clonar el repositorio de LibreScan (por ahora el del branch develop).

        $ git clone https://github.com/LabExperimental-SIUA/LibreScan/tree/develop

- Nos metemos a la carpeta clonada y al código fuente.

        $ cd LibreScan/src

- Corremos el setup para la creación de carpetas y archivos de configuración.

        $ python3.4 setup.py

    Esto crea dos carpetas en el home/nombreusuario, una oculta llamada .librescan con archivos de configuración, y la otra se llama LibreScanProjects, donde se almacenarán todos los proyectos.

- Ejecutamos el programa (en línea de comandos por ahora). Es necesario tener las cámaras en posición y encendidas, además de conectadas a la computadora.

        $ python3.4 main.py


