import yfinance as yf

def obtener_precio_accion(consulta):
    try:
        accion = yf.Ticker(consulta.upper())
        info = accion.info
        empresa = info.get("longName", "N/A")
        precio = info.get("currentPrice", "N/A")
        divisa = info.get("currency", "N/A")
        ticker = consulta.upper()
        return f"{empresa} [{ticker}] ${precio} {divisa.upper()}."
    except Exception as e:
        return f"No se pudo obtener el precio: {e}"