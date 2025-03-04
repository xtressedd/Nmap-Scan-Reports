import xml.etree.ElementTree as ET
import csv

def parse_nmap_xml(xml_file, output_csv):
    """
    Parsea un archivo XML de Nmap y extrae información de los puertos abiertos y sus servicios.
    Guarda los resultados en un archivo CSV.
    
    Parámetros:
    xml_file (str): Ruta del archivo XML de Nmap.
    output_csv (str): Ruta del archivo CSV de salida.
    """
    # Cargar el archivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = []  # Lista para almacenar la información extraída
    
    # Iterar sobre los hosts detectados en el escaneo
    for host in root.findall("host"):
        ip_address = host.find("address").attrib.get("addr")  # Obtener la dirección IP del host
        
        # Buscar los puertos abiertos en el host
        for port in host.findall("ports/port"):
            port_id = port.attrib.get("portid")  # Obtener el número de puerto
            protocol = port.attrib.get("protocol")  # Obtener el protocolo (TCP/UDP)
            state = port.find("state").attrib.get("state")  # Obtener el estado del puerto (open, closed, filtered)
            
            # Obtener el nombre del servicio si está disponible, de lo contrario, marcar como "Unknown"
            service = port.find("service").attrib.get("name") if port.find("service") is not None else "Unknown"
            
            # Agregar los datos a la lista
            data.append([ip_address, port_id, protocol, state, service])
    
    # Guardar los datos extraídos en un archivo CSV
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Port", "Protocol", "State", "Service"])  # Encabezado del CSV
        writer.writerows(data)  # Escribir los datos extraídos
    print("Script ejecutado correctamente")
    print(f"Datos guardados en {output_csv}")

# Ejemplo de uso con un archivo XML de Nmap de ejemplo
parse_nmap_xml("servicios.nmap.xml", "nmap_results.csv")