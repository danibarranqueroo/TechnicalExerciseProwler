import json

def leer_json(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def analizar_chequeos(data):
    total_checks = len(data)
    
    passed_checks = sum(1 for check in data if check["status"] == "PASS")
    failed_checks = sum(1 for check in data if check["status"] == "FAIL")
    
    failed_checks_list = [
        {"check": check["check"], "recommendation": check["recommendation"]}
        for check in data if check["status"] == "FAIL"
    ]
    
    return total_checks, passed_checks, failed_checks, failed_checks_list

def imprimir_resumen(total_checks, passed_checks, failed_checks, failed_checks_list):
    print(f"Total de chequeos realizados: {total_checks}")
    print(f"Chequeos que pasaron: {passed_checks}")
    print(f"Chequeos que fallaron: {failed_checks}\n")
    print("Chequeos fallidos y recomendaciones:")
    for idx, check in enumerate(failed_checks_list, start=1):
        print(f"{idx}. {check['check']}\n   Recomendación: {check['recommendation']}")

if __name__ == "__main__":
    data = leer_json('checks.json')

    total_checks, passed_checks, failed_checks, failed_checks_list = analizar_chequeos(data)
        
    imprimir_resumen(total_checks, passed_checks, failed_checks, failed_checks_list)
