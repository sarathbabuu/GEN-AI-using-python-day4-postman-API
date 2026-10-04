
import streamlit as st


# -----------------------------
# Grade calculation
# -----------------------------
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# -----------------------------
# Session state
# -----------------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -----------------------------
# Page title
# -----------------------------
st.title("🎓 Grade Manager")

st.write("Add students and view the class results.")


# -----------------------------
# Add student form
# -----------------------------
st.subheader("Add Student")

with st.form("student_form"):
    name = st.text_input("Student Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:
        if not name.strip():
            st.error("Please enter a student name.")
        elif mark < 0 or mark > 100:
            st.error("Mark must be between 0 and 100.")
        else:
            student = {
                "Name": name.strip(),
                "Mark": mark,
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# -----------------------------
# Student results
# -----------------------------
st.subheader("Student Results")

if st.session_state.students:

    st.dataframe(
        st.session_state.students,
        use_container_width=True,
        hide_index=True
    )

    # Get all marks
    marks = [
        student["Mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # -----------------------------
    # Class figures
    # -----------------------------
    st.subheader("Class Figures")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Class Average", f"{average:.2f}")

    with col2:
        st.metric("Highest Mark", highest)

    with col3:
        st.metric("Lowest Mark", lowest)

else:
    st.info("No students added yet.")