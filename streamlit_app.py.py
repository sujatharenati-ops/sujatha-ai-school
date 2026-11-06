import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import csv
from datetime import datetime

# --- AI BRAIN - SAME AS BEFORE ---
X = [
    [10, 50], [20, 60], [20, 90], [30, 50], [30, 95], [40, 60],
    [40, 90], [45, 80], [48, 95],
    [50, 50], [55, 70], [60, 60], [70, 80], [75, 50],
    [80, 40], [85, 90], [90, 45], [90, 95], [95, 95], [100, 100]
]
y = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1]
model = DecisionTreeClassifier()
model.fit(X, y)

# --- WEB PAGE ---
st.set_page_config(page_title="Sujatha's AI School App", page_icon="🎓")
st.title("🎓 Sujatha's AI School App - Day 7 Web Version")
st.write("Made by Sujatha - 2000 Java to 2026 AI")

# Inputs - Now on Web!
name = st.text_input("Student Name")
marks = st.number_input("Enter Marks (0-100)", min_value=0, max_value=100, value=75)
attend = st.number_input("Enter Attendance % (0-100)", min_value=0, max_value=100, value=80)

if st.button("Predict + Save", type="primary"):
    if not name:
        st.error("Please enter Name!")
    else:
        pred = model.predict([[marks, attend]])[0]

        if pred == 0:
            grade = "F"
            status = "FAIL"
            st.error(f"{name} - Marks: {marks}, Att: {attend}% - {status} - Grade: {grade}")
        else:
            status = "PASS"
            if marks >= 90:
                grade = "A+"
            elif marks >= 75:
                grade = "A"
            elif marks >= 60:
                grade = "B"
            else:
                grade = "C"
            st.success(f"{name} - Marks: {marks}, Att: {attend}% - {status} - Grade: {grade}")
            st.balloons()

        # Save to CSV - Same as before
        with open("results.csv", "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%d-%m-%Y %H:%M"), name, marks, attend, status, grade])
        st.info("Saved to results.csv")

st.divider()
st.write("### All Saved Students")
try:
    with open("results.csv", "r", encoding="utf-8-sig") as f:
        data = f.read()
        st.text(data)
except:
    st.write("No students saved yet. Add your first student above!")

st.caption("Day 7 - From Desktop to Web - Next: Share on Internet!")