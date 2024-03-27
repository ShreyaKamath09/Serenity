import random
import time

import joblib
import numpy as np
import pandas as pd
import streamlit as st
import xgboost


def main():
    st.title("Mental Health in Tech Industry")
    st.caption("Experiencing persistent feeling of stress, anxiety, or burnout in your workplace? "
               "You came to the right place!")
    st.markdown('---')
    menu = ['Home', 'About Us']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == 'Home':
        st.subheader('Take a Test, you might need some help!')
        # show_form = st.button("Start the test!")
        # if show_form:
        columns = ['Age', 'Gender', 'Self_Employed',
                   'Family_History',
                   'Work_Interference', 'Employees_Num', 'Remote_Working',
                   'Technology_Company', 'Company_Benefits', 'Healthcare_Options',
                   'Wellness_Program', 'Resources', 'Anonymity', 'Medical_Leave',
                   'Mental_Consequence', 'Physical_Consequence', 'Discuss_Coworkers',
                   'Discuss_Supervisor', 'Mental_Interview', 'Physical_Interview',
                   'Mental_VS_Physical', 'Observed_Consequence']
        df = pd.DataFrame(index=range(1), columns=columns)

        with st.form("Form"):

            df['Age'] = st.number_input('How old are you?', step=1.0, format='%.0f', min_value=15.0, max_value=100.0)
            df['Gender'] = st.selectbox('What is your gender?', ['Female', 'Male', 'Others'])
            df['Self_Employed'] = st.selectbox('Are you currently employed (part time/full time)?', ['Yes', 'No'])
            df['Family_History'] = st.selectbox('Do your family members have mental illness history?', ['No', 'Yes'])
            df['Work_Interference'] = st.select_slider('How often do you feel stressed out lately?',
                                                       options=['Never', 'Rarely', 'Sometimes', 'Often'])
            df['Employees_Num'] = st.select_slider('How many classmates do you have?',
                                       ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
            df['Remote_Working'] = st.selectbox('Are you attending classes remotely? (At least 50% of the time)', ['No', 'Yes'])
            df['Technology_Company'] = st.selectbox('Do you feel your mental health is impacting your academic performance?',
                                                    ['No', 'Yes'])
            df['Company_Benefits'] = st.selectbox('Does your employer provide mental health benefits?',
                                                  ['No', 'Yes', 'Don\'t know'])
            df['Healthcare_Options'] = st.selectbox('Do you know the options for mental health care your employer '
                                                    'provides?', ['No', 'Yes', 'Not Sure'])
            df['Wellness_Program'] = st.selectbox('Has your employer ever discussed mental health as part of '
                                                  'an employee wellness program?', ['No', 'Yes', 'Don\'t know'])
            df['Resources'] = st.selectbox('Does your employer provide resources to learn more about mental health '
                                           'issues and how to seek help?', ['No', 'Yes', 'Don\'t know'])
            df['Anonymity'] = st.selectbox('Is your anonymity protected if you choose to take advantage of mental '
                                           'health or substance abuse treatment resources?', ['No', 'Yes', 'Don\'t know'])
            df['Medical_Leave'] = st.select_slider('How easy is it for you to take medical leave for a mental health '
                                                   'condition?', options=['Very Easy', 'Somewhat Easy', 'Don\'t Know',
                                                                          'Somewhat Difficult', 'Very Difficult'])
            df['Mental_Consequence'] = st.selectbox('Do you think that discussing a mental health issue with your '
                                                    'employer would have negative consequences?',
                                                    ['No', 'Yes', 'Maybe'])
            df['Physical_Consequence'] = st.selectbox('Do you think that discussing a physical health issue with your '
                                                      'employer would have negative consequences?', ['No', 'Yes',
                                                                                                     'Maybe'])
            df['Discuss_Coworkers'] = st.selectbox('Would you be willing to discuss a mental health issue with your '
                                                   'coworkers?', ['No', 'Yes', 'Some of them'])
            df['Discuss_Supervisor'] = st.selectbox('Would you be willing to discuss a mental health issue with your '
                                                    'direct supervisor(s)?', ['No', 'Yes', 'Some of them'])
            df['Mental_Interview'] = st.selectbox('Would you bring up a mental health issue with a potential employer '
                                                  'in an interview?', ['No', 'Yes', 'Maybe'])
            df['Physical_Interview'] = st.selectbox('Would you bring up a physical health issue with a potential '
                                                    'employer in an interview?', ['No', 'Yes', 'Maybe'])
            df['Mental_VS_Physical'] = st.selectbox('Do you feel that your employer takes mental health as seriously '
                                                    'as physical health?', ['No', 'Yes', 'Don\'t Know'])
            df['Observed_Consequence'] = st.selectbox('Have you heard of or observed negative consequences for '
                                                      'coworkers with mental health conditions in your workplace?',
                                                      ['No', 'Yes'])

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                test = pd.read_csv("output.csv")
                test = test.loc[:, test.columns != 'Seek_Treatment']
                test.loc[len(test)] = df.loc[0]

                model = joblib.load('model.pkl')
                scaler = joblib.load('scaler1.pkl')

                for column in test.columns:
                    if column == 'Age' or column == 'Seek_Treatment':
                        continue
                    else:
                        encoder = joblib.load(f'{column}_encoder.pkl')
                        test[column] = encoder.fit_transform(test[column])

                test[['Age']] = scaler.transform(test[['Age']])
                user_input = np.array([test.loc[len(test)-1]])
                # st.write(user_input)

                proba = model.predict_proba(user_input)
                prediction = model.predict(user_input)
                probability = proba[0, 1]
                progress = 0
                st.success("Form Submitted")
                progress_text = st.empty()
                progress_container = st.empty()
                while progress <= probability * 100:
                    time.sleep(0.008)
                    progress += 1
                    progress_container.progress(progress)
                    progress_text.subheader(f"Probability: {progress:.2f} %")
                progress_text.subheader(f"Probability: {probability*100:.2f} %")

                if prediction < 0.25:
                    msgs = ["It seems like you're currently in a good mental state and managing well. Continue to "
                            "prioritize self-care and maintain healthy habits to support your overall well-being.",
                            "Your mental well-being appears to be strong, but remember to seek support if you ever "
                            "feel overwhelmed or need someone to talk to."]
                    rand = random.randint(0, 1)
                    msg = msgs[rand]
                elif prediction < 0.5:
                    msgs = ["If you're experiencing occasional or mild symptoms that don't significantly impact "
                            "your daily life, self-care practices and seeking support from friends or loved ones "
                            "may be helpful.",
                            "While you might not require immediate treatment, it could be beneficial to monitor "
                            "your symptoms and consider seeking professional help if they worsen or persist."]
                    rand = random.randint(0, 1)
                    msg = msgs[rand]
                elif prediction < 0.75:
                    msgs = ["If you're finding that your symptoms are significantly affecting your daily life, "
                            "relationships, or work, it's important to reach out to a mental health professional "
                            "for a comprehensive assessment.",
                            "A mental health provider can help identify the underlying causes of your concerns and "
                            "develop a tailored treatment plan to address them effectively.",
                            "Seeking support from a mental health professional is a courageous step towards "
                            "improving your well-being. They have the expertise to guide you through this process."]
                    rand = random.randint(0, 2)
                    msg = msgs[rand]
                else:
                    msgs = ["I'm really concerned about what you're experiencing. It's crucial to seek immediate help "
                            "from a mental health professional or a local crisis hotline. They can provide the "
                            "support you need during this difficult time.",
                            "If you're in a crisis or feel like you're in immediate danger, please don't hesitate "
                            "to contact emergency services or go to the nearest emergency room. They are equipped "
                            "to handle urgent mental health situations.",
                            "Your safety and well-being are of utmost importance. Please reach out to a mental "
                            "health professional or a helpline right away. They are trained to provide the "
                            "assistance you need in this critical situation."]
                    rand = random.randint(0, 2)
                    msg = msgs[rand]

                st.write('You are fine!' if prediction < 0.5 else 'You need some treatment.')
                st.write(msg)
    else:
        st.subheader('About Us')


if __name__ == '__main__':
    main()
