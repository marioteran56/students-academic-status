import streamlit as st
import pandas as pd
from prediction import predict
import joblib

st.title('Prediciendo el estado académico de los estudiantes')
st.markdown('Se tienen multiples modelos entrenados para la predicción del exito académico de los estudiantes y abandono escolar, se puede seleccionar el modelo que se desea utilizar para la predicción.')

# Slider en la página principal para seleccionar el modelo
st.sidebar.header('Clasificadores')
model = st.sidebar.selectbox('', ['Support Vector Classifier', 'Random Forest Classifier', 'Extra Trees Classifier'])

# Resultados del modelo seleccionado
model_results = []
if model == 'Support Vector Classifier':
    model_results = joblib.load('models/svc_clf_results.pkl')
elif model == 'Random Forest Classifier':
    model_results = joblib.load('models/rfc_clf_results.pkl')
elif model == 'Extra Trees Classifier':
    model_results = joblib.load('models/etc_clf_results.pkl')
    
st.sidebar.text(f'Accuracy: {model_results[0]}')
st.sidebar.text(f'👌 Precision: {model_results[1]}')
st.sidebar.text(f'Recall: {model_results[2]}')
st.sidebar.text(f'F1 Score: {model_results[3]}')

st.header('Datos del alumno')
col1, col2 = st.beta_columns(2)
with col1:
    marital_status = st.selectbox('Estado civil', ['Single','Married','Widower','Divorced','Facto Union','Legally Seperated'], index=0)
    application_mode = st.selectbox('Modo de solicitud', ['1st phase - general contingent', 'Ordinance No. 612/93', '1st phase - special contingent (Azores Island)', 'Holders of other higher courses', 'Ordinance No. 854-B/99', 'International student (bachelor)', '1st phase - special contingent (Madeira Island)', '2nd phase - general contingent', '3rd phase - general contingent', 'Ordinance No. 533-A/99, item b2) (Different Plan)', 'Ordinance No. 533-A/99, item b3 (Other Institution)', 'Over 23 years old', 'Transfer', 'Change of course', 'Technological specialization diploma holders', 'Change of institution/course', 'Short cycle diploma holders', 'Change of institution/course (International)'], index=5)
    application_order = st.slider('Orden de solicitud', 0, 9, 1, 1)
    course = st.selectbox('Curso', ['Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service (evening attendance)', 'Agronomy', 'Communication Design', 'Veterinary Nursing', 'Informatics Engineering', 'Equinculture', 'Management', 'Social Service', 'Tourism', 'Nursing', 'Oral Hygiene', 'Advertising and Marketing Management', 'Journalism and Communication', 'Basic Education', 'Management (evening attendance)'], index=10)
    attendance_type = st.selectbox('Tipo de asistencia', ['Evening', 'Daytime'], index=1)
    previous_qualification = st.selectbox('Educación previa', ['Secondary education', 'Higher education - bachelors degree', 'Higher education - degree', 'Higher education - masters', 'Higher education - doctorate', 'Frequency of higher education', '12th year of schooling - not completed', '11th year of schooling - not completed', 'Other - 11th year of schooling', '10th year of schooling', '10th year of schooling', 'Basic education 3rd cycle (9th/10th/11th year) or equiv.', 'Basic education 2nd cycle (6th/7th/8th year) or equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Professional higher technical course', 'Higher education - master (2nd cycle)'], index=0)
    previous_qualification_grade = st.slider('Grado de educación previa', 0, 200, 160, 1)
    nacionality = st.selectbox('Nacionalidad', ['Portuguese', 'German', 'Spanish', 'Italian', 'Dutch', 'English', 'Lithuanian', 'Angolan', 'Cape Verdean', 'Guinean', 'Mozambican', 'Santomean', 'Turkish', 'Brazilian', 'Romanian', 'Moldova (Republic of)', 'Mexican', 'Ukrainian', 'Russian', 'Cuban', 'Colombian'], index=0)
    mothers_qualification = st.selectbox('Calificación de la madre', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelors Degree', 'Higher Education - Degree', 'Higher Education - Masters', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'], index=0)
    fathers_qualification = st.selectbox('Calificación del padre', ['Secondary Education - 12th Year of Schooling or Eq.', 'Higher Education - Bachelors Degree', 'Higher Education - Degree', 'Higher Education - Masters', 'Higher Education - Doctorate', 'Frequency of Higher Education', '12th Year of Schooling - Not Completed', '11th Year of Schooling - Not Completed', '7th Year (Old)', 'Other - 11th Year of Schooling', '10th Year of Schooling', 'General commerce course', 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.', 'Technical-professional course', '7th year of schooling', '2nd cycle of the general high school course', '9th Year of Schooling - Not Completed', '8th year of schooling', 'Unknown', 'Can\'t read or write', 'Can read without having a 4th year of schooling', 'Basic education 1st cycle (4th/5th year) or equiv.', 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.', 'Technological specialization course', 'Higher education - degree (1st cycle)', 'Specialized higher studies course', 'Professional higher technical course', 'Higher Education - Master (2nd cycle)', 'Higher Education - Doctorate (3rd cycle)'], index=2)
    mothers_occupation = st.selectbox('Ocupación de la madre', [    "Student",    "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",    "Specialists in Intellectual and Scientific Activities",    "Intermediate Level Technicians and Professions",    "Administrative staff",    "Personal Services, Security and Safety Workers and Sellers",    "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",    "Skilled Workers in Industry, Construction and Craftsmen",    "Installation and Machine Operators and Assembly Workers",    "Unskilled Workers",    "Armed Forces Professions",    "Other Situation",    "(blank)",    "Health professionals",    "teachers",    "Specialists in information and communication technologies (ICT)",    "Intermediate level science and engineering technicians and professions",    "Technicians and professionals, of intermediate level of health",    "Intermediate level technicians from legal, social, sports, cultural and similar services",    "Office workers, secretaries in general and data processing operators",    "Data, accounting, statistical, financial services and registry-related operators",    "Other administrative support staff",    "personal service workers",    "sellers",    "Personal care workers and the like",    "Skilled construction workers and the like, except electricians",    "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",    "Workers in food processing, woodworking, clothing and other industries and crafts",    "cleaning workers",    "Unskilled workers in agriculture, animal production, fisheries and forestry",    "Unskilled workers in extractive industry, construction, manufacturing and transport",    "Meal preparation assistants"], index=3)
    fathers_occupation = st.selectbox('Ocupación del padre', ['Student', 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers', 'Specialists in Intellectual and Scientific Activities', 'Intermediate Level Technicians and Professions', 'Administrative staff', 'Personal Services, Security and Safety Workers and Sellers', 'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry', 'Skilled Workers in Industry, Construction and Craftsmen', 'Installation and Machine Operators and Assembly Workers', 'Unskilled Workers', 'Armed Forces Professions', 'Other Situation', '(blank)', 'Armed Forces Officers', 'Armed Forces Sergeants', 'Other Armed Forces personnel', 'Directors of administrative and commercial services', 'Hotel, catering, trade and other services directors', 'Specialists in the physical sciences, mathematics, engineering and related techniques', 'Health professionals', 'teachers', 'Specialists in finance, accounting, administrative organization, public and commercial relations', 'Intermediate level science and engineering technicians and professions', 'Technicians and professionals, of intermediate level of health', 'Intermediate level technicians from legal, social, sports, cultural and similar services', 'Information and communication technology technicians', 'Office workers, secretaries in general and data processing operators', 'Data, accounting, statistical, financial services and registry-related operators', 'Other administrative support staff', 'personal service workers', 'sellers', 'Personal care workers and the like', 'Protection and security services personnel', 'Market-oriented farmers and skilled agricultural and animal production workers', 'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence', 'Skilled construction workers and the like, except electricians', 'Skilled workers in metallurgy, metalworking and similar', 'Skilled workers in electricity and electronics', 'Workers in food processing, woodworking, clothing and other industries and crafts', 'Fixed plant and machine operators', 'assembly workers', 'Vehicle drivers and mobile equipment operators', 'Unskilled workers in agriculture, animal production, fisheries and forestry', 'Unskilled workers in extractive industry, construction, manufacturing and transport', 'Meal preparation assistants', 'Street vendors (except food) and street service providers'], index=3)
    admision_grade = st.slider('Grado de admisión', 0.0, 200.0, 142.5, 0.5)
    displaced = st.selectbox('Desplazado', ['No', 'Yes'], index=1)
    educational_special_needs = st.selectbox('Necesidades educativas especiales', ['No', 'Yes'], index=0)
    debtor = st.selectbox('Deudor', ['No', 'Yes'], index=0)
    tuition_fees_up_to_date = st.selectbox('Cuotas de matrícula al día', ['No', 'Yes'], index=0)
    gender = st.selectbox('Genero', ['Mujer', 'Hombre'], index=1)
    scholarship_holder = st.selectbox('Becario', ['No', 'Yes'], index=0)
with col2:
    age_at_enrollment = st.slider('Edad al inscribirse', 0, 100, 19, 1)
    international = st.selectbox('Internacional', ['No', 'Yes'], index=0)
    curricular_units_1st_semester_credited = st.number_input('Unidades curriculares del primer semestre acreditadas', 0, 100, 0, 1)
    curricular_units_1st_semester_enrolled = st.number_input('Unidades curriculares del primer semestre inscritas', 0, 100, 6, 1)
    curricular_units_1st_semester_evaluations = st.number_input('Unidades curriculares del primer semestre evaluadas', 0, 100, 6, 1)
    curricular_units_1st_semester_approved = st.number_input('Unidades curriculares del primer semestre aprobadas', 0, 100, 6, 1)
    curricular_units_1st_semester_grade = st.slider('Grado de las unidades curriculares del primer semestre', 0.0, 20.0, 14.0, 1.0)
    curricular_units_1st_semester_without_evaluation = st.number_input('Unidades curriculares del primer semestre sin evaluación', 0, 100, 0, 1)
    curricular_units_2nd_semester_credited = st.number_input('Unidades curriculares del segundo semestre acreditadas', 0, 100, 0, 1)
    curricular_units_2nd_semester_enrolled = st.number_input('Unidades curriculares del segundo semestre inscritas', 0, 100, 6, 1)
    curricular_units_2nd_semester_evaluations = st.number_input('Unidades curriculares del segundo semestre evaluadas', 0, 100, 6, 1)
    curricular_units_2nd_semester_approved = st.number_input('Unidades curriculares del segundo semestre aprobadas', 0, 100, 6, 1)
    curricular_units_2nd_semester_grade = st.slider('Grado de las unidades curriculares del segundo semestre', 0.0, 20.0, 14.0, 1.0)
    curricular_units_2nd_semester_without_evaluation = st.number_input('Unidades curriculares del segundo semestre sin evaluación', 0, 100, 0, 1)
    unemployment_rate = st.slider('Tasa de desempleo', 0.0, 100.0, 13.0, 1.0)
    inflation_rate = st.slider('Tasa de inflación', -100.0, 100.0, 0.0, 1.0)
    gdp = st.slider('PIB', 0.0, 1000.0, 1.0, 1.0)

if st.button('Predecir el estado académico'):
    data = {
            'marital_status': marital_status,
            'application_mode': application_mode,
            'application_order': application_order,
            'course': course,
            'attendance_type': attendance_type,
            'previous_qualification': previous_qualification,
            'previous_qualification_grade': previous_qualification_grade,
            'nacionality': nacionality,
            'mothers_qualification': mothers_qualification,
            'fathers_qualification': fathers_qualification,
            'mothers_occupation': mothers_occupation,
            'fathers_occupation': fathers_occupation,
            'admission_grade': admision_grade,
            'displaced': displaced,
            'educational_special_needs': educational_special_needs,
            'debtor': debtor,
            'tuition_fees_up_to_date': tuition_fees_up_to_date,
            'gender': gender,
            'scholarship_holder': scholarship_holder,
            'age_at_enrollment': age_at_enrollment,
            'international': international,
            'curricular_units_1st_semester_credited': curricular_units_1st_semester_credited,
            'curricular_units_1st_semester_enrolled': curricular_units_1st_semester_enrolled,
            'curricular_units_1st_semester_evaluations': curricular_units_1st_semester_evaluations,
            'curricular_units_1st_semester_approved': curricular_units_1st_semester_approved,
            'curricular_units_1st_semester_grade': curricular_units_1st_semester_grade,
            'curricular_units_1st_semester_without_evaluation': curricular_units_1st_semester_without_evaluation,
            'curricular_units_2nd_semester_credited': curricular_units_2nd_semester_credited,
            'curricular_units_2nd_semester_enrolled': curricular_units_2nd_semester_enrolled,
            'curricular_units_2nd_semester_evaluations': curricular_units_2nd_semester_evaluations,
            'curricular_units_2nd_semester_approved': curricular_units_2nd_semester_approved,
            'curricular_units_2nd_semester_grade': curricular_units_2nd_semester_grade,
            'curricular_units_2nd_semester_without_evaluation': curricular_units_2nd_semester_without_evaluation,
            'unemployment_rate': unemployment_rate,
            'inflation_rate': inflation_rate,
            'gdp': gdp
        }
    
    if model == 'Support Vector Classifier':
        result = predict(data, 'svc_clf.pkl')
    elif model == 'Random Forest Classifier':
        result = predict(data, 'rfc_clf.pkl')
    elif model == 'Extra Trees Classifier':
        result = predict(data, 'etc_clf.pkl')
    
    target = {
        0: 'Desertor',
        1: 'Cursando',
        2: 'Graduado'
    }
    
    st.subheader('Resultado')
    st.text(f'Se estima que el estudiante se encuentra en el estado académico: {target[result[0]]}')

st.header('Conclusiones')
st.markdown('Tras entrenar los modelos de clasificación, se obtuvieron los resultados muy similares. No obstante, no se logró obtener un modelo que pudiera predecir con una precisión mayor al 73%, siendo el de Suport Vector Machine el que obtuvo el mejor resultado.')
st.markdown('Tras analizar trabajos similares que se han realizado con este dataset, se pudo observar que la mayoría de los modelos que se han entrenado han obtenido resultados similares a los obtenidos en este trabajo. Esto se debe a que el dataset no es muy grande y se encuentran los datos un poco desbalanceados, lo que dificulta la predicción de los modelos.')
st.markdown('Sin embargo, es posible obtener una mayor precisión en la predicción de los modelos si es que se elimina la clase de estudiantes que se encuentran cursando, ya que se puede considerar que son muy pocos los datos de esta clase.')
st.markdown('A continuación, se proporciona un enlace a Kaggle donde se encuentra un ejemplo de un modelo que se entrenó con dichas modificaciones: https://www.kaggle.com/code/paulandrewpaglinawan/eda-and-prediction-of-student-academic-success')