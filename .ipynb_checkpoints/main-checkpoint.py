from funciones_agentes import obtener_precio_accion

acciones = ["AAPL", "MSFT", "GOOGL", "AMZN"]

for ticker in acciones:
    print(obtener_precio_accion(ticker))