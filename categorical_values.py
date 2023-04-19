import pandas as pd

# Marital status
ms_dict = {'Single': 1, 'Married': 2, 'Widower': 3, 'Divorced': 4, 'Facto Union': 5, 'Legally Seperated': 6}

# Application mode
am_dict = {
    '1st phase - general contingent': 1,
    'Ordinance No. 612/93': 2,
    '1st phase - special contingent (Azores Island)': 5,
    'Holders of other higher courses': 7,
    'Ordinance No. 854-B/99': 10,
    'International student (bachelor)': 15,
    '1st phase - special contingent (Madeira Island)': 16,
    '2nd phase - general contingent': 17,
    '3rd phase - general contingent': 18,
    'Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
    'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
    'Over 23 years old': 39,
    'Transfer': 42,
    'Change of course': 43,
    'Technological specialization diploma holders': 44,
    'Change of institution/course': 51,
    'Short cycle diploma holders': 53,
    'Change of institution/course (International)': 57
}

# Course
course_dict = {'Biofuel Production Technologies': 33, 'Animation and Multimedia Design': 171, 'Social Service (evening attendance)': 8014, 'Agronomy': 9003, 'Communication Design': 9070, 'Veterinary Nursing': 9085, 'Informatics Engineering': 9119, 'Equinculture': 9130, 'Management': 9147, 'Social Service': 9238, 'Tourism': 9254, 'Nursing': 9500, 'Oral Hygiene': 9556, 'Advertising and Marketing Management': 9670, 'Journalism and Communication': 9773, 'Basic Education': 9853, 'Management (evening attendance)': 9991}

# Daytime/evening attendance\t
de_attendance = {'Evening': 0, 'Daytime': 1}

# Previous qualification
pq_dict = {
    'Secondary education': 1,
    "Higher education - bachelor's degree": 2,
    'Higher education - degree': 3,
    "Higher education - master's": 4,
    'Higher education - doctorate': 5,
    'Frequency of higher education': 6,
    '12th year of schooling - not completed': 9,
    '11th year of schooling - not completed': 10,
    'Other - 11th year of schooling': 12,
    '10th year of schooling': 14,
    '10th year of schooling - not completed': 15,
    'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 19,
    'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 38,
    'Technological specialization course': 39,
    'Higher education - degree (1st cycle)': 40,
    'Professional higher technical course': 42,
    'Higher education - master (2nd cycle)': 43
}
    
# Nacionality
nacionality_dict = {
    'Portuguese': 1,
    'German': 2,
    'Spanish': 6,
    'Italian': 11,
    'Dutch': 13,
    'English': 14,
    'Lithuanian': 17,
    'Angolan': 21,
    'Cape Verdean': 22,
    'Guinean': 24,
    'Mozambican': 25,
    'Santomean': 26,
    'Turkish': 32,
    'Brazilian': 41,
    'Romanian': 62,
    'Moldova (Republic of)': 100,
    'Mexican': 101,
    'Ukrainian': 103,
    'Russian': 105,
    'Cuban': 108,
    'Colombian': 109
}

# Mothers qualification
mq_dict = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Technical-professional course": 22,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

# Fathers qualification
fq_dict = {
    "Secondary Education - 12th Year of Schooling or Eq.": 1,
    "Higher Education - Bachelor's Degree": 2,
    "Higher Education - Degree": 3,
    "Higher Education - Master's": 4,
    "Higher Education - Doctorate": 5,
    "Frequency of Higher Education": 6,
    "12th Year of Schooling - Not Completed": 9,
    "11th Year of Schooling - Not Completed": 10,
    "7th Year (Old)": 11,
    "Other - 11th Year of Schooling": 12,
    "2nd year complementary high school course": 13,
    "10th Year of Schooling": 14,
    "General commerce course": 18,
    "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
    "Complementary High School Course": 20,
    "Technical-professional course": 22,
    "Complementary High School Course - not concluded": 25,
    "7th year of schooling": 26,
    "2nd cycle of the general high school course": 27,
    "9th Year of Schooling - Not Completed": 29,
    "8th year of schooling": 30,
    "General Course of Administration and Commerce": 31,
    "Supplementary Accounting and Administration": 33,
    "Unknown": 34,
    "Can't read or write": 35,
    "Can read without having a 4th year of schooling": 36,
    "Basic education 1st cycle (4th/5th year) or equiv.": 37,
    "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
    "Technological specialization course": 39,
    "Higher education - degree (1st cycle)": 40,
    "Specialized higher studies course": 41,
    "Professional higher technical course": 42,
    "Higher Education - Master (2nd cycle)": 43,
    "Higher Education - Doctorate (3rd cycle)": 44
}

# Mothers occupation
mo_dict = {
    'Student': 0,
    'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
    'Specialists in Intellectual and Scientific Activities': 2,
    'Intermediate Level Technicians and Professions': 3,
    'Administrative staff': 4,
    'Personal Services, Security and Safety Workers and Sellers': 5,
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
    'Skilled Workers in Industry, Construction and Craftsmen': 7,
    'Installation and Machine Operators and Assembly Workers': 8,
    'Unskilled Workers': 9,
    'Armed Forces Professions': 10,
    'Other Situation': 90,
    '(blank)': 99,
    'Health professionals': 122,
    'Teachers': 123,
    'Specialists in information and communication technologies (ICT)': 125,
    'Intermediate level science and engineering technicians and professions': 131,
    'Technicians and professionals, of intermediate level of health': 132,
    'Intermediate level technicians from legal, social, sports, cultural and similar services': 134,
    'Office workers, secretaries in general and data processing operators': 141,
    'Data, accounting, statistical, financial services and registry-related operators': 143,
    'Other administrative support staff': 144,
    'Personal service workers': 151,
    'Sellers': 152,
    'Personal care workers and the like': 153,
    'Skilled construction workers and the like, except electricians': 171,
    'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like': 173,
    'Workers in food processing, woodworking, clothing and other industries and crafts': 175,
    'Cleaning workers': 191,
    'Unskilled workers in agriculture, animal production, fisheries and forestry': 192,
    'Unskilled workers in extractive industry, construction, manufacturing and transport': 193,
    'Meal preparation assistants': 194
}

# Fathers occupation
fo_dict = {
    'Student': 0,
    'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
    'Specialists in Intellectual and Scientific Activities': 2,
    'Intermediate Level Technicians and Professions': 3,
    'Administrative staff': 4,
    'Personal Services, Security and Safety Workers and Sellers': 5,
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
    'Skilled Workers in Industry, Construction and Craftsmen': 7,
    'Installation and Machine Operators and Assembly Workers': 8,
    'Unskilled Workers': 9,
    'Armed Forces Professions': 10,
    'Other Situation': 90,
    '(blank)': 99,
    'Armed Forces Officers': 101,
    'Armed Forces Sergeants': 102,
    'Other Armed Forces personnel': 103,
    'Directors of administrative and commercial services': 112,
    'Hotel, catering, trade and other services directors': 114,
    'Specialists in the physical sciences, mathematics, engineering and related techniques': 121,
    'Health professionals': 122,
    'Teachers': 123,
    'Specialists in finance, accounting, administrative organization, public and commercial relations': 124,
    'Intermediate level science and engineering technicians and professions': 131,
    'Technicians and professionals, of intermediate level of health': 132,
    'Intermediate level technicians from legal, social, sports, cultural and similar services': 134,
    'Information and communication technology technicians': 135,
    'Office workers, secretaries in general and data processing operators': 141,
    'Data, accounting, statistical, financial services and registry-related operators': 143,
    'Other administrative support staff': 144,
    'Personal service workers': 151,
    'Sellers': 152,
    'Personal care workers and the like': 153,
    'Protection and security services personnel': 154,
    'Market-oriented farmers and skilled agricultural and animal production workers': 161,
    'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence': 163,
    'Skilled construction workers and the like, except electricians': 171,
    'Skilled workers in metallurgy, metalworking and similar': 172,
    'Skilled workers in electricity and electronics': 174,
    'Workers in food processing, woodworking, clothing and other industries and crafts': 175,
    'Fixed plant and machine operators': 181,
    'Assembly workers': 182,
    'Vehicle drivers and mobile equipment operators': 183,
    'Unskilled workers in agriculture, animal production, fisheries and forestry': 192,
    'Unskilled workers in extractive industry, construction, manufacturing and transport': 193,
    'Meal preparation assistants': 194,
    'Street vendors (except food) and street service providers': 195
}

