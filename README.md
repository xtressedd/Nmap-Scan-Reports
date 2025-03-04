# 🔍 Nmap Scan Reports  

Este repositorio contiene un script en Python para analizar escaneos de Nmap y exportarlos a CSV.  
Está pensado para pentesters junior que quieran automatizar la extracción de datos de escaneos.  

---

## 📂 Archivos  

| Archivo               | Descripción |
|----------------------|------------|
| `parse_nmap_xml.py`  | Script en Python que procesa el XML de Nmap y genera un CSV con los puertos abiertos. |
| `nmap_results.csv`   | Resultados del escaneo, exportados en formato CSV. |
| `servicios.nmap.xml` | Archivo XML generado por Nmap con el escaneo realizado. |

---

## 🚀 Uso del script  

Para usar este script, sigue estos pasos:  

1️⃣ **Asegúrate de tener Python instalado**  
   - Puedes verificarlo ejecutando:  
     ```bash
     python --version
     ```

2️⃣ **Ejecuta el script con:**  
   ```bash
   python parse_nmap_xml.py
Esto generará un archivo nmap_results.csv con los datos procesados.

3️⃣ Abre nmap_results.csv con Excel, LibreOffice o cualquier visor de CSV.

🛠️ Requisitos
Python 3.x
Biblioteca estándar de Python (xml.etree.ElementTree y csv)
📌 Nota
Este repositorio es parte de mi formación en ciberseguridad y pentesting.
Si tienes sugerencias o mejoras, ¡haz un pull request! 🚀
