import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))


def predict_energy(temperature,exhaust_vacuum,ambient_pressure,relative_humidity):
    input=np.array([[temperature,exhaust_vacuum,ambient_pressure,relative_humidity]]).astype(np.float64)
    prediction=model.predict(input)
    
    return float(prediction)

def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">PP Energy Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    temperature = st.text_input("temperature","")
    exhaust_vacuum = st.text_input("exhaust_vacuum","")
    ambient_pressure = st.text_input("ambient_pressure","")
    relative_humidity=st.text_input("relative_humidity","")
    
    if st.button("Predict"):
        output=predict_energy(temperature,exhaust_vacuum,ambient_pressure,relative_humidity)
        st.success('The Energy Output will be {}'.format(round(output,2)))

        

if __name__=='__main__':
    main()