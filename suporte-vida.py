def monitorar_ambiente(oxigenio, temperatura, pressao):
    print("=== Monitoramento do Ambiente ===")

    if oxigenio < 19.5:
        print(f"ALERTA: Nível de oxigênio crítico: {oxigenio}%")
    else:
        print(f"Oxigênio dentro do normal: {oxigenio}%")

    if temperatura < 18 or temperatura > 27:
        print(f"ALERTA: Temperatura fora do ideal: {temperatura}°C")
    else:
        print(f"Temperatura dentro do normal: {temperatura}°C")

    if pressao < 95 or pressao > 105:
        print(f"ALERTA: Pressão fora do ideal: {pressao} kPa")
    else:
        print(f"Pressão dentro do normal: {pressao} kPa")


if __name__ == "__main__":
    monitorar_ambiente(20.9, 22.0, 101.0)
