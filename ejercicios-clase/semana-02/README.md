# Respuesta al laboratorio #2

Con este comando creo el entorno virtual en la carpeta llamada "semana-02"

```bash
python3 -m venv venv 
```

Después para activarlo se utiliza

```bash
venv\Scripts\activate
```

Revisé que la lista de librerias estuviera vacia con

```bash
pip list
```

Después de confirmalo, para los dos pasos finales, usé este comando para crear el archivo que permite reproducirlo en otras computadoras.

```bash
pip freeze > requirements.txt
```

Y este último para poder reproducirlo desde un entorno nuevvo sin librerias

```bash
pip install -r requirements.txt
```