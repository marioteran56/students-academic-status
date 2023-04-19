# Proyecto para la predicción del estado académico de los estudiantes

![Class image](https://s35691.pcdn.co/wp-content/uploads/2019/11/Implementing-active-learning-and-student-centered-pedagogy.jpg)

## Objetivo

El objetivo de este proyecto es entrenar una serie de modelos de clasificación, como Suport Vector Classifier, Desicion Tree Classifiery Random Forest Classifier, para predecir si un alumno se graduó de la universidad, abandonó la universidad, o se encuentra cursando actualmente. Para ello, se utilizará el dataset de [Predict students' dropout and academic success](https://marioteran56-students-academic-status-app-gkik16.streamlit.app/) de Kaggle.

De esta manera, se crea un proyecto con Streamlit para que el usuario pueda ingresar los datos del estudiante para predecir su estado académico. Dicho proyecto se encuentra disponible en la siguiente liga de [Streamlit](https://marioteran56-students-academic-status-app-gkik16.streamlit.app/)

## Requerimientos

El proyecto est disponible en la liga de [Streamlit](https://marioteran56-students-academic-status-app-gkik16.streamlit.app/). No obstante, si se desea correr el proyecto en local, se requiere de los siguientes paquetes instalados dentro de nuestro entorno virtual:

- streamlit
- pandas
- numpy
- sklearn
- joblib

Por otro lado, si deseas reentrenar los modelos dentro de nuestro archivo de Jupyter Notebook, se requiere de los siguientes paquetes adicionales:

- matplotlib

## Uso

Para correr el proyecto de manera local, se debe abrir la terminal y dirigirse a la carpeta donde se encuentra el archivo `app.py`. Una vez ahí, se debe correr el siguiente comando:

```bash
streamlit run app.py
```
