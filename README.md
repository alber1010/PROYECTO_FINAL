![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/c3e67109-6273-4e75-9288-fd1f7deb1054)







[# PROYECTO_FINAL] El siguiente link es el render.(https://proyecto-final-b2oj.onrender.com/docs)https://proyecto-final-b2oj.onrender.com/docs)

El siguiente link es el DEPLOYMENT. https://github.com/alber1010/DEPLOYMENT

El siguiente es el LINK del video https://drive.google.com/file/d/1PTmd_V165ACW7bySu0iWdQNZ3LP3falk/view?usp=sharing

Link de todos los datasets https://drive.google.com/drive/folders/1L4rr0ZFabXn9lDjs_7Y-lfPTDTpw0jXl?usp=sharing

Link de todos los Notebooks de Google Colab https://drive.google.com/drive/folders/1aszlj1r2LFucUdUsDSmMYBtllfz7ur1T?usp=sharing


PASO 1 CREACIÓN DEL DATA FRAME



Dado que los archivos son tan grandes, decidí realizar el proyecto en Google Colab. Los archivos se encontraban en formato JSON así que tuve que abrirlos de manera diferente, adicional a eso algunos tenían columnas anidadas y se tuvieron que desanidar según el caso específico.

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/5dea52ee-0ee4-43d1-ad35-c6c410154e59)

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/3e80ece0-081f-4344-ba32-17b9a0401b20)

Dado la composición de cada archivo, lo desanide de una manera diferente y también se hizo su respectivo tratamiento de datos.

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/c93090a1-e59d-4dfb-92c1-adf179b5d226)

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/5d6a30ec-4e45-4bd8-8a20-00ec652d3efd)

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/c66b0934-47f1-45df-aa4f-9fa28220cfac)

![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/54096a72-e41a-4245-9596-5a50dec6dbe7)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/7c0dcf10-eee4-4e47-94cc-5ab2429cdec1)


PASO 2 VERIFICAR OUTLIERS Y ANÁLISIS DE SENTIMIENTO.

Con un Data Frame unificado, empiezo a realizar un análisis para encontrar Outliers.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/dccc4d77-cd28-4ab2-92b8-216aa50f173b)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/9a8c6815-63f3-4a16-94f6-7005d72ed065)

También realizo el análisis de sentimiento a la columna Reviews.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/1f50d6b8-6f79-4a37-8284-d3e2ab784875)


PASO 3 CREACIÓN DE FUNCIONES.

Cree las funciones en Google Colab, pero luego necesite ajustarlas para que funcionaran en el Visual Studio Code, y así funcionaran en la API.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/90de4d62-c453-4794-84d1-e7c3f2aac384)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/9be0e97c-720b-4f1b-bb32-952aa4fee969)


PASO 4 ANÁLISIS DE DATOS.

Decidí crear una matriz de correlación.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/5e89c871-bccc-4fb8-b8e3-bd5b2c0d90ea)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/d869db80-893a-410e-b948-ada0c1319cdc)


PASO 5 MODELO DE MACHINE LEARNING

Elijo el modelo item-item, y elimino más filas que considero no me sirven.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/feee0c34-90f4-4e80-a734-18b0d5bcab1f)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/151cd290-82d2-40f9-a05a-d396b00153c0)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/51d0a263-54c3-4872-ad3f-56cb8bfca6b0)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/aef8d124-35bb-42af-8fd3-4670c0149388)


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/ae2c038e-ba2e-4223-9307-faf7cb93d5e3)

Creo el modelo de recomendación. Al igual que con las funciones debo ajustarlo para que funcione en el Visual Studio Code.


![imagen](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/970b0f8e-2c2d-40e5-b499-d586c9d59c88)


![image](https://github.com/alber1010/PROYECTO_FINAL/assets/112127531/10046737-e3a0-476a-a0cb-69b734a915e3)































