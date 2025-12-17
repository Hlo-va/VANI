import streamlit as st

st.set_page_config(page_title="Percentage & Grade Calculator")

st.title("Student Percentage & Grade Calculator")

st.write("This app collects marks for a number of subjects and computes the total, percentage and grade.")

n = st.number_input("Number of subjects", min_value=1, value=5, step=1)
total_per_subject = st.number_input("Total marks per subject", min_value=1.0, value=100.0)

st.header("Enter Marks")
marks = []
for i in range(int(n)):
	marks.append(st.number_input(f"Marks for subject {i+1}", min_value=0.0, value=0.0, key=f"m{i}"))

def compute_grade(pct: float) -> str:
	if pct >= 90:
		return "A+"
	if pct >= 80:
		return "A"
	if pct >= 70:
		return "B"
	if pct >= 60:
		return "C"
	if pct >= 50:
		return "D"
	return "F"

if st.button("Calculate Percentage & Grade"):
	max_total = total_per_subject * n
	obtained = sum(marks)
	if any(m < 0 for m in marks):
		st.error("Marks cannot be negative.")
	else:
		if any(m > total_per_subject for m in marks):
			st.warning("Some entered marks exceed the total per subject; calculation will continue.")
		percentage = (obtained / max_total) * 100 if max_total > 0 else 0.0
		grade = compute_grade(percentage)

		st.subheader("Result")
		st.write(f"**Total Obtained:** {obtained} / {max_total}")
		st.write(f"**Percentage:** {percentage:.2f}%")
		st.write(f"**Grade:** {grade}")
