import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF

df = pd.read_csv("data/comportamiento_estudiantes.csv")

# Visualización: progreso según abandono
plt.figure(figsize=(8, 5))
sns.boxplot(x="Abandono", y="Progreso_%", data=df, palette="Set2")
plt.title("Progreso según Abandono")
plt.tight_layout()
plt.savefig("images/grafico_engagement.png")
plt.close()

# Generar resumen en PDF
resumen = df.groupby("Abandono").agg({
    "Progreso_%": "mean",
    "Accesos_Semana": "mean",
    "Tareas_Entregadas": "mean",
    "Tiempo_Sesion_min": "mean"
}).round(2)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, "Informe de Engagement y Abandono", ln=True, align="C")
pdf.ln(10)

for abandono in resumen.index:
    r = resumen.loc[abandono]
    pdf.cell(200, 10, f"Abandono: {abandono}", ln=True)
    pdf.cell(200, 10, f"- Progreso medio: {r['Progreso_%']}%", ln=True)
    pdf.cell(200, 10, f"- Accesos promedio: {r['Accesos_Semana']}", ln=True)
    pdf.cell(200, 10, f"- Tareas entregadas promedio: {r['Tareas_Entregadas']}", ln=True)
    pdf.cell(200, 10, f"- Tiempo por sesión promedio: {r['Tiempo_Sesion_min']} min", ln=True)
    pdf.ln(5)

pdf.output("output/resumen_engagement.pdf")
print("Informe generado.")