# Displaced
displaced_dict = {
    'No': 0,
    'Yes': 1
}

# Educational special needs
esn_dict = {
    'No': 0,
    'Yes': 1
}

# Debtor
debtor_dict = {
    'No': 0,
    'Yes': 1
}

# Tuiton fees up to date
tfd_dict = {
    'No': 0,
    'Yes': 1
}

# Gender
gender_dict = {
    'Mujer': 0,
    'Hombre': 1
}

# Scholarship holder
scholarship_dict = {
    'No': 0,
    'Yes': 1
}

# International
international_dict = {
    'No': 0,
    'Yes': 1
}

def transform_data(data):
    prepared = pd.DataFrame({
        'Marital status': [ms_dict[data['marital_status']]],
        'Application mode': [am_dict[data['application_mode']]],
        'Application order': [data['application_order']],
        'Course': [course_dict[data['course']]],
        'Daytime/evening attendance\t': [de_attendance[data['attendance_type']]],
        'Previous qualification': [pq_dict[data['previous_qualification']]],
        'Previous qualification (grade)': [data['previous_qualification_grade']],
        'Nacionality': [nacionality_dict[data['nacionality']]],
        "Mother's qualification": [mq_dict[data['mothers_qualification']]],
        "Father's qualification": [fq_dict[data['fathers_qualification']]],
        "Mother's occupation": [mo_dict[data['mothers_occupation']]],
        "Father's occupation": [fo_dict[data['fathers_occupation']]],
        'Admission grade': [data['admission_grade']],
        'Displaced': [displaced_dict[data['displaced']]],
        'Educational special needs': [esn_dict[data['educational_special_needs']]],
        'Debtor': [debtor_dict[data['debtor']]],
        'Tuition fees up to date': [tfd_dict[data['tuition_fees_up_to_date']]],
        'Gender': [gender_dict[data['gender']]],
        'Scholarship holder': [scholarship_dict[data['scholarship_holder']]],
        'Age at enrollment': [data['age_at_enrollment']],
        'International': [international_dict[data['international']]],
        'Curricular units 1st sem (credited)': [data['curricular_units_1st_semester_credited']],
        'Curricular units 1st sem (enrolled)': [data['curricular_units_1st_semester_enrolled']],
        'Curricular units 1st sem (evaluations)': [data['curricular_units_1st_semester_evaluations']],
        'Curricular units 1st sem (approved)': [data['curricular_units_1st_semester_approved']],
        'Curricular units 1st sem (grade)': [data['curricular_units_1st_semester_grade']],
        'Curricular units 1st sem (without evaluations)': [data['curricular_units_1st_semester_without_evaluation']],
        'Curricular units 2nd sem (credited)': [data['curricular_units_2nd_semester_credited']],
        'Curricular units 2nd sem (enrolled)': [data['curricular_units_2nd_semester_enrolled']],
        'Curricular units 2nd sem (evaluations)': [data['curricular_units_2nd_semester_evaluations']],
        'Curricular units 2nd sem (approved)': [data['curricular_units_2nd_semester_approved']],
        'Curricular units 2nd sem (grade)': [data['curricular_units_2nd_semester_grade']],
        'Curricular units 2nd sem (without evaluations)': [data['curricular_units_2nd_semester_without_evaluation']],
        'Unemployment rate': [data['unemployment_rate']],
        'Inflation rate': [data['inflation_rate']],
        'GDP': [data['gdp']]
    })
    return prepared